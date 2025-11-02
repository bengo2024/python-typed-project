# 🤖 Guide du Chatbot Web Interactif

Ce guide explique comment utiliser l'interface web du chatbot CI/CD pour discuter avec l'IA et corriger vos erreurs.

---

## 🚀 Démarrage Rapide

### 1. Installer les dépendances

```bash
pip install flask openai python-dotenv
```

### 2. Configurer la clé API Groq

Créez un fichier `.env` à la racine du projet :

```bash
GROQ_API_KEY=votre_clé_groq_ici
```

### 3. Lancer le chatbot

```bash
python chatbot_app.py
```

### 4. Ouvrir l'interface

Ouvrez votre navigateur et allez sur :
```
http://localhost:5000
```

---

## 💬 Utilisation du Chatbot

### Interface

L'interface est divisée en 3 zones :

#### 1️⃣ **Panneau de gauche : Erreurs détectées**
- 📊 Résumé des erreurs (nombre total)
- 🔍 Détails MyPy (erreurs de typage)
- ✨ Détails Ruff (erreurs de style)
- 🔧 Bouton Auto-Fix

#### 2️⃣ **Zone centrale : Conversation**
- 💬 Historique des messages
- 🤖 Réponses de l'IA
- 👤 Vos questions

#### 3️⃣ **Zone de saisie : Input**
- ⌨️ Tapez votre question
- 📤 Bouton Envoyer
- 💡 Suggestions de questions

---

## 🎯 Exemples de Conversations

### Exemple 1 : Découvrir les erreurs

**Vous :** Bonjour, quelles sont les erreurs actuelles ?

**Bot :** 👋 Bonjour ! J'ai détecté 4 erreurs dans votre code :
- 3 erreurs de style (Ruff) : imports inutilisés
- 1 erreur de typage (MyPy) : fonction sans annotations

Voulez-vous que je vous explique une erreur en particulier ?

---

### Exemple 2 : Comprendre une erreur MyPy

**Vous :** Explique-moi l'erreur MyPy en détail

**Bot :** 💡 L'erreur MyPy concerne la fonction `test_discord_notification` à la ligne 39.

**Problème :**
La fonction n'a pas d'annotations de types pour ses paramètres et sa valeur de retour.

**❌ Code actuel :**
```python
def test_discord_notification(x, y):
    return x * y
```

**✅ Code corrigé :**
```python
def test_discord_notification(x: int, y: int) -> int:
    return x * y
```

**Pourquoi c'est important ?**
Les annotations de types permettent à MyPy de :
- Détecter les erreurs avant l'exécution
- Améliorer l'autocomplétion dans votre IDE
- Documenter le code automatiquement

Voulez-vous que je corrige automatiquement les autres erreurs ?

---

### Exemple 3 : Comprendre une erreur Ruff

**Vous :** Pourquoi Ruff détecte des imports inutilisés ?

**Bot :** ✨ Ruff a détecté 3 imports qui ne sont jamais utilisés dans votre code :

1. `import os` (ligne 1)
2. `import sys` (ligne 2)
3. `import json` (ligne 3)

**Pourquoi c'est un problème ?**
- 📦 Augmente la taille du fichier
- ⚡ Ralentit le chargement du module
- 🧹 Rend le code moins propre
- 🐛 Peut masquer des erreurs

**Solution :**
Supprimez ces imports ou utilisez-les dans votre code.

Je peux les supprimer automatiquement avec le bouton "Auto-Fix" ! 🔧

---

### Exemple 4 : Demander des conseils

**Vous :** Comment éviter ces erreurs à l'avenir ?

**Bot :** 🎓 Excellente question ! Voici mes conseils :

**Pour éviter les imports inutilisés :**
- Utilisez un IDE avec auto-import (VS Code, PyCharm)
- Configurez Ruff pour vérifier automatiquement
- Supprimez les imports dès qu'ils ne sont plus utilisés

**Pour éviter les erreurs de typage :**
- Ajoutez toujours des annotations de types
- Utilisez MyPy en mode strict
- Configurez votre IDE pour afficher les erreurs MyPy

**Astuce :**
Activez le formatage automatique dans votre IDE pour que Ruff corrige les erreurs à chaque sauvegarde !

---

### Exemple 5 : Déclencher l'auto-fix

**Vous :** Corrige toutes les erreurs automatiquement

**Bot :** 🔧 Pour corriger automatiquement les erreurs Ruff, cliquez sur le bouton **"Auto-Fix"** dans le panneau de gauche.

⚠️ **Note :** L'auto-fix ne peut corriger que les erreurs Ruff (style). Les erreurs MyPy (typage) nécessitent une correction manuelle car elles dépendent de la logique de votre code.

Voulez-vous que je vous guide pour corriger manuellement l'erreur MyPy ?

---

## 🔧 Fonctionnalités

### 1. Actualiser les erreurs

Cliquez sur **🔄 Actualiser** pour recharger les erreurs après avoir modifié le code.

### 2. Nouvelle conversation

Cliquez sur **🗑️ Nouvelle conversation** pour réinitialiser l'historique et recommencer.

### 3. Auto-Fix

Cliquez sur **🔧 Auto-Fix** pour :
1. Créer une nouvelle branche `auto-fix/YYYYMMDD-HHMMSS`
2. Appliquer les corrections Ruff automatiques
3. Committer les changements
4. Pousser la branche sur GitHub

Ensuite, vous pouvez créer une Pull Request manuellement.

---

## 💡 Questions Suggérées

Voici des exemples de questions que vous pouvez poser :

### Questions générales
- "Quelles sont les erreurs actuelles ?"
- "Combien d'erreurs ai-je ?"
- "Tout est-il correct ?"

### Questions sur MyPy
- "Explique-moi l'erreur MyPy"
- "Qu'est-ce qu'une annotation de type ?"
- "Comment corriger l'erreur de typage ?"
- "Pourquoi MyPy est important ?"

### Questions sur Ruff
- "Explique-moi l'erreur Ruff"
- "Pourquoi les imports inutilisés sont un problème ?"
- "Comment formater mon code ?"
- "Qu'est-ce que le linting ?"

### Questions sur les corrections
- "Comment corriger ces erreurs ?"
- "Peux-tu me montrer le code corrigé ?"
- "Quelles erreurs peuvent être corrigées automatiquement ?"
- "Comment éviter ces erreurs à l'avenir ?"

### Questions pédagogiques
- "C'est quoi MyPy ?"
- "C'est quoi Ruff ?"
- "Pourquoi utiliser des types en Python ?"
- "Quelles sont les bonnes pratiques Python ?"

---

## 🎨 Raccourcis Clavier

- **Entrée** : Envoyer le message
- **Shift + Entrée** : Nouvelle ligne dans le message
- **Ctrl + R** : Actualiser les erreurs (si implémenté)

---

## 🔍 Dépannage

### Le chatbot ne répond pas

1. Vérifiez que `GROQ_API_KEY` est défini dans `.env`
2. Vérifiez que Flask est bien démarré
3. Regardez les logs dans le terminal

### Les erreurs ne s'affichent pas

1. Cliquez sur **🔄 Actualiser**
2. Vérifiez que MyPy et Ruff sont installés :
   ```bash
   pip install mypy ruff
   ```

### L'auto-fix ne fonctionne pas

1. Vérifiez que `auto_fix.py` existe
2. Vérifiez que vous êtes sur la branche `main`
3. Vérifiez que vous avez les droits Git

---

## 🚀 Fonctionnalités Avancées

### Personnaliser les réponses de l'IA

Modifiez le `system_prompt` dans `chatbot_app.py` pour changer le comportement du bot.

### Ajouter des commandes

Vous pouvez ajouter des commandes spéciales dans le code JavaScript :
- `/errors` - Afficher les erreurs
- `/fix` - Déclencher l'auto-fix
- `/help` - Afficher l'aide

### Intégration avec GitHub

Le chatbot peut créer des branches et pousser du code. Pour créer automatiquement des Pull Requests, ajoutez le GitHub CLI :

```bash
gh pr create --title "Auto-Fix" --body "Corrections automatiques"
```

---

## 📊 Comparaison avec Discord

| Fonctionnalité | Chatbot Web | Discord Bot |
|----------------|-------------|-------------|
| Interface graphique | ✅ Moderne | ❌ Texte uniquement |
| Conversation fluide | ✅ Oui | ⚠️ Limité |
| Affichage des erreurs | ✅ Panneau dédié | ❌ Dans le chat |
| Auto-Fix | ✅ Bouton dédié | ⚠️ Commande |
| Accessibilité | ✅ Navigateur | ⚠️ Nécessite Discord |
| Temps réel | ✅ Instantané | ⚠️ Dépend du webhook |

**Recommandation :** Utilisez le chatbot web pour une meilleure expérience utilisateur !

---

## 🎯 Conclusion

Le chatbot web offre une **interface moderne et intuitive** pour :
- 💬 Discuter avec l'IA sur vos erreurs
- 📊 Visualiser les erreurs en temps réel
- 🔧 Corriger automatiquement certaines erreurs
- 🎓 Apprendre les bonnes pratiques Python

**C'est l'outil parfait pour impressionner votre prof ! 🌟**

---

## 📚 Ressources

- [Documentation Flask](https://flask.palletsprojects.com/)
- [Documentation Groq](https://console.groq.com/docs)
- [Documentation MyPy](https://mypy.readthedocs.io/)
- [Documentation Ruff](https://docs.astral.sh/ruff/)

