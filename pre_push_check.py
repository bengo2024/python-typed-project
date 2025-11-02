"""
Script de vérification pre-push avec envoi d'email si erreurs détectées.
Bloque le push si des erreurs sont trouvées.
"""

import os
import subprocess
import sys
from datetime import datetime

from dotenv import load_dotenv


# Charger les variables d'environnement
load_dotenv()


def run_command(command: list[str]) -> tuple[int, str, str]:
    """Exécute une commande et retourne le code de retour, stdout et stderr."""
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return result.returncode, result.stdout, result.stderr


def count_errors(output: str, tool: str) -> int:
    """Compte le nombre d'erreurs dans la sortie."""
    if tool == "mypy":
        return output.count("error:")
    elif tool == "ruff":
        lines = output.split("\n")
        return len([line for line in lines if ":" in line and any(c in line for c in ["F", "E", "W", "I"])])
    return 0


def generate_error_report(mypy_output: str, ruff_output: str, mypy_errors: int, ruff_errors: int) -> str:
    """Génère un rapport d'erreurs formaté."""
    total_errors = mypy_errors + ruff_errors

    # Déterminer la gravité
    if total_errors <= 3:
        severity = "⚠️  FAIBLE"
        color_emoji = "🟠"
    elif total_errors <= 10:
        severity = "🔴 MOYENNE"
        color_emoji = "🟠"
    else:
        severity = "❌ CRITIQUE"
        color_emoji = "🔴"

    report = f"""
{'='*70}
{color_emoji} PUSH BLOQUÉ - ERREURS DÉTECTÉES
{'='*70}

📊 Gravité : {severity}
📈 Total : {total_errors} erreur(s)

{'='*70}
🔍 ERREURS MyPy ({mypy_errors} erreur(s))
{'='*70}
{mypy_output if mypy_output else "✅ Aucune erreur MyPy"}

{'='*70}
✨ ERREURS Ruff ({ruff_errors} erreur(s))
{'='*70}
{ruff_output if ruff_output else "✅ Aucune erreur Ruff"}

{'='*70}
🤖 COMMENT CORRIGER ?
{'='*70}

Option 1 : Utiliser le Chatbot Auto-Fix (RECOMMANDÉ)
   python chatbot_app.py
   → Cliquez sur "🔧 Auto-Fix"
   → Le chatbot corrige automatiquement les erreurs Ruff
   → Vous devez corriger manuellement les erreurs MyPy

Option 2 : Correction manuelle
   # Auto-fix Ruff
   python -m ruff check --fix .

   # Vérifier MyPy
   python -m mypy .

   # Corriger manuellement les erreurs MyPy

Option 3 : Forcer le push (NON RECOMMANDÉ)
   git push --no-verify
   ⚠️  Attention : Cela contourne les vérifications !

{'='*70}
"""
    return report


def send_error_email(report: str, branch_name: str) -> bool:
    """Envoie un email d'erreur à l'utilisateur."""
    try:
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from smtplib import SMTP

        from openai import OpenAI

        groq_api_key = os.getenv("GROQ_API_KEY")
        email_host = os.getenv("EMAIL_HOST")
        email_port = os.getenv("EMAIL_PORT")
        email_user = os.getenv("EMAIL_USER")
        email_password = os.getenv("EMAIL_PASSWORD")

        # Vérifier que les variables d'environnement sont définies
        if not all([groq_api_key, email_host, email_port, email_user, email_password]):
            print("⚠️  Variables d'environnement manquantes pour l'envoi d'email")
            return False

        # Type narrowing - on sait maintenant que toutes les variables sont définies
        assert groq_api_key is not None
        assert email_host is not None
        assert email_port is not None
        assert email_user is not None
        assert email_password is not None

        # Obtenir l'email de l'utilisateur depuis Git
        returncode, user_email, _ = run_command(["git", "config", "user.email"])
        if returncode != 0 or not user_email.strip():
            print("⚠️  Impossible de récupérer l'email de l'utilisateur Git")
            return False

        user_email = user_email.strip()

        # Obtenir le nom de l'utilisateur
        returncode, user_name, _ = run_command(["git", "config", "user.name"])
        user_name = user_name.strip() if returncode == 0 else "Développeur"

        # Générer un message personnalisé avec l'IA
        client = OpenAI(
            api_key=groq_api_key,
            base_url="https://api.groq.com/openai/v1"
        )

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"Tu es un mentor bienveillant en développement. Génère un email court (100 mots max) en français pour {user_name}, professionnel mais encourageant. Explique que son push a été bloqué car il y a des erreurs, et qu'il doit les corriger avant de pouvoir push. Mentionne le chatbot Auto-Fix comme solution rapide. Ton message doit être motivant, pas décourageant."
                },
                {
                    "role": "user",
                    "content": f"Branche: {branch_name}\n\nRapport:\n{report}"
                }
            ],
            temperature=0.7,
            max_tokens=200
        )

        ai_message = response.choices[0].message.content or "Ton push a été bloqué car des erreurs ont été détectées."

        # Créer l'email
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = user_email
        msg['Subject'] = f"🚫 Push Bloqué - Corrections Nécessaires ({branch_name})"

        full_body = f"""{ai_message}

{'='*70}
📊 RAPPORT DÉTAILLÉ
{'='*70}
{report}

{'='*70}
💡 ASTUCE
{'='*70}
Utilisez le chatbot Auto-Fix pour corriger rapidement :
   python chatbot_app.py

Le chatbot peut corriger automatiquement les erreurs Ruff et vous guider
pour les erreurs MyPy.

{'='*70}
🤖 Généré automatiquement par le système Pre-Push
"""

        msg.attach(MIMEText(full_body, 'plain', 'utf-8'))

        # Envoyer l'email
        server = SMTP(email_host, int(email_port))
        server.starttls()
        server.login(email_user, email_password)
        server.send_message(msg)
        server.quit()

        print(f"\n✅ Email envoyé à {user_email}")
        return True

    except Exception as e:
        print(f"\n⚠️  Erreur lors de l'envoi de l'email : {e}")
        return False


def main() -> int:
    """Fonction principale du pre-push check."""
    print("\n" + "="*70)
    print("🔍 VÉRIFICATION PRE-PUSH")
    print("="*70 + "\n")

    # Obtenir le nom de la branche
    returncode, branch_name, _ = run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    branch_name = branch_name.strip() if returncode == 0 else "unknown"

    print(f"🌿 Branche : {branch_name}")
    print(f"⏰ Heure : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

    # Exécuter MyPy
    print("🔍 Vérification MyPy...")
    mypy_returncode, mypy_stdout, mypy_stderr = run_command(["python", "-m", "mypy", "."])
    mypy_output = mypy_stdout + mypy_stderr
    mypy_errors = count_errors(mypy_output, "mypy")

    if mypy_errors == 0:
        print("   ✅ MyPy : 0 erreur")
    else:
        print(f"   ❌ MyPy : {mypy_errors} erreur(s)")

    # Exécuter Ruff
    print("✨ Vérification Ruff...")
    ruff_returncode, ruff_stdout, ruff_stderr = run_command(["python", "-m", "ruff", "check", "."])
    ruff_output = ruff_stdout + ruff_stderr
    ruff_errors = count_errors(ruff_output, "ruff")

    if ruff_errors == 0:
        print("   ✅ Ruff : 0 erreur")
    else:
        print(f"   ❌ Ruff : {ruff_errors} erreur(s)")

    total_errors = mypy_errors + ruff_errors

    print("\n" + "="*70)

    if total_errors == 0:
        print("✅ PUSH AUTORISÉ - Aucune erreur détectée")
        print("="*70 + "\n")
        return 0
    else:
        print(f"🚫 PUSH BLOQUÉ - {total_errors} erreur(s) détectée(s)")
        print("="*70 + "\n")

        # Générer le rapport
        report = generate_error_report(mypy_output, ruff_output, mypy_errors, ruff_errors)
        print(report)

        # Envoyer l'email
        print("\n📧 Envoi de l'email de notification...")
        send_error_email(report, branch_name)

        print("\n" + "="*70)
        print("💡 CONSEIL : Utilisez le chatbot Auto-Fix pour corriger rapidement")
        print("   python chatbot_app.py")
        print("="*70 + "\n")

        return 1


if __name__ == "__main__":
    sys.exit(main())

