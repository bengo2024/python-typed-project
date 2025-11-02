# 🛍️ Shopify - Application E-Commerce

Application e-commerce complète en Python typé, intégrée avec le système CI/CD.

## 🚀 Fonctionnalités

### Pour les Clients
- ✅ Catalogue de produits avec recherche et filtres par catégorie
- ✅ Page détail produit avec images et descriptions
- ✅ Panier d'achat avec gestion des quantités
- ✅ Système de commande avec adresse de livraison
- ✅ Historique des commandes
- ✅ Authentification utilisateur (inscription/connexion)

### Pour les Administrateurs
- ✅ Dashboard d'administration
- ✅ Ajout de nouveaux produits
- ✅ Gestion du catalogue

### Intégration CI/CD
- ✅ Vérification MyPy (typage statique)
- ✅ Vérification Ruff (linting et formatage)
- ✅ Notifications email en cas d'erreur
- ✅ Chatbot IA pour expliquer les erreurs
- ✅ Auto-Fix automatique des erreurs corrigeables

## 📦 Installation

```bash
# Installer les dépendances
pip install -r requirements.txt

# Initialiser la base de données avec des données de démonstration
python -m shopify.init_data

# Lancer l'application
python -m shopify.app
```

L'application sera accessible sur **http://127.0.0.1:5001**

## 👤 Comptes de Test

### Administrateur
- **Email:** admin@shopify.com
- **Mot de passe:** admin123

### Client
- **Email:** client@example.com
- **Mot de passe:** client123

## 🏗️ Architecture

```
shopify/
├── __init__.py          # Package initialization
├── models.py            # Modèles de données (Product, User, Order, etc.)
├── database.py          # Gestion de la base de données SQLite
├── app.py               # Application Flask avec toutes les routes
├── init_data.py         # Script d'initialisation avec données de démo
└── README.md            # Documentation

templates/shopify/
├── base.html            # Template de base avec navigation
├── index.html           # Page d'accueil
├── products.html        # Catalogue de produits
├── product_detail.html  # Détail d'un produit
├── cart.html            # Panier
├── checkout.html        # Page de paiement
├── orders.html          # Historique des commandes
├── login.html           # Connexion
├── register.html        # Inscription
└── admin/
    └── dashboard.html   # Dashboard administrateur

static/
├── css/
│   └── shopify.css      # Styles CSS modernes
└── js/
    └── shopify.js       # JavaScript pour interactions
```

## 🗄️ Base de Données

SQLite avec les tables suivantes :
- **products** - Produits du catalogue
- **users** - Utilisateurs (clients et admins)
- **orders** - Commandes
- **order_items** - Articles des commandes

## 🎨 Design

- Design moderne avec dégradés et animations
- Interface responsive (mobile-friendly)
- Icônes Font Awesome
- Palette de couleurs cohérente avec variables CSS
- Messages flash avec auto-dismiss

## 🔒 Sécurité

- Mots de passe hashés avec SHA-256
- Sessions Flask pour l'authentification
- Protection des routes admin
- Validation des formulaires

## 🧪 Tests

```bash
# Vérifier le typage
python -m mypy shopify/

# Vérifier le linting
python -m ruff check shopify/

# Formater le code
python -m ruff format shopify/
```

## 📝 Rollback vers Version Stable

Pour revenir à la version stable avant Shopify :

```bash
git checkout v1.0-stable
```

## 🔗 Intégration CI/CD

Chaque commit déclenche automatiquement :
1. ✅ Vérification MyPy et Ruff
2. ✅ Génération de rapports HTML
3. ✅ Envoi d'email avec suggestions IA (si erreurs)
4. ✅ Chatbot disponible pour expliquer les erreurs
5. ✅ Auto-Fix disponible pour corriger automatiquement

## 📊 Badges CI/CD

![MyPy](https://img.shields.io/badge/MyPy-Passing-success)
![Ruff](https://img.shields.io/badge/Ruff-Passing-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)

## 🤝 Contribution

Ce projet est un projet académique démontrant l'intégration complète d'une application e-commerce avec un système CI/CD avancé.

