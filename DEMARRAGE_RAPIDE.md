# 🚀 Démarrage Rapide du Chatbot

## ⚡ En 3 Étapes

### 1️⃣ Créer le fichier `.env`

Créez un fichier nommé `.env` à la racine du projet avec ce contenu :

```
GROQ_API_KEY=gsk_votre_clé_groq_ici
```

**🔑 Où trouver votre clé Groq ?**
- Allez sur : https://console.groq.com/keys
- Connectez-vous (ou créez un compte gratuit)
- Cliquez sur "Create API Key"
- Copiez la clé (elle commence par `gsk_`)

---

### 2️⃣ Lancer le chatbot

**Option A : Double-cliquez sur le fichier**
```
start_chatbot.bat
```

**Option B : Dans le terminal**
```bash
python chatbot_app.py
```

---

### 3️⃣ Ouvrir le navigateur

Allez sur :
```
http://localhost:5000
```

---

## 🎯 C'est Tout !

Vous devriez voir l'interface du chatbot avec :
- 🤖 Message de bienvenue
- 📊 Panneau des erreurs
- 💬 Zone de conversation

---

## ❌ Problèmes Courants

### "GROQ_API_KEY n'est pas définie"

**Solution :** Créez le fichier `.env` avec votre clé Groq (voir étape 1)

### "Localhost refuse la connexion"

**Solution :** Le serveur n'est pas démarré. Lancez `python chatbot_app.py`

### "Module 'flask' not found"

**Solution :** Installez Flask avec `pip install flask python-dotenv`

---

## 📝 Exemple de fichier .env

Votre fichier `.env` doit ressembler à ça :

```
GROQ_API_KEY=gsk_1234567890abcdefghijklmnopqrstuvwxyz
```

⚠️ **Important :** Remplacez `gsk_1234...` par votre vraie clé !

---

## 🎉 Prêt !

Une fois le chatbot lancé, vous pouvez :
- Poser des questions sur vos erreurs
- Demander des explications
- Cliquer sur Auto-Fix pour corriger automatiquement

**Amusez-vous bien ! 🚀**

