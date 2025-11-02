"""Application web Flask pour le chatbot CI/CD interactif."""

import os
import subprocess
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from openai import OpenAI


# Charger les variables d'environnement depuis .env
load_dotenv()

app = Flask(__name__)

# Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
REPO_PATH = Path(__file__).parent

# Vérifier que la clé API est définie
if not GROQ_API_KEY:
    print("❌ ERREUR: La clé GROQ_API_KEY n'est pas définie !")
    print("📝 Créez un fichier .env avec :")
    print("   GROQ_API_KEY=gsk_votre_clé_ici")
    print("🔑 Obtenez votre clé sur : https://console.groq.com/keys")
    exit(1)

# Client Groq
groq_client = OpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

# Stocker l'historique de conversation
conversation_history: list[dict[str, str]] = []


def run_command(command: str) -> tuple[str, int]:
    """Exécute une commande shell et retourne la sortie."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            cwd=REPO_PATH,
            timeout=30,
            encoding="utf-8",
            errors="replace",  # Remplace les caractères invalides au lieu de crasher
        )
        return result.stdout + result.stderr, result.returncode
    except Exception as e:
        return f"Erreur: {e!s}", 1


def get_current_errors() -> dict[str, str]:
    """Récupère les erreurs actuelles du code."""
    errors = {"mypy": "", "ruff": "", "summary": ""}

    # Exécuter MyPy
    mypy_output, _ = run_command("python -m mypy . --ignore-missing-imports")
    if "error:" in mypy_output.lower() or "found" in mypy_output.lower():
        errors["mypy"] = mypy_output

    # Exécuter Ruff
    ruff_output, _ = run_command("python -m ruff check .")
    if ruff_output.strip() and "All checks passed" not in ruff_output:
        errors["ruff"] = ruff_output

    # Créer un résumé
    mypy_count = mypy_output.count("error:")
    ruff_lines = [
        line
        for line in ruff_output.split("\n")
        if ":" in line and any(c in line for c in ["F", "E", "W", "I"])
    ]
    ruff_count = len(ruff_lines)

    if mypy_count > 0 or ruff_count > 0:
        errors["summary"] = f"J'ai détecté {mypy_count + ruff_count} erreur(s) :\n"
        if mypy_count > 0:
            errors["summary"] += f"- {mypy_count} erreur(s) de typage (MyPy)\n"
        if ruff_count > 0:
            errors["summary"] += f"- {ruff_count} erreur(s) de style (Ruff)\n"
    else:
        errors["summary"] = "✅ Aucune erreur détectée ! Votre code est parfait !"

    return errors


def trigger_autofix() -> dict[str, str]:
    """Déclenche l'auto-fix et crée une Pull Request."""
    print("🔧 Démarrage de l'auto-fix...")

    # Créer une branche auto-fix
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    branch_name = f"auto-fix/{timestamp}"
    print(f"📝 Branche: {branch_name}")

    # Créer et checkout la branche
    print("🌿 Création de la branche...")
    checkout_output, checkout_code = run_command(f"git checkout -b {branch_name}")
    print(f"Checkout output: {checkout_output[:200]}")

    # Appliquer les corrections Ruff directement (sans auto_fix.py)
    print("🔍 Exécution de Ruff check --fix...")
    ruff_output, ruff_code = run_command("python -m ruff check --fix --unsafe-fixes .")
    print(f"Ruff output: {ruff_output[:200]}")

    print("✨ Exécution de Ruff format...")
    format_output, format_code = run_command("python -m ruff format .")
    print(f"Format output: {format_output[:200]}")

    # Vérifier s'il y a des changements
    print("📊 Vérification des changements...")
    diff_output, _ = run_command("git diff")
    print(f"Diff length: {len(diff_output)} caractères")

    if diff_output.strip():
        # Il y a des changements, on commit et push
        run_command("git add .")
        commit_output, _ = run_command(
            'git commit -m "🤖 Auto-Fix: Corrections automatiques via chatbot"'
        )
        push_output, push_code = run_command(f"git push origin {branch_name}")

        # Retourner à main
        run_command("git checkout main")

        if push_code == 0:
            return {
                "success": True,
                "message": f"✅ Corrections appliquées avec succès !\n\n📝 Changements :\n{ruff_output}\n\n🌿 Branche créée : {branch_name}\n\n🔗 Créez une Pull Request sur GitHub pour merger ces corrections.",
                "branch": branch_name,
            }
        else:
            return {
                "success": False,
                "message": f"❌ Erreur lors du push de la branche.\n\n{push_output}",
                "branch": None,
            }
    else:
        # Pas de changements, retourner à main
        run_command("git checkout main")
        run_command(f"git branch -D {branch_name}")
        return {
            "success": False,
            "message": "INFO: Aucune correction automatique disponible.\n\nRuff n'a trouvé aucune erreur à corriger automatiquement.\n\nLes erreurs MyPy nécessitent une correction manuelle car elles concernent les types.",
            "branch": None,
        }


@app.route("/")
def index() -> str:
    """Page d'accueil du chatbot."""
    return render_template("chatbot.html")


@app.route("/api/chat", methods=["POST"])
def chat() -> dict:
    """Endpoint pour discuter avec le chatbot."""
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message vide"}), 400

    # Ajouter le message de l'utilisateur à l'historique
    conversation_history.append({"role": "user", "content": user_message})

    # Récupérer les erreurs actuelles
    errors = get_current_errors()

    # Créer le contexte pour l'IA
    system_prompt = f"""Tu es un assistant expert en Python qui aide les développeurs à comprendre et corriger leurs erreurs de code.

Tu as accès aux erreurs actuelles du projet :

ERREURS MYPY :
{errors['mypy'] if errors['mypy'] else 'Aucune erreur MyPy'}

ERREURS RUFF :
{errors['ruff'] if errors['ruff'] else 'Aucune erreur Ruff'}

Réponds de manière :
1. Amicale et encourageante
2. Pédagogique avec des exemples
3. Concise (maximum 300 mots)
4. En français
5. Avec des emojis pour rendre la conversation agréable

IMPORTANT - Ce que l'Auto-Fix peut faire :
✅ L'Auto-Fix peut corriger UNIQUEMENT les erreurs Ruff (imports inutilisés, formatage, style)
❌ L'Auto-Fix NE PEUT PAS corriger les erreurs MyPy (types manquants) - celles-ci nécessitent une correction manuelle

Si l'utilisateur demande de corriger les erreurs :
- Pour les erreurs Ruff : propose le bouton "Auto-Fix"
- Pour les erreurs MyPy : explique qu'il faut les corriger manuellement et montre comment faire avec des exemples avant/après
"""

    # Appeler l'IA Groq
    try:
        response = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                *conversation_history,
            ],
            temperature=0.7,
            max_tokens=500,
        )

        bot_message = response.choices[0].message.content

        # Ajouter la réponse du bot à l'historique
        conversation_history.append({"role": "assistant", "content": bot_message})

        return jsonify(
            {
                "message": bot_message,
                "errors": errors,
                "timestamp": datetime.now().isoformat(),
            }
        )

    except Exception as e:
        return jsonify({"error": f"Erreur IA: {e!s}"}), 500


@app.route("/api/errors", methods=["GET"])
def get_errors() -> dict:
    """Récupère les erreurs actuelles."""
    errors = get_current_errors()
    return jsonify(errors)


@app.route("/api/autofix", methods=["POST"])
def autofix() -> dict:
    """Déclenche l'auto-fix."""
    try:
        result = trigger_autofix()
        return jsonify(result)
    except Exception as e:
        import traceback

        error_details = traceback.format_exc()
        print(f"❌ ERREUR AUTO-FIX: {e}")
        print(error_details)
        return jsonify(
            {
                "success": False,
                "message": f"❌ Erreur lors de l'auto-fix:\n\n{e!s}\n\nVoir les logs du serveur pour plus de détails.",
                "branch": None,
            }
        ), 500


@app.route("/api/reset", methods=["POST"])
def reset_conversation() -> dict:
    """Réinitialise la conversation."""
    conversation_history.clear()
    return jsonify({"message": "Conversation réinitialisée"})


if __name__ == "__main__":
    print("🤖 Démarrage du chatbot CI/CD...")
    print("📊 Accédez à l'interface : http://localhost:5000")
    print(
        "🔑 Assurez-vous que GROQ_API_KEY est défini dans vos variables d'environnement"
    )
    app.run(debug=True, host="0.0.0.0", port=5000)
