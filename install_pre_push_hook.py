"""
Script d'installation du Git Hook pre-push.
"""

import os
import stat
from pathlib import Path


def install_pre_push_hook() -> None:
    """Installe le Git Hook pre-push."""
    # Chemin du hook
    git_hooks_dir = Path(".git/hooks")
    pre_push_hook = git_hooks_dir / "pre-push"

    # Vérifier que le dossier .git existe
    if not git_hooks_dir.exists():
        print("❌ Erreur : Le dossier .git/hooks n'existe pas.")
        print("   Assurez-vous d'être dans un dépôt Git.")
        return

    # Contenu du hook
    hook_content = """#!/bin/sh
# Git Hook Pre-Push
# Vérifie MyPy et Ruff avant chaque push

echo ""
echo "🔍 Vérification pre-push en cours..."
echo ""

# Exécuter le script Python de vérification
python pre_push_check.py

# Récupérer le code de retour
exit_code=$?

if [ $exit_code -ne 0 ]; then
    echo ""
    echo "🚫 Push annulé en raison d'erreurs."
    echo ""
    echo "💡 Pour forcer le push (non recommandé) :"
    echo "   git push --no-verify"
    echo ""
    exit 1
fi

echo ""
echo "✅ Vérifications réussies ! Push en cours..."
echo ""
exit 0
"""

    # Écrire le hook
    with open(pre_push_hook, "w", encoding="utf-8", newline="\n") as f:
        f.write(hook_content)

    # Rendre le hook exécutable (Unix/Mac)
    if os.name != "nt":  # Si pas Windows
        st = os.stat(pre_push_hook)
        os.chmod(pre_push_hook, st.st_mode | stat.S_IEXEC)

    print("✅ Git Hook pre-push installé avec succès !")
    print(f"   Emplacement : {pre_push_hook}")
    print("")
    print("🎯 Fonctionnement :")
    print("   1. À chaque 'git push', le hook vérifie MyPy et Ruff")
    print("   2. Si des erreurs sont détectées :")
    print("      - Le push est BLOQUÉ")
    print("      - Un email vous est envoyé")
    print("      - Le rapport d'erreurs s'affiche")
    print("   3. Si aucune erreur : le push continue normalement")
    print("")
    print("💡 Pour désactiver temporairement :")
    print("   git push --no-verify")
    print("")


if __name__ == "__main__":
    install_pre_push_hook()
