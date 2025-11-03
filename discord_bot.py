import os

import discord
from discord.ext import commands
from openai import OpenAI


# Configuration
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "bengo2024/python-typed-project")

# Initialiser le client Groq
groq_client = OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

# Initialiser le bot Discord
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Stocker les dernières erreurs
last_errors: dict[str, str] = {
    "mypy": "",
    "ruff": "",
    "french": "",
    "commit_msg": "",
    "author": "",
}


@bot.event  # type: ignore
async def on_ready() -> None:
    """Événement déclenché quand le bot est prêt."""
    print(f"✅ Bot connecté en tant que {bot.user}")
    print(f"📊 Serveurs: {len(bot.guilds)}")


@bot.command(name="erreurs")  # type: ignore
async def show_errors(ctx: commands.Context) -> None:
    """Affiche les dernières erreurs détectées."""
    if not any(last_errors.values()):
        await ctx.send("✅ Aucune erreur récente détectée!")
        return
    embed = discord.Embed(
        title="📊 Dernières Erreurs CI/CD",
        description=f"Commit: `{last_errors['commit_msg']}`\nAuteur: {last_errors['author']}",
        color=discord.Color.red(),
    )
    if last_errors["mypy"]:
        mypy_preview = (
            last_errors["mypy"][:500] + "..."
            if len(last_errors["mypy"]) > 500
            else last_errors["mypy"]
        )
        embed.add_field(
            name="🔍 MyPy (Types)", value=f"```\n{mypy_preview}\n```", inline=False
        )
    if last_errors["ruff"]:
        ruff_preview = (
            last_errors["ruff"][:500] + "..."
            if len(last_errors["ruff"]) > 500
            else last_errors["ruff"]
        )
        embed.add_field(
            name="✨ Ruff (Style)", value=f"```\n{ruff_preview}\n```", inline=False
        )
    if last_errors["french"]:
        embed.add_field(
            name="🇫🇷 Français", value=f"```\n{last_errors['french']}\n```", inline=False
        )
    await ctx.send(embed=embed)


@bot.command(name="expliquer")  # type: ignore
async def explain_error(
    ctx: commands.Context, *, error_type: str | None = None
) -> None:
    """Explique une erreur spécifique en détail avec l'IA.
    Usage: !expliquer [mypy|ruff|french]
    """
    if not error_type:
        await ctx.send(
            "❌ Spécifie le type d'erreur: `!expliquer mypy`, `!expliquer ruff`, ou `!expliquer french`"
        )
        return
    error_type = error_type.lower()
    if error_type not in ["mypy", "ruff", "french"]:
        await ctx.send(
            "❌ Type d'erreur invalide. Utilise: `mypy`, `ruff`, ou `french`"
        )
        return
    if not last_errors[error_type]:
        await ctx.send(f"✅ Aucune erreur {error_type.upper()} détectée!")
        return
    # Afficher un message de chargement
    loading_msg = await ctx.send("🤖 Analyse en cours avec l'IA...")
    try:
        # Demander à l'IA d'expliquer l'erreur
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """Tu es un mentor expert en Python. Explique les erreurs de manière:
                    1. Simple et pédagogique
                    2. Avec des exemples concrets
                    3. En français
                    4. Avec des suggestions de correction
                    Maximum 500 mots.""",
                },
                {
                    "role": "user",
                    "content": f"Explique cette erreur {error_type.upper()}:\n\n{last_errors[error_type]}",
                },
            ],
            temperature=0.5,
        )
        explanation = response.choices[0].message.content
        # Découper en chunks si trop long (limite Discord: 2000 caractères)
        if explanation is not None:
            chunks = [explanation[i : i + 1900] for i in range(0, len(explanation), 1900)]
        else:
            chunks = []
        await loading_msg.delete()
        for i, chunk in enumerate(chunks):
            embed = discord.Embed(
                title=f"💡 Explication {error_type.upper()} ({i+1}/{len(chunks)})",
                description=chunk,
                color=discord.Color.blue(),
            )
            await ctx.send(embed=embed)
        # Proposer l'auto-fix
        await ctx.send(
            "💡 **Astuce**: Utilise `!autofix` pour corriger automatiquement les erreurs Ruff!"
        )
    except Exception as e:
        await loading_msg.delete()
        await ctx.send(f"❌ Erreur lors de l'explication: {e!s}")


@bot.command(name="autofix")  # type: ignore
async def trigger_autofix(ctx: commands.Context) -> None:
    """Déclenche l'auto-fix et crée une Pull Request."""
    if not last_errors["ruff"] and not last_errors["mypy"]:
        await ctx.send("✅ Aucune erreur à corriger!")
        return
    await ctx.send("🤖 Déclenchement de l'auto-fix...")
    await ctx.send(
        "📝 Une Pull Request va être créée avec les corrections automatiques."
    )
    await ctx.send(f"🔗 Vérifie sur: https://github.com/{REPO_NAME}/pulls")
    # Note: L'auto-fix est déjà déclenché par le workflow GitHub Actions
    # Ce message informe juste l'utilisateur
    await ctx.send("✅ L'auto-fix a été déclenché par le workflow CI/CD!")


@bot.command(name="aide")  # type: ignore
async def help_command(ctx: commands.Context) -> None:
    """Affiche l'aide du bot."""
    embed = discord.Embed(
        title="🤖 Aide du Bot CI/CD",
        description="Bot pour expliquer les erreurs et déclencher les corrections",
        color=discord.Color.green(),
    )
    embed.add_field(
        name="!erreurs", value="Affiche les dernières erreurs détectées", inline=False
    )
    embed.add_field(
        name="!expliquer [type]",
        value="Explique une erreur en détail (mypy, ruff, french)",
        inline=False,
    )
    embed.add_field(
        name="!autofix",
        value="Déclenche l'auto-fix et crée une Pull Request",
        inline=False,
    )
    embed.add_field(name="!aide", value="Affiche ce message d'aide", inline=False)
    await ctx.send(embed=embed)


async def send_error_notification(channel_id: int, errors: dict[str, str]) -> None:
    """Envoie une notification d'erreur dans un canal Discord."""
    channel = bot.get_channel(channel_id)
    if not channel:
        print(f"❌ Canal {channel_id} introuvable")
        return
    # Mettre à jour les erreurs globales
    last_errors.update(errors)
    embed = discord.Embed(
        title="⚠️ Erreurs CI/CD Détectées",
        description=f"Commit: `{errors['commit_msg']}`\nAuteur: {errors['author']}",
        color=discord.Color.orange(),
    )
    if errors.get("mypy"):
        embed.add_field(
            name="🔍 MyPy", value="Erreurs de typage détectées", inline=True
        )
    if errors.get("ruff"):
        embed.add_field(name="✨ Ruff", value="Erreurs de style détectées", inline=True)
    if errors.get("french"):
        embed.add_field(name="🇫🇷 Français", value="Problème de français", inline=True)
    embed.add_field(
        name="💡 Actions disponibles",
        value="• `!erreurs` - Voir les détails\n• `!expliquer [type]` - Explication IA\n• `!autofix` - Corriger automatiquement",
        inline=False,
    )
    await channel.send(embed=embed)


def run_bot() -> None:
    """Lance le bot Discord."""
    if not DISCORD_TOKEN:
        print("❌ DISCORD_BOT_TOKEN non défini")
        return
    if not GROQ_API_KEY:
        print("❌ GROQ_API_KEY non défini")
        return
    print("🚀 Démarrage du bot Discord...")
    bot.run(DISCORD_TOKEN)


if __name__ == "__main__":
    run_bot()
