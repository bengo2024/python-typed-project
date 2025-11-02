# 🤖 Guide de Configuration du Bot Discord

Ce guide explique comment configurer le chatbot Discord pour expliquer les erreurs CI/CD et déclencher l'auto-fix.

## 📋 Table des Matières

1. [Créer un Webhook Discord](#créer-un-webhook-discord)
2. [Configurer le Secret GitHub](#configurer-le-secret-github)
3. [Tester les Notifications](#tester-les-notifications)
4. [Créer un Bot Discord (Optionnel)](#créer-un-bot-discord-optionnel)
5. [Commandes Disponibles](#commandes-disponibles)

---

## 🔗 Créer un Webhook Discord

### Étape 1 : Créer un Serveur Discord (si nécessaire)

1. Ouvrez Discord
2. Cliquez sur le `+` dans la barre latérale gauche
3. Choisissez "Créer un serveur"
4. Donnez un nom : `CI/CD Notifications`

### Étape 2 : Créer un Canal

1. Clic droit sur votre serveur → "Créer un salon"
2. Nom : `ci-cd-alerts`
3. Type : Salon textuel

### Étape 3 : Créer le Webhook

1. Clic droit sur le canal `ci-cd-alerts` → "Modifier le salon"
2. Allez dans l'onglet **Intégrations**
3. Cliquez sur **Webhooks** → **Nouveau Webhook**
4. Donnez un nom : `CI/CD Bot`
5. Choisissez une icône (optionnel)
6. **Copiez l'URL du Webhook** (elle ressemble à : `https://discord.com/api/webhooks/...`)
7. Cliquez sur **Enregistrer**

---

## 🔐 Configurer le Secret GitHub

### Via l'Interface Web

1. Allez sur : https://github.com/bengo2024/python-typed-project/settings/secrets/actions
2. Cliquez sur **New repository secret**
3. Nom : `DISCORD_WEBHOOK_URL`
4. Valeur : Collez l'URL du webhook Discord
5. Cliquez sur **Add secret**

### Via GitHub CLI

```bash
gh secret set DISCORD_WEBHOOK_URL
# Collez l'URL du webhook quand demandé
```

---

## ✅ Tester les Notifications

Une fois le webhook configuré, faites un commit pour tester :

```bash
# Créer une erreur volontaire
echo "import os" >> main.py  # Import inutilisé

git add .
git commit -m "Test notification Discord"
git push origin main
```

Vous devriez recevoir une notification dans Discord avec :
- 📊 Résumé des erreurs
- 🔍 Détails MyPy, Ruff, Français
- 💡 Actions disponibles
- 🔗 Lien vers le rapport HTML

---

## 🤖 Créer un Bot Discord (Optionnel)

Pour utiliser les commandes interactives (`!expliquer`, `!autofix`), créez un bot Discord :

### Étape 1 : Créer l'Application

1. Allez sur : https://discord.com/developers/applications
2. Cliquez sur **New Application**
3. Nom : `CI/CD Assistant`
4. Acceptez les conditions

### Étape 2 : Créer le Bot

1. Dans le menu de gauche, cliquez sur **Bot**
2. Cliquez sur **Add Bot** → **Yes, do it!**
3. Sous **TOKEN**, cliquez sur **Reset Token** → **Copy**
4. ⚠️ **Gardez ce token secret !**

### Étape 3 : Configurer les Permissions

1. Dans le menu de gauche, cliquez sur **OAuth2** → **URL Generator**
2. Cochez **bot** dans SCOPES
3. Cochez ces permissions dans BOT PERMISSIONS :
   - ✅ Send Messages
   - ✅ Embed Links
   - ✅ Read Message History
   - ✅ Use Slash Commands
4. Copiez l'URL générée en bas

### Étape 4 : Inviter le Bot

1. Collez l'URL dans votre navigateur
2. Sélectionnez votre serveur
3. Cliquez sur **Autoriser**

### Étape 5 : Configurer le Token

Ajoutez le token comme secret GitHub :

```bash
gh secret set DISCORD_BOT_TOKEN
# Collez le token du bot
```

### Étape 6 : Lancer le Bot

Sur votre machine locale ou un serveur :

```bash
# Installer les dépendances
pip install -r requirements-bot.txt

# Créer un fichier .env
echo "DISCORD_BOT_TOKEN=votre_token_ici" > .env
echo "GROQ_API_KEY=votre_clé_groq" >> .env

# Lancer le bot
python discord_bot.py
```

Le bot doit afficher :
```
✅ Bot connecté en tant que CI/CD Assistant
📊 Serveurs: 1
```

---

## 💬 Commandes Disponibles

Une fois le bot en ligne, utilisez ces commandes dans Discord :

### `!aide`
Affiche la liste des commandes disponibles.

```
!aide
```

### `!erreurs`
Affiche les dernières erreurs CI/CD détectées.

```
!erreurs
```

**Exemple de sortie :**
```
📊 Dernières Erreurs CI/CD
Commit: `add fonction without type annotation`
Auteur: bengo2024

🔍 MyPy (Types)
main.py:28: error: Function is missing a type annotation

✨ Ruff (Style)
main.py:1:8: F401 `os` imported but unused
```

### `!expliquer [type]`
Demande à l'IA d'expliquer une erreur en détail.

```
!expliquer mypy
!expliquer ruff
!expliquer french
```

**Exemple de sortie :**
```
💡 Explication MYPY

L'erreur "Function is missing a type annotation" signifie que votre fonction
n'a pas d'annotations de types pour ses paramètres et sa valeur de retour.

❌ Code actuel :
def fonction_sans_types(x, y):
    return x + y

✅ Code corrigé :
def fonction_sans_types(x: int, y: int) -> int:
    return x + y

Les annotations de types permettent à MyPy de vérifier que vous utilisez
les bonnes types de données et d'éviter des bugs.
```

### `!autofix`
Déclenche l'auto-fix et crée une Pull Request avec les corrections.

```
!autofix
```

**Exemple de sortie :**
```
🤖 Déclenchement de l'auto-fix...
📝 Une Pull Request va être créée avec les corrections automatiques.
🔗 Vérifie sur: https://github.com/bengo2024/python-typed-project/pulls
✅ L'auto-fix a été déclenché par le workflow CI/CD!
```

---

## 🎯 Workflow Complet

Voici le workflow typique avec le bot Discord :

1. **Vous faites un commit** avec des erreurs
2. **GitHub Actions** détecte les erreurs
3. **Notification Discord** envoyée automatiquement
4. **Vous tapez** `!erreurs` pour voir les détails
5. **Vous tapez** `!expliquer ruff` pour comprendre l'erreur
6. **L'IA explique** l'erreur en détail avec des exemples
7. **Vous tapez** `!autofix` pour corriger automatiquement
8. **Une Pull Request** est créée avec les corrections
9. **Vous mergez** la PR et tout est corrigé ! 🎉

---

## 🔧 Dépannage

### Le webhook ne fonctionne pas

- ✅ Vérifiez que l'URL du webhook est correcte
- ✅ Vérifiez que le secret `DISCORD_WEBHOOK_URL` est bien configuré
- ✅ Vérifiez les logs du workflow GitHub Actions

### Le bot ne répond pas

- ✅ Vérifiez que le bot est en ligne (voyez-vous son statut "En ligne" ?)
- ✅ Vérifiez que le token est correct
- ✅ Vérifiez que le bot a les permissions nécessaires
- ✅ Vérifiez les logs du bot (`python discord_bot.py`)

### Les commandes ne fonctionnent pas

- ✅ Assurez-vous d'utiliser le préfixe `!` (ex: `!aide`, pas `aide`)
- ✅ Vérifiez que le bot a la permission "Read Message History"
- ✅ Essayez de redémarrer le bot

---

## 📊 Exemple de Notification

Voici à quoi ressemble une notification Discord :

```
⚠️ Erreurs CI/CD Détectées

Commit: `add fonction without type annotation`
Auteur: bengo2024
Total erreurs: 3

🔍 MyPy (2 erreurs)
main.py:28: error: Function is missing a type annotation
main.py:29: error: Function is missing a return type annotation

✨ Ruff (1 erreur)
main.py:1:8: F401 [*] `os` imported but unused

🇫🇷 Français
✅ Message parfait

💡 Actions Disponibles
• Utilise `!erreurs` pour voir les détails
• Utilise `!expliquer [type]` pour une explication IA
• Utilise `!autofix` pour corriger automatiquement
• Vérifie le rapport HTML
```

---

## 🎉 Félicitations !

Votre bot Discord est maintenant configuré ! Vous avez :

- ✅ Notifications automatiques des erreurs CI/CD
- ✅ Explications IA des erreurs
- ✅ Auto-fix en une commande
- ✅ Rapport HTML détaillé

**Votre système CI/CD est maintenant ultra-professionnel ! 🚀**

---

## 📚 Ressources

- [Documentation Discord.py](https://discordpy.readthedocs.io/)
- [Discord Developer Portal](https://discord.com/developers/applications)
- [Groq API Documentation](https://console.groq.com/docs)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

