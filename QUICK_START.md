# 🚀 Quick Start - Démarrage Rapide (5 minutes)

## ⚡ Installation Express

### 1️⃣ Cloner le Projet (30 secondes)

```bash
git clone https://github.com/bengo2024/python-typed-project.git
cd python-typed-project
```

### 2️⃣ Installer Python 3.10+ (si nécessaire)

**Vérifier votre version :**
```bash
python --version
# Doit afficher : Python 3.10.x ou supérieur
```

**Si version < 3.10, télécharger :**
- Windows : https://www.python.org/downloads/
- Linux : `sudo apt install python3.10`
- Mac : `brew install python@3.10`

### 3️⃣ Créer l'Environnement Virtuel (30 secondes)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

**Vous devriez voir `(venv)` devant votre prompt :**
```bash
(venv) C:\Users\HP\python-typed-project>
```

### 4️⃣ Installer les Dépendances (1 minute)

```bash
pip install -r requirements.txt
```

**Sortie attendue :**
```
Successfully installed mypy-1.11.1 ruff-0.6.0 Flask-3.0.0 ...
```

### 5️⃣ Configurer les Variables d'Environnement (2 minutes)

**Créer le fichier `.env` :**

```bash
# Windows
copy .env.example .env
notepad .env

# Linux/Mac
cp .env.example .env
nano .env
```

**Contenu du fichier `.env` :**
```bash
# API Groq (OBLIGATOIRE pour le chatbot)
GROQ_API_KEY=gsk_votre_clé_ici

# Email (OPTIONNEL - pour les notifications)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=votre_email@gmail.com
EMAIL_PASSWORD=votre_mot_de_passe_application

# Discord (OPTIONNEL - pour les notifications)
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
```

**🔑 Obtenir une clé Groq (GRATUIT) :**
1. Allez sur https://console.groq.com/keys
2. Créez un compte (email + mot de passe)
3. Cliquez sur "Create API Key"
4. Copiez la clé (commence par `gsk_`)
5. Collez dans `.env` : `GROQ_API_KEY=gsk_...`

### 6️⃣ Vérifier l'Installation (30 secondes)

```bash
# Vérifier MyPy
python -m mypy --version
# Sortie : mypy 1.11.1

# Vérifier Ruff
python -m ruff --version
# Sortie : ruff 0.6.0

# Vérifier que tout fonctionne
python -m mypy . && python -m ruff check .
# Sortie : Success: no issues found in X source files
```

---

## 🎯 Tester les Applications

### Chatbot CI/CD

```bash
# Démarrer le chatbot
python chatbot_app.py
```

**Ouvrir dans le navigateur :** http://localhost:5000

**Tester :**
1. Cliquez sur "🔄 Actualiser" → Voir les erreurs
2. Tapez "Bonjour" dans le chat → Réponse de l'IA
3. Cliquez sur "🔧 Auto-Fix" → Correction automatique

### Application Shopify

```bash
# Démarrer Shopify
python -m shopify.app

# OU (Windows)
start_shopify.bat
```

**Ouvrir dans le navigateur :** http://localhost:5001

**Tester :**
1. Parcourir les produits
2. Se connecter : `alice@example.com` / `password123`
3. Ajouter au panier
4. Passer commande

**Compte Admin :**
- Email : `admin@shopify.com`
- Mot de passe : `admin123`

---

## 🌿 Créer Votre Première Branche

### 1️⃣ Créer une Branche

```bash
# Format : feature/votre-nom-description
git checkout -b feature/alice-ajout-produit

# Exemples :
# git checkout -b feature/bob-page-contact
# git checkout -b fix/charlie-bug-panier
```

### 2️⃣ Faire une Modification Simple

**Exemple : Ajouter un produit dans Shopify**

Ouvrez `shopify/init_data.py` et ajoutez :

```python
Product(
    id=21,
    name="Votre Produit",
    description="Description de votre produit",
    price=99.99,
    stock=50,
    category="Électronique",
    image_url="https://via.placeholder.com/300x300?text=Votre+Produit",
    rating=4.5,
    reviews_count=10
),
```

### 3️⃣ Vérifier AVANT de Commit

```bash
# Vérifier les types
python -m mypy .

# Vérifier le style
python -m ruff check .

# Auto-corriger Ruff
python -m ruff check --fix .

# Formater le code
python -m ruff format .
```

### 4️⃣ Commit et Push

```bash
# Ajouter les fichiers
git add .

# Commit avec message clair
git commit -m "✨ Ajout d'un nouveau produit dans le catalogue"

# Push vers votre branche
git push origin feature/alice-ajout-produit
```

### 5️⃣ Créer une Pull Request

1. Allez sur GitHub : https://github.com/bengo2024/python-typed-project
2. Cliquez sur **"Compare & pull request"**
3. Remplissez :
   - **Titre** : `✨ Ajout d'un nouveau produit`
   - **Description** :
     ```markdown
     ## Changements
     - Ajout d'un produit "Votre Produit" dans le catalogue
     
     ## Tests
     - ✅ MyPy passe
     - ✅ Ruff passe
     - ✅ Produit visible dans Shopify
     ```
4. Cliquez sur **"Create pull request"**

---

## 🎓 Commandes Essentielles

### Vérification du Code

```bash
# Vérifier tout
python -m mypy . && python -m ruff check .

# Vérifier + Auto-corriger
python -m mypy . && python -m ruff check --fix .

# Formater le code
python -m ruff format .
```

### Git

```bash
# Voir l'état
git status

# Voir les branches
git branch

# Changer de branche
git checkout main

# Mettre à jour depuis main
git pull origin main

# Voir l'historique
git log --oneline -10
```

### Applications

```bash
# Chatbot
python chatbot_app.py

# Shopify
python -m shopify.app

# Initialiser la base de données Shopify
python -m shopify.init_data
```

---

## 🆘 Problèmes Courants

### ❌ "Module not found"

```bash
# Solution : Réinstaller
pip install -r requirements.txt
```

### ❌ "GROQ_API_KEY not found"

```bash
# Solution : Vérifier .env
cat .env  # Linux/Mac
type .env  # Windows

# Doit contenir :
GROQ_API_KEY=gsk_...
```

### ❌ "Port 5000 already in use"

```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### ❌ Erreurs MyPy incompréhensibles

```bash
# Solution : Utiliser le chatbot !
python chatbot_app.py
# Puis posez votre question
```

---

## 📚 Documentation Complète

- **Guide Complet** : `GUIDE_COLLABORATEURS.md`
- **Architecture Technique** : `ARCHITECTURE_TECHNIQUE.md`
- **Guide Shopify** : `shopify/README.md`

---

## ✅ Checklist de Démarrage

Avant de commencer à coder, vérifiez :

- [ ] Python 3.10+ installé (`python --version`)
- [ ] Environnement virtuel activé (`(venv)` visible)
- [ ] Dépendances installées (`pip list`)
- [ ] Fichier `.env` créé avec `GROQ_API_KEY`
- [ ] MyPy fonctionne (`python -m mypy --version`)
- [ ] Ruff fonctionne (`python -m ruff --version`)
- [ ] Chatbot testé (http://localhost:5000)
- [ ] Shopify testé (http://localhost:5001)
- [ ] Branche créée (`git branch`)
- [ ] Première modification faite
- [ ] Vérifications passées (`mypy` + `ruff`)
- [ ] Premier commit fait
- [ ] Première PR créée

---

## 🎉 Vous êtes Prêt !

**Prochaines étapes :**
1. Lisez `GUIDE_COLLABORATEURS.md` pour comprendre le projet
2. Explorez le code dans `shopify/` et `chatbot_app.py`
3. Faites votre première contribution
4. Demandez de l'aide au chatbot si besoin

**Bon développement ! 🚀**

---

## 💡 Astuces Pro

### Alias Git Utiles

```bash
# Ajouter dans ~/.gitconfig ou ~/.bashrc

# Vérification rapide
alias check="python -m mypy . && python -m ruff check ."

# Vérification + Auto-fix
alias fix="python -m ruff check --fix . && python -m ruff format ."

# Status court
alias gs="git status -s"

# Log joli
alias gl="git log --oneline --graph --decorate -10"
```

### VS Code Extensions Recommandées

1. **Python** (Microsoft) - Support Python
2. **Pylance** (Microsoft) - IntelliSense
3. **Ruff** (Astral) - Linting en temps réel
4. **MyPy Type Checker** - Vérification des types
5. **GitLens** - Git amélioré

### Configuration VS Code

Créez `.vscode/settings.json` :

```json
{
  "python.linting.enabled": true,
  "python.linting.mypyEnabled": true,
  "python.formatting.provider": "none",
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": true,
      "source.organizeImports": true
    }
  },
  "ruff.lint.run": "onSave"
}
```

---

## 📞 Besoin d'Aide ?

1. **Chatbot** - Posez vos questions sur http://localhost:5000
2. **Documentation** - Lisez `GUIDE_COLLABORATEURS.md`
3. **GitHub Issues** - Créez une issue sur le repo
4. **Discord** - Rejoignez le canal du projet

**Bonne chance ! 🍀**

