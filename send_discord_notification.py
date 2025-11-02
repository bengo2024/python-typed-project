"""Envoie une notification Discord via webhook."""
import os
import sys
from datetime import datetime

import requests


def send_discord_webhook(
    webhook_url: str,
    mypy_errors: str,
    ruff_errors: str,
    french_errors: str,
    commit_msg: str,
    author: str,
    repo_url: str
) -> bool:
    """Envoie une notification Discord via webhook."""
    # Compter les erreurs
    mypy_count = mypy_errors.count("error:") if mypy_errors else 0
    ruff_count = len([line for line in ruff_errors.split("\n") if ":" in line and any(c in line for c in ["F", "E", "W", "I"])]) if ruff_errors else 0
    french_ok = "OK" in french_errors or not french_errors

    total_errors = mypy_count + ruff_count + (0 if french_ok else 1)

    # Déterminer la couleur
    if total_errors == 0:
        color = 0x28a745  # Vert
        title = "✅ CI/CD Réussi"
        emoji = "🎉"
    else:
        color = 0xdc3545  # Rouge
        title = "❌ Erreurs CI/CD Détectées"
        emoji = "⚠️"

    # Construire les champs
    fields = []

    if mypy_count > 0:
        mypy_preview = mypy_errors[:200] + "..." if len(mypy_errors) > 200 else mypy_errors
        fields.append({
            "name": f"🔍 MyPy ({mypy_count} erreur{'s' if mypy_count > 1 else ''})",
            "value": f"```\n{mypy_preview}\n```",
            "inline": False
        })
    else:
        fields.append({
            "name": "🔍 MyPy",
            "value": "✅ Aucune erreur",
            "inline": True
        })

    if ruff_count > 0:
        ruff_preview = ruff_errors[:200] + "..." if len(ruff_errors) > 200 else ruff_errors
        fields.append({
            "name": f"✨ Ruff ({ruff_count} erreur{'s' if ruff_count > 1 else ''})",
            "value": f"```\n{ruff_preview}\n```",
            "inline": False
        })
    else:
        fields.append({
            "name": "✨ Ruff",
            "value": "✅ Aucune erreur",
            "inline": True
        })

    if not french_ok:
        fields.append({
            "name": "🇫🇷 Français",
            "value": f"```\n{french_errors}\n```",
            "inline": False
        })
    else:
        fields.append({
            "name": "🇫🇷 Français",
            "value": "✅ Message parfait",
            "inline": True
        })

    # Ajouter les actions disponibles si erreurs
    if total_errors > 0:
        fields.append({
            "name": "💡 Actions Disponibles",
            "value": (
                "• Utilise `!erreurs` pour voir les détails\n"
                "• Utilise `!expliquer [type]` pour une explication IA\n"
                "• Utilise `!autofix` pour corriger automatiquement\n"
                f"• Vérifie le [rapport HTML]({repo_url}/actions)"
            ),
            "inline": False
        })

    # Construire le payload
    payload = {
        "embeds": [{
            "title": f"{emoji} {title}",
            "description": f"**Commit**: `{commit_msg}`\n**Auteur**: {author}\n**Total erreurs**: {total_errors}",
            "color": color,
            "fields": fields,
            "footer": {
                "text": f"CI/CD • {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
            },
            "url": f"{repo_url}/actions"
        }]
    }

    # Envoyer le webhook
    try:
        response = requests.post(webhook_url, json=payload, timeout=10)
        response.raise_for_status()
        print("✅ Notification Discord envoyée avec succès")
        return True
    except Exception as e:
        print(f"❌ Erreur lors de l'envoi de la notification Discord: {e}")
        return False


def main() -> None:
    """Fonction principale."""
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        print("⚠️ DISCORD_WEBHOOK_URL non défini, notification ignorée")
        sys.exit(0)

    # Lire les fichiers d'erreurs
    mypy_errors = ""
    ruff_errors = ""
    french_errors = ""

    try:
        with open("mypy_output.txt", encoding="utf-8") as f:
            mypy_errors = f.read()
    except FileNotFoundError:
        pass

    try:
        with open("ruff_output.txt", encoding="utf-8") as f:
            ruff_errors = f.read()
    except FileNotFoundError:
        pass

    try:
        with open("french_check.txt", encoding="utf-8") as f:
            french_errors = f.read()
    except FileNotFoundError:
        pass

    commit_msg = os.getenv("COMMIT_MSG", "N/A")
    author = os.getenv("COMMITTER_NAME", "Développeur")
    repo_url = f"https://github.com/{os.getenv('GITHUB_REPOSITORY', 'bengo2024/python-typed-project')}"

    # Envoyer la notification
    success = send_discord_webhook(
        webhook_url,
        mypy_errors,
        ruff_errors,
        french_errors,
        commit_msg,
        author,
        repo_url
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

