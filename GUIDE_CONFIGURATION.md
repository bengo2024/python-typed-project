# 🚀 Guide de Configuration CI/CD - Projet Python Typé

## 📋 Table des matières
1. [Prérequis](#prérequis)
2. [Configuration des Secrets GitHub](#configuration-des-secrets-github)
3. [Configuration de l'Email Gmail](#configuration-de-lemail-gmail)
4. [Configuration de l'API OpenAI](#configuration-de-lapi-openai)
5. [Utilisation de GitHub CLI](#utilisation-de-github-cli)
6. [Tester en Local](#tester-en-local)
7. [Workflow de Développement](#workflow-de-développement)

---

## 🔧 Prérequis

- **Python 3.10+** installé
- **Git** installé et configuré
- **GitHub CLI** (`gh`) installé
- Un compte **GitHub**
- Un compte **Gmail** (pour l'envoi d'emails)
- Une clé **OpenAI API** (GPT-3.5-turbo)

---

## 🔐 Configuration des Secrets GitHub

Les secrets GitHub permettent de stocker des informations sensibles (clés API, mots de passe) de manière sécurisée.

### Méthode 1 : Via l'interface web GitHub

1. Allez sur votre dépôt GitHub
2. Cliquez sur **Settings** (Paramètres)
3. Dans le menu de gauche, cliquez sur **Secrets and variables** → **Actions**
4. Cliquez sur **New repository secret**
5. Ajoutez les secrets suivants :

| Nom du Secret | Description | Exemple |
|---------------|-------------|---------|
| `GROQ_API_KEY` | Clé API Groq (gratuit) | `gsk_...` |
| `EMAIL_HOST` | Serveur SMTP Gmail | `smtp.gmail.com` |
| `EMAIL_PORT` | Port SMTP | `587` |
| `EMAIL_USER` | Votre adresse Gmail | `votre.email@gmail.com` |
| `EMAIL_PASSWORD` | Mot de passe d'application Gmail | `abcd efgh ijkl mnop` |

### Méthode 2 : Via GitHub CLI

```bash
# Se connecter à GitHub
gh auth login

# Ajouter les secrets
gh secret set GROQ_API_KEY
# Collez votre clé API Groq quand demandé

gh secret set EMAIL_HOST -b "smtp.gmail.com"
gh secret set EMAIL_PORT -b "587"
gh secret set EMAIL_USER -b "votre.email@gmail.com"
gh secret set EMAIL_PASSWORD
# Collez votre mot de passe d'application Gmail

# Vérifier les secrets
gh secret list
```

---

## 📧 Configuration de l'Email Gmail

Pour que le workflow puisse envoyer des emails, vous devez créer un **mot de passe d'application** Gmail.

### Étapes :

1. **Activer la validation en deux étapes** sur votre compte Google :
   - Allez sur https://myaccount.google.com/security
   - Activez la "Validation en deux étapes"

2. **Créer un mot de passe d'application** :
   - Allez sur https://myaccount.google.com/apppasswords
   - Sélectionnez "Autre (nom personnalisé)"
   - Entrez "GitHub Actions CI/CD"
   - Cliquez sur "Générer"
   - **Copiez le mot de passe de 16 caractères** (format : `abcd efgh ijkl mnop`)
   - Utilisez ce mot de passe pour le secret `EMAIL_PASSWORD`

⚠️ **Important** : N'utilisez JAMAIS votre mot de passe Gmail principal !

---

## 🤖 Configuration de l'API Groq (Gratuit !)

### Obtenir une clé API Groq :

1. Allez sur https://console.groq.com/
2. Créez un compte (gratuit, pas de carte bancaire requise)
3. Cliquez sur **API Keys** dans le menu de gauche
4. Cliquez sur **Create API Key**
5. Donnez un nom à la clé (ex: "GitHub Actions CI/CD")
6. **Copiez la clé** (elle commence par `gsk_...`)
7. Ajoutez-la comme secret GitHub `GROQ_API_KEY`

### Pourquoi Groq ?

- ✅ **100% gratuit** (pas de carte bancaire)
- ✅ **Quota généreux** (14,400 requêtes/jour)
- ✅ **Très rapide** (plus rapide qu'OpenAI)
- ✅ **Modèle puissant** (Llama 3.1 70B)
- ✅ **Compatible OpenAI** (même API)

### Vérifier que la clé fonctionne :

```bash
# Créer un fichier .env local (NE PAS COMMITER)
echo "GROQ_API_KEY=gsk_..." > .env

# Tester la clé
python test_groq.py
```

---

## 💻 Utilisation de GitHub CLI

### Installation de GitHub CLI :

**Windows** :
```bash
winget install --id GitHub.cli
```

**macOS** :
```bash
brew install gh
```

**Linux** :
```bash
sudo apt install gh
```

### Commandes utiles :

```bash
# Se connecter
gh auth login

# Voir les secrets
gh secret list

# Ajouter un secret
gh secret set NOM_SECRET

# Supprimer un secret
gh secret remove NOM_SECRET

# Voir les workflows
gh workflow list

# Voir les runs d'un workflow
gh run list

# Voir les détails d'un run
gh run view <run-id>

# Relancer un workflow
gh run rerun <run-id>
```

---

## 🧪 Tester en Local

Avant de pusher, testez toujours votre code localement :

### 1. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 2. Vérifier les types avec MyPy

```bash
python -m mypy main.py
```

✅ Résultat attendu : `Success: no issues found in 1 source file`

### 3. Vérifier le style avec Ruff

```bash
# Vérifier
python -m ruff check .

# Corriger automatiquement
python -m ruff check --fix .
```

✅ Résultat attendu : `All checks passed!`

### 4. Tester l'API OpenAI

```bash
python test_openai.py
```

---

## 🔄 Workflow de Développement

### Workflow recommandé avec branches :

```bash
# 1. Créer une branche feature
git checkout -b feature/ma-nouvelle-fonctionnalite

# 2. Faire vos modifications
# ... éditer les fichiers ...

# 3. Tester localement
python -m mypy main.py
python -m ruff check .

# 4. Commiter avec un message en français parfait
git add .
git commit -m "Ajout de la fonctionnalité de gestion des utilisateurs"

# 5. Pusher la branche
git push origin feature/ma-nouvelle-fonctionnalite

# 6. Créer une Pull Request
gh pr create --title "Ajout gestion utilisateurs" --body "Description détaillée"

# 7. Le workflow GitHub Actions se lance automatiquement
# Vous recevrez un email selon le résultat

# 8. Si tout est OK, merger la PR
gh pr merge --merge
```

### Bonnes pratiques pour les messages de commit :

✅ **BON** :
- "Ajout de la fonctionnalité de connexion utilisateur"
- "Correction du bug d'affichage des produits"
- "Amélioration des performances de la base de données"

❌ **MAUVAIS** :
- "fix bug" (pas en français)
- "update" (pas descriptif)
- "Ajout fonctionalité" (faute d'orthographe)

---

## 📊 Comprendre les Résultats du Workflow

### Workflow réussi ✅

Vous recevrez un email de **félicitations** :
- Sujet : "Félicitations pour ton commit parfait !"
- Contenu : Message personnalisé généré par l'IA

### Workflow échoué ❌

Vous recevrez un email de **correction** :
- Sujet : "⚠️ Corrections nécessaires pour ton commit"
- Contenu :
  - Message personnalisé et encourageant
  - Rapport détaillé des erreurs (MyPy, Ruff, Français)
  - Conseils pour corriger

---

## 🎯 Objectif Final : 20/20

Pour obtenir la note maximale, assurez-vous que :

- ✅ Tous les secrets GitHub sont configurés
- ✅ MyPy passe sans erreur (toutes les fonctions sont typées)
- ✅ Ruff passe sans erreur (pas d'imports inutilisés, lignes ≤ 88 caractères)
- ✅ Les messages de commit sont en français parfait
- ✅ Les emails sont personnalisés et adaptés à la culture du développeur
- ✅ Le workflow fonctionne sur chaque push/PR sur `main`
- ✅ La collaboration se fait via branches et Pull Requests

---

## 🆘 Dépannage

### Problème : Le workflow échoue avec "Secret not found"

**Solution** : Vérifiez que tous les secrets sont bien configurés :
```bash
gh secret list
```

### Problème : L'email n'est pas envoyé

**Solution** : Vérifiez que :
1. Vous avez activé la validation en deux étapes sur Gmail
2. Vous utilisez un mot de passe d'application (pas votre mot de passe Gmail)
3. Le secret `EMAIL_PASSWORD` est bien configuré

### Problème : MyPy trouve des erreurs

**Solution** : Assurez-vous que toutes vos fonctions ont des annotations de type :
```python
# ❌ MAUVAIS
def ma_fonction(x, y):
    return x + y

# ✅ BON
def ma_fonction(x: int, y: int) -> int:
    return x + y
```

### Problème : Ruff trouve des imports inutilisés

**Solution** : Supprimez les imports non utilisés ou utilisez `--fix` :
```bash
python -m ruff check --fix .
```

---

## 📚 Ressources

- [Documentation GitHub Actions](https://docs.github.com/en/actions)
- [Documentation MyPy](https://mypy.readthedocs.io/)
- [Documentation Ruff](https://docs.astral.sh/ruff/)
- [Documentation OpenAI API](https://platform.openai.com/docs/)
- [Documentation GitHub CLI](https://cli.github.com/manual/)

---

**Bon courage pour votre projet ! 🚀**

