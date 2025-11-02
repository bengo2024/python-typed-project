"""Script d'auto-correction des erreurs détectées par MyPy et Ruff."""

import subprocess
import sys


def run_command(cmd: list[str]) -> tuple[int, str, str]:
    """Exécute une commande et retourne le code de retour, stdout et stderr."""
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return result.returncode, result.stdout, result.stderr


def auto_fix_ruff() -> bool:
    """Applique les corrections automatiques de Ruff."""
    print("🔧 Application des corrections Ruff...")

    # Ruff fix
    returncode, stdout, stderr = run_command(
        ["python", "-m", "ruff", "check", "--fix", "."]
    )

    if returncode == 0:
        print("✅ Ruff: Toutes les erreurs corrigées")
        return True

    # Essayer avec --unsafe-fixes pour les corrections plus agressives
    returncode, stdout, stderr = run_command(
        ["python", "-m", "ruff", "check", "--fix", "--unsafe-fixes", "."]
    )

    if "fixed" in stdout.lower():
        print(f"✅ Ruff: Corrections appliquées\n{stdout}")
        return True

    print("⚠️ Ruff: Certaines erreurs ne peuvent pas être corrigées automatiquement")
    return False


def auto_fix_mypy() -> bool:
    """Tente de corriger les erreurs MyPy basiques."""
    print("🔧 Analyse des erreurs MyPy...")

    # MyPy ne peut pas auto-corriger, mais on peut détecter les erreurs
    returncode, stdout, stderr = run_command(["python", "-m", "mypy", "main.py"])

    if returncode == 0:
        print("✅ MyPy: Aucune erreur de typage")
        return True

    print("⚠️ MyPy: Les erreurs de typage nécessitent une correction manuelle")
    print(f"Erreurs détectées:\n{stdout}")
    return False


def format_code() -> bool:
    """Formate le code avec Ruff."""
    print("✨ Formatage du code...")

    returncode, stdout, stderr = run_command(["python", "-m", "ruff", "format", "."])

    if returncode == 0:
        print("✅ Code formaté avec succès")
        return True

    print(f"⚠️ Erreur lors du formatage: {stderr}")
    return False


def main() -> None:
    """Fonction principale."""
    print("🤖 Démarrage de l'auto-correction...\n")

    fixes_applied = False

    # 1. Corriger les erreurs Ruff
    if auto_fix_ruff():
        fixes_applied = True

    # 2. Formater le code
    if format_code():
        fixes_applied = True

    # 3. Vérifier MyPy (info seulement)
    auto_fix_mypy()

    if fixes_applied:
        print("\n✅ Des corrections ont été appliquées!")
        print("📝 Les changements sont prêts à être committés")
        sys.exit(0)
    else:
        print("\n⚠️ Aucune correction automatique n'a pu être appliquée")
        print("🔍 Vérification manuelle nécessaire")
        sys.exit(1)


if __name__ == "__main__":
    main()
