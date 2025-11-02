# 🚀 Projet Python Typé avec CI/CD Automatisé

[![CI/CD Python Typé + IA Français](https://github.com/VOTRE_USERNAME/python-typed-project/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/VOTRE_USERNAME/python-typed-project/actions/workflows/ci-cd.yml)

## 📝 Description

Projet Python démontrant un système CI/CD complet et automatisé avec GitHub Actions, incluant :

- ✅ **Vérification des types** avec MyPy (toutes les fonctions annotées)
- ✅ **Contrôle du style** avec Ruff (pas d'imports inutilisés, lignes ≤ 88 caractères)
- ✅ **Analyse du français** via OpenAI GPT-3.5 pour des messages de commit impeccables
- ✅ **Emails personnalisés** envoyés automatiquement (félicitations ou corrections)
- ✅ **Sécurité** avec GitHub Secrets pour les clés API
- ✅ **Collaboration** via branches et Pull Requests

## 🎯 Objectif

Garantir un code propre, typé, lisible, avec des messages de commit en français parfait, et un feedback IA instantané pour un rendu professionnel noté **20/20**.

## 🛠️ Technologies Utilisées

- **Python 3.10+**
- **MyPy** - Vérification statique des types
- **Ruff** - Linter et formateur ultra-rapide
- **OpenAI API** (GPT-3.5-turbo) - Analyse du français et génération d'emails
- **GitHub Actions** - CI/CD automatisé
- **SMTP Gmail** - Envoi d'emails
- **GitHub CLI** - Gestion des secrets et workflows

## 📦 Installation

```bash
# Cloner le dépôt
git clone https://github.com/VOTRE_USERNAME/python-typed-project.git
cd python-typed-project

# Installer les dépendances
pip install -r requirements.txt
```

## 🔧 Configuration

Consultez le **[Guide de Configuration Complet](GUIDE_CONFIGURATION.md)** pour :

1. Configurer les secrets GitHub
2. Obtenir une clé API OpenAI
3. Configurer l'email Gmail
4. Utiliser GitHub CLI
5. Tester en local

## 🚀 Utilisation

### Tester localement avant de pusher

```bash
# Vérifier les types
python -m mypy main.py

# Vérifier le style
python -m ruff check .

# Corriger automatiquement
python -m ruff check --fix .
```

### Workflow de développement

```bash
# 1. Créer une branche
git checkout -b feature/ma-fonctionnalite

# 2. Faire vos modifications
# ... éditer les fichiers ...

# 3. Tester localement
python -m mypy main.py && python -m ruff check .

# 4. Commiter (en français parfait !)
git add .
git commit -m "Ajout de la fonctionnalité de gestion des utilisateurs"

# 5. Pusher
git push origin feature/ma-fonctionnalite

# 6. Créer une Pull Request
gh pr create --title "Ajout gestion utilisateurs"
```

## 📧 Système d'Emails Automatisés

### Email de Félicitations ✅

Reçu quand tout est parfait :
- MyPy : aucune erreur de type
- Ruff : code conforme aux normes
- Français : message de commit impeccable

### Email de Correction ⚠️

Reçu en cas d'erreur :
- Message personnalisé et encourageant généré par l'IA
- Rapport détaillé des erreurs
- Conseils concrets pour corriger
- Adapté à la culture francophone

## 📊 Structure du Projet

```
python-typed-project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Workflow GitHub Actions
├── main.py                    # Fichier principal avec fonctions typées
├── mypy.ini                   # Configuration MyPy
├── ruff.toml                  # Configuration Ruff
├── requirements.txt           # Dépendances Python
├── test_ci.sh                 # Script de test local
├── test_openai.py             # Test de l'API OpenAI
├── GUIDE_CONFIGURATION.md     # Guide de configuration détaillé
├── PROCHAINES_ETAPES.md       # Checklist de finalisation
└── README.md                  # Ce fichier
```

## 🔐 Secrets GitHub Requis

| Secret | Description |
|--------|-------------|
| `OPENAI_API_KEY` | Clé API OpenAI pour GPT-3.5 |
| `EMAIL_HOST` | Serveur SMTP (smtp.gmail.com) |
| `EMAIL_PORT` | Port SMTP (587) |
| `EMAIL_USER` | Adresse email Gmail |
| `EMAIL_PASSWORD` | Mot de passe d'application Gmail |

## 📚 Documentation

- [Guide de Configuration](GUIDE_CONFIGURATION.md) - Configuration complète du projet
- [Workflow CI/CD](.github/workflows/ci-cd.yml) - Détails du pipeline

## 🤝 Contribution

1. Forkez le projet
2. Créez une branche (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Ajout d'une fonctionnalité incroyable'`)
4. Pushez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT.

## 👥 Auteurs

- **Votre Nom** - Développeur principal

## 🙏 Remerciements

- OpenAI pour l'API GPT-3.5
- La communauté Python pour MyPy et Ruff
- GitHub pour GitHub Actions
