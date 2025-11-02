# 🚀 Projet Python Typé avec CI/CD Automatisé + E-Commerce Shopify

[![CI/CD Status](https://github.com/bengo2024/python-typed-project/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/bengo2024/python-typed-project/actions/workflows/ci-cd.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg)](http://mypy-lang.org/)
[![AI: Groq](https://img.shields.io/badge/AI-Groq%20Llama%203.3-orange.svg)](https://groq.com/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)

## 📝 Description

**Plateforme complète** combinant un système CI/CD automatisé avec une application e-commerce fonctionnelle, le tout en Python 100% typé.

### 🎯 Fonctionnalités Principales

#### 🤖 Pipeline CI/CD Intelligent
- ✅ **Vérification des types** avec MyPy (Python 3.10+)
- ✅ **Contrôle du style** avec Ruff (ultra-rapide, 100x plus rapide que Pylint)
- ✅ **IA Groq** (Llama 3.3-70b) pour suggestions de correction
- ✅ **Emails automatisés** avec rapports HTML détaillés
- ✅ **Auto-Fix automatique** avec création de branches Git
- ✅ **Chatbot Web IA** pour expliquer les erreurs en temps réel
- ✅ **Notifications Discord** pour le suivi d'équipe

#### 🛍️ Application E-Commerce "Shopify"
- ✅ **Catalogue de produits** avec recherche et filtres
- ✅ **Panier d'achat** avec gestion des quantités
- ✅ **Système d'authentification** (clients et admins)
- ✅ **Processus de commande** complet
- ✅ **Dashboard admin** pour gestion des produits
- ✅ **Base de données SQLite** avec modèles typés
- ✅ **Interface moderne** avec CSS responsive

## 🎯 Objectif Pédagogique

Démontrer la maîtrise de :
- **Python moderne** (3.10+) avec typage statique
- **Outils de qualité** (MyPy, Ruff) et leurs avantages
- **CI/CD automatisé** avec GitHub Actions
- **Développement web** avec Flask
- **Intégration IA** pour améliorer la productivité
- **Architecture logicielle** propre et maintenable

## 🛠️ Technologies Utilisées

### Backend & Outils
- **Python 3.10+** - Typage moderne (union types `|`, generics simplifiés)
- **MyPy 1.11.1** - Vérificateur de types statiques (standard officiel)
- **Ruff 0.6.0** - Linter/formateur ultra-rapide (100x plus rapide que Pylint)
- **Flask 3.0.0** - Framework web micro et flexible
- **SQLite 3.x** - Base de données embarquée (zéro configuration)

### IA & Automatisation
- **Groq API** (Llama 3.3-70b) - IA gratuite et ultra-rapide (500 tokens/s)
- **GitHub Actions** - Pipeline CI/CD automatisé
- **SMTP Gmail** - Notifications par email avec rapports HTML
- **Discord Webhooks** - Notifications d'équipe en temps réel

### Frontend
- **Jinja2** - Templates HTML dynamiques
- **CSS3** - Design moderne et responsive
- **JavaScript Vanilla** - Interactions client (fetch API)

## 📦 Installation Rapide (5 minutes)

### Pour les Nouveaux Collaborateurs

**📖 Consultez le [Quick Start Guide](QUICK_START.md)** pour une installation guidée pas à pas.

```bash
# 1. Cloner le projet
git clone https://github.com/bengo2024/python-typed-project.git
cd python-typed-project

# 2. Créer l'environnement virtuel
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer les variables d'environnement
copy .env.example .env  # Windows
# cp .env.example .env  # Linux/Mac
# Puis éditez .env et ajoutez votre GROQ_API_KEY

# 5. Tester l'installation
python -m mypy --version
python -m ruff --version
```

### Obtenir une Clé Groq (GRATUIT)

1. Allez sur https://console.groq.com/keys
2. Créez un compte (email + mot de passe)
3. Générez une clé API
4. Ajoutez dans `.env` : `GROQ_API_KEY=gsk_...`

## 🚀 Utilisation

### Démarrer les Applications

#### Chatbot CI/CD (Port 5000)
```bash
python chatbot_app.py
```
Accédez à : **http://localhost:5000**

**Fonctionnalités :**
- 🔄 Actualiser les erreurs en temps réel
- 💬 Poser des questions à l'IA sur les erreurs
- 🔧 Auto-Fix automatique (crée une branche Git)
- 📊 Visualisation des erreurs MyPy et Ruff

#### Application Shopify (Port 5001)
```bash
python -m shopify.app
# OU
start_shopify.bat  # Windows
```
Accédez à : **http://localhost:5001**

**Comptes de test :**
- **Client** : `alice@example.com` / `password123`
- **Admin** : `admin@shopify.com` / `admin123`

### Workflow de Développement

```bash
# 1. Créer votre branche
git checkout -b feature/votre-nom-fonctionnalite

# 2. Faire vos modifications
# ... éditer les fichiers ...

# 3. Vérifier AVANT de commit
python -m mypy .
python -m ruff check .

# 4. Auto-corriger Ruff
python -m ruff check --fix .
python -m ruff format .

# 5. Commit avec message clair
git add .
git commit -m "✨ Ajout de la fonctionnalité X"

# 6. Push vers votre branche
git push origin feature/votre-nom-fonctionnalite

# 7. Créer une Pull Request sur GitHub
```

### Commandes Utiles

```bash
# Vérification complète
python -m mypy . && python -m ruff check .

# Auto-fix + Format
python -m ruff check --fix . && python -m ruff format .

# Initialiser la base de données Shopify
python -m shopify.init_data

# Voir les erreurs actuelles
python chatbot_app.py  # Puis cliquez sur "Actualiser"
```

## 🎓 Documentation pour Collaborateurs

### 📚 Guides Disponibles

| Guide | Description | Pour Qui ? |
|-------|-------------|------------|
| **[QUICK_START.md](QUICK_START.md)** | Installation rapide (5 min) | 🆕 Nouveaux membres |
| **[GUIDE_COLLABORATEURS.md](GUIDE_COLLABORATEURS.md)** | Guide complet du projet | 👥 Tous les collaborateurs |
| **[ARCHITECTURE_TECHNIQUE.md](ARCHITECTURE_TECHNIQUE.md)** | Détails techniques approfondis | 🔧 Développeurs avancés |
| **[shopify/README.md](shopify/README.md)** | Documentation Shopify | 🛍️ Développeurs e-commerce |

### 🤔 Pourquoi Ruff au lieu d'ESLint ?

**ESLint est pour JavaScript, pas Python !**

Pour Python, nous avons choisi **Ruff** car :
- ⚡ **100x plus rapide** que Pylint (écrit en Rust)
- 🎯 **Tout-en-un** : remplace 8 outils (Flake8, Black, isort, etc.)
- 🔧 **Auto-Fix puissant** : corrige automatiquement les erreurs
- ⚙️ **Configuration simple** : un seul fichier `ruff.toml`
- 🚀 **Moderne** : support Python 3.10+

**Benchmark :**
```
Pylint:  8.2 secondes
Flake8:  2.1 secondes
Ruff:    0.08 secondes  ✅
```

### 🔍 Pourquoi MyPy au lieu de TypeScript ?

**TypeScript est pour JavaScript, pas Python !**

Pour Python, nous avons choisi **MyPy** car :
- 📜 **Standard officiel** : créé par Guido van Rossum (créateur de Python)
- 🎯 **Typage graduel** : ajoutez des types progressivement
- 🆕 **Types modernes** : support Python 3.10+ (`str | None`, `list[dict]`)
- 🐛 **Détection précoce** : trouve les erreurs avant l'exécution
- 🏢 **Utilisé en production** : Google, Dropbox, Instagram

**Exemple :**
```python
# Sans types (Python classique)
def add(a, b):
    return a + b

# Avec types (Python typé)
def add(a: int, b: int) -> int:
    return a + b
```

### 📧 Système de Notifications

#### Email Automatique 📧
- ✅ Envoyé à chaque push
- ✅ Rapport HTML des erreurs en pièce jointe
- ✅ Suggestions de correction générées par IA
- ✅ Lien vers le commit GitHub

#### Notification Discord 💬
- ✅ Statut du build (✅ ou ❌)
- ✅ Nombre d'erreurs
- ✅ Lien vers les logs GitHub Actions

## 📊 Structure du Projet

```
python-typed-project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml                    # Pipeline GitHub Actions
├── shopify/                             # Application E-Commerce
│   ├── __init__.py
│   ├── app.py                          # Application Flask Shopify
│   ├── models.py                       # Modèles de données typés
│   ├── database.py                     # Gestion SQLite
│   ├── init_data.py                    # Données de test
│   └── README.md                       # Documentation Shopify
├── templates/                           # Templates HTML (Jinja2)
│   ├── chatbot.html                    # Interface chatbot
│   └── shopify/                        # Templates Shopify
│       ├── index.html
│       ├── products.html
│       ├── cart.html
│       └── ...
├── static/                              # Assets statiques
│   ├── css/
│   │   ├── chatbot.css
│   │   └── shopify.css
│   ├── js/
│   │   ├── chatbot.js
│   │   └── shopify.js
│   └── images/
├── chatbot_app.py                       # Application Chatbot Flask
├── main.py                              # Fichier de test CI/CD
├── mypy.ini                             # Configuration MyPy
├── ruff.toml                            # Configuration Ruff
├── requirements.txt                     # Dépendances Python
├── .env.example                         # Template variables d'environnement
├── .env                                 # Variables d'environnement (SECRET!)
├── QUICK_START.md                       # Guide démarrage rapide
├── GUIDE_COLLABORATEURS.md              # Guide complet collaborateurs
├── ARCHITECTURE_TECHNIQUE.md            # Documentation technique
└── README.md                            # Ce fichier
```

## 🔐 Configuration GitHub Secrets

Pour que le pipeline CI/CD fonctionne, configurez ces secrets dans GitHub :

| Secret | Description | Obligatoire ? |
|--------|-------------|---------------|
| `GROQ_API_KEY` | Clé API Groq (gratuite) | ✅ Oui |
| `EMAIL_HOST` | Serveur SMTP (smtp.gmail.com) | ⚠️ Optionnel |
| `EMAIL_PORT` | Port SMTP (587) | ⚠️ Optionnel |
| `EMAIL_USER` | Adresse email Gmail | ⚠️ Optionnel |
| `EMAIL_PASSWORD` | Mot de passe d'application Gmail | ⚠️ Optionnel |
| `DISCORD_WEBHOOK_URL` | URL webhook Discord | ⚠️ Optionnel |

**Comment configurer :**
1. Allez dans **Settings** → **Secrets and variables** → **Actions**
2. Cliquez sur **New repository secret**
3. Ajoutez chaque secret

## 🤝 Contribution

### Pour les Membres du Groupe

1. **Lisez le [Quick Start](QUICK_START.md)** pour l'installation
2. **Créez votre branche** : `git checkout -b feature/votre-nom-fonctionnalite`
3. **Faites vos modifications** en respectant le typage
4. **Vérifiez localement** : `python -m mypy . && python -m ruff check .`
5. **Committez** : `git commit -m "✨ Description claire"`
6. **Pushez** : `git push origin feature/votre-nom-fonctionnalite`
7. **Créez une Pull Request** sur GitHub

### Règles de Contribution

- ✅ **Toujours typer** vos fonctions (MyPy doit passer)
- ✅ **Respecter le style** Ruff (utilisez `ruff check --fix`)
- ✅ **Messages de commit clairs** avec emojis (✨ 🐛 📚 🔧)
- ✅ **Tester localement** avant de push
- ✅ **Créer une branche** par fonctionnalité
- ❌ **Jamais commit** le fichier `.env`

## 🎯 Fonctionnalités Avancées

### Auto-Fix Automatique
Le chatbot peut créer automatiquement une branche Git avec les corrections Ruff :
1. Ouvrez http://localhost:5000
2. Cliquez sur "🔧 Auto-Fix"
3. Une branche `auto-fix/YYYYMMDD-HHMMSS` est créée
4. Les corrections sont commitées et pushées
5. Créez une PR pour merger

### Chatbot IA
Posez des questions sur les erreurs :
- "Explique-moi l'erreur MyPy ligne 37"
- "Comment corriger les imports inutilisés ?"
- "Qu'est-ce qu'une annotation de type ?"

### Pipeline CI/CD
À chaque push :
1. ✅ MyPy vérifie les types
2. ✅ Ruff vérifie le style
3. ✅ Rapport HTML généré
4. ✅ Email envoyé si erreurs
5. ✅ Notification Discord

## 📝 Licence

Ce projet est sous licence MIT - Projet pédagogique.

## 👥 Équipe

- **Développeur Principal** - Architecture et CI/CD
- **Collaborateurs** - Fonctionnalités Shopify

## 🙏 Remerciements

- **Groq** pour l'API IA gratuite et ultra-rapide
- **Astral** pour Ruff (outil révolutionnaire)
- **Guido van Rossum** pour MyPy et Python
- **Pallets** pour Flask
- **GitHub** pour GitHub Actions
- **Communauté Python** pour l'écosystème incroyable

---

## 🚀 Prêt à Contribuer ?

1. **Lisez** le [Quick Start](QUICK_START.md) (5 minutes)
2. **Installez** le projet
3. **Testez** le chatbot et Shopify
4. **Créez** votre première branche
5. **Contribuez** !

**Bon développement ! 💻✨**
