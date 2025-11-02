"""Génère un rapport HTML des erreurs MyPy et Ruff."""

import os
from datetime import datetime


def generate_html_report(
    mypy_output: str,
    ruff_output: str,
    french_output: str,
    commit_msg: str,
    committer_name: str,
) -> str:
    """Génère un rapport HTML stylisé des erreurs."""
    # Compter les erreurs
    mypy_errors = mypy_output.count("error:") if mypy_output else 0
    ruff_errors = (
        len(
            [
                line
                for line in ruff_output.split("\n")
                if ":" in line and any(c in line for c in ["F", "E", "W", "I"])
            ]
        )
        if ruff_output
        else 0
    )
    french_ok = "OK" in french_output or not french_output

    total_errors = mypy_errors + ruff_errors + (0 if french_ok else 1)

    # Déterminer le statut
    if total_errors == 0:
        status_color = "#28a745"
        status_text = "✅ SUCCÈS"
        status_emoji = "🎉"
    else:
        status_color = "#dc3545"
        status_text = "❌ ERREURS DÉTECTÉES"
        status_emoji = "⚠️"

    html = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport CI/CD - {committer_name}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        .header {{
            background: {status_color};
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header .emoji {{
            font-size: 4em;
            margin-bottom: 10px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .stat-card .number {{
            font-size: 3em;
            font-weight: bold;
            color: #667eea;
        }}
        .stat-card .label {{
            color: #6c757d;
            margin-top: 10px;
            font-size: 0.9em;
        }}
        .stat-card.error .number {{
            color: #dc3545;
        }}
        .stat-card.success .number {{
            color: #28a745;
        }}
        .section {{
            padding: 30px;
            border-bottom: 1px solid #e9ecef;
        }}
        .section h2 {{
            color: #333;
            margin-bottom: 20px;
            font-size: 1.8em;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .section-icon {{
            font-size: 1.2em;
        }}
        .commit-info {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            margin-bottom: 20px;
        }}
        .commit-info strong {{
            color: #667eea;
        }}
        .error-box {{
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            border-radius: 5px;
            margin: 10px 0;
        }}
        .error-box.critical {{
            background: #f8d7da;
            border-left-color: #dc3545;
        }}
        .error-box.success {{
            background: #d4edda;
            border-left-color: #28a745;
        }}
        pre {{
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 20px;
            border-radius: 8px;
            overflow-x: auto;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            line-height: 1.5;
        }}
        .footer {{
            background: #343a40;
            color: white;
            padding: 20px;
            text-align: center;
        }}
        .footer a {{
            color: #667eea;
            text-decoration: none;
        }}
        .timestamp {{
            color: #6c757d;
            font-size: 0.9em;
            margin-top: 10px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="emoji">{status_emoji}</div>
            <h1>{status_text}</h1>
            <p>Rapport CI/CD - {committer_name}</p>
            <p class="timestamp">Généré le {datetime.now().strftime("%d/%m/%Y à %H:%M:%S")}</p>
        </div>

        <div class="stats">
            <div class="stat-card {'error' if mypy_errors > 0 else 'success'}">
                <div class="number">{mypy_errors}</div>
                <div class="label">Erreurs MyPy</div>
            </div>
            <div class="stat-card {'error' if ruff_errors > 0 else 'success'}">
                <div class="number">{ruff_errors}</div>
                <div class="label">Erreurs Ruff</div>
            </div>
            <div class="stat-card {'error' if not french_ok else 'success'}">
                <div class="number">{'❌' if not french_ok else '✅'}</div>
                <div class="label">Français</div>
            </div>
            <div class="stat-card {'error' if total_errors > 0 else 'success'}">
                <div class="number">{total_errors}</div>
                <div class="label">Total Erreurs</div>
            </div>
        </div>

        <div class="section">
            <h2><span class="section-icon">📝</span> Informations du Commit</h2>
            <div class="commit-info">
                <p><strong>Message :</strong> {commit_msg}</p>
                <p><strong>Auteur :</strong> {committer_name}</p>
            </div>
        </div>

        <div class="section">
            <h2><span class="section-icon">🔍</span> MyPy - Vérification des Types</h2>
            {f'<div class="error-box critical"><strong>⚠️ {mypy_errors} erreur(s) détectée(s)</strong></div>' if mypy_errors > 0 else '<div class="error-box success"><strong>✅ Aucune erreur de typage</strong></div>'}
            {f'<pre>{mypy_output}</pre>' if mypy_output else '<p>Aucune sortie MyPy</p>'}
        </div>

        <div class="section">
            <h2><span class="section-icon">✨</span> Ruff - Vérification du Style</h2>
            {f'<div class="error-box critical"><strong>⚠️ {ruff_errors} erreur(s) détectée(s)</strong></div>' if ruff_errors > 0 else '<div class="error-box success"><strong>✅ Code conforme au style</strong></div>'}
            {f'<pre>{ruff_output}</pre>' if ruff_output else '<p>Aucune sortie Ruff</p>'}
        </div>

        <div class="section">
            <h2><span class="section-icon">🇫🇷</span> Vérification du Français</h2>
            {f'<div class="error-box critical"><strong>⚠️ Problème détecté</strong><br>{french_output}</div>' if not french_ok else '<div class="error-box success"><strong>✅ Message en français parfait</strong></div>'}
        </div>

        <div class="footer">
            <p>🤖 Généré automatiquement par le système CI/CD</p>
            <p>Propulsé par <a href="https://groq.com">Groq AI</a> • MyPy • Ruff</p>
        </div>
    </div>
</body>
</html>
"""
    return html


def main() -> None:
    """Fonction principale."""
    # Lire les fichiers de sortie
    mypy_output = ""
    ruff_output = ""
    french_output = ""

    try:
        with open("mypy_output.txt", encoding="utf-8") as f:
            mypy_output = f.read()
    except FileNotFoundError:
        pass

    try:
        with open("ruff_output.txt", encoding="utf-8") as f:
            ruff_output = f.read()
    except FileNotFoundError:
        pass

    try:
        with open("french_check.txt", encoding="utf-8") as f:
            french_output = f.read()
    except FileNotFoundError:
        pass

    commit_msg = os.getenv("COMMIT_MSG", "N/A")
    committer_name = os.getenv("COMMITTER_NAME", "Développeur")

    # Générer le rapport HTML
    html_content = generate_html_report(
        mypy_output, ruff_output, french_output, commit_msg, committer_name
    )

    # Sauvegarder le rapport
    with open("ci_report.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Rapport HTML généré : ci_report.html")


if __name__ == "__main__":
    main()
