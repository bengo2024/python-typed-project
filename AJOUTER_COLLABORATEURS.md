# 👥 Guide pour Ajouter des Collaborateurs au Projet

## 🎯 Objectif

Ce guide explique comment ajouter les membres de votre groupe au repository GitHub pour qu'ils puissent contribuer au projet.

---

## 📋 Prérequis

### Pour Vous (Propriétaire du Repo)
- ✅ Compte GitHub avec le repository `python-typed-project`
- ✅ Droits d'administration sur le repository

### Pour les Collaborateurs
- ✅ Compte GitHub (gratuit)
- ✅ Git installé sur leur machine
- ✅ Python 3.10+ installé

---

## 🚀 Étape 1 : Ajouter des Collaborateurs sur GitHub

### Méthode 1 : Via l'Interface Web (Recommandé)

1. **Allez sur votre repository GitHub**
   ```
   https://github.com/bengo2024/python-typed-project
   ```

2. **Cliquez sur "Settings" (Paramètres)**
   - En haut à droite du repository
   - Icône d'engrenage ⚙️

3. **Dans le menu de gauche, cliquez sur "Collaborators"**
   - Ou "Collaborators and teams"

4. **Cliquez sur "Add people" (Ajouter des personnes)**
   - Bouton vert

5. **Entrez le nom d'utilisateur GitHub ou l'email**
   - Exemple : `alice-dev`, `bob-coder`, etc.
   - Ou leur email associé à GitHub

6. **Sélectionnez le niveau d'accès**
   - **Write** (Écriture) - Recommandé pour les collaborateurs
     - Peuvent créer des branches
     - Peuvent faire des commits
     - Peuvent créer des Pull Requests
     - **NE PEUVENT PAS** supprimer le repository
   
   - **Admin** (Administration) - Seulement pour les co-responsables
     - Tous les droits
     - Peuvent modifier les paramètres
     - Peuvent supprimer le repository

7. **Cliquez sur "Add [username] to this repository"**

8. **Le collaborateur reçoit un email d'invitation**
   - Il doit accepter l'invitation
   - Lien dans l'email ou sur https://github.com/notifications

### Méthode 2 : Via GitHub CLI (Avancé)

```bash
# Installer GitHub CLI si nécessaire
# Windows : winget install GitHub.cli
# Mac : brew install gh
# Linux : voir https://cli.github.com/

# Se connecter
gh auth login

# Ajouter un collaborateur
gh api repos/bengo2024/python-typed-project/collaborators/USERNAME -X PUT

# Exemple
gh api repos/bengo2024/python-typed-project/collaborators/alice-dev -X PUT
```

---

## 📧 Étape 2 : Envoyer les Instructions aux Collaborateurs

### Email Type à Envoyer

```
Objet : Invitation au Projet Python CI/CD - Action Requise

Bonjour [Nom],

Tu as été ajouté(e) au projet "Python Typed Project" sur GitHub !

🔗 Repository : https://github.com/bengo2024/python-typed-project

📋 ACTIONS À FAIRE :

1. Accepte l'invitation GitHub
   - Vérifie tes emails
   - Ou va sur : https://github.com/notifications
   - Clique sur "Accept invitation"

2. Clone le projet
   git clone https://github.com/bengo2024/python-typed-project.git
   cd python-typed-project

3. Suis le guide de démarrage rapide
   - Ouvre le fichier QUICK_START.md
   - Ou consulte : https://github.com/bengo2024/python-typed-project/blob/main/QUICK_START.md

4. Lis la documentation complète
   - GUIDE_COLLABORATEURS.md - Guide complet du projet
   - ARCHITECTURE_TECHNIQUE.md - Détails techniques

📚 RESSOURCES IMPORTANTES :

- Quick Start (5 min) : QUICK_START.md
- Guide Complet : GUIDE_COLLABORATEURS.md
- Architecture : ARCHITECTURE_TECHNIQUE.md

🎯 PREMIÈRE TÂCHE :

1. Installe le projet (voir QUICK_START.md)
2. Teste le chatbot : python chatbot_app.py
3. Teste Shopify : python -m shopify.app
4. Crée ta première branche : git checkout -b feature/ton-nom-test
5. Fais une petite modification
6. Crée ta première Pull Request

💬 BESOIN D'AIDE ?

- Utilise le chatbot IA : http://localhost:5000
- Pose des questions dans le groupe
- Consulte la documentation

Bon développement ! 🚀

[Ton Nom]
```

---

## 🔧 Étape 3 : Configurer les Permissions (Optionnel)

### Protéger la Branche Main

Pour éviter les commits directs sur `main` :

1. **Settings** → **Branches** → **Add branch protection rule**

2. **Branch name pattern** : `main`

3. **Cochez les options suivantes :**
   - ✅ **Require a pull request before merging**
     - Oblige à créer une PR
   - ✅ **Require approvals** (1 approbation minimum)
     - Vous devez approuver les PR
   - ✅ **Require status checks to pass before merging**
     - CI/CD doit passer (MyPy + Ruff)
   - ✅ **Require conversation resolution before merging**
     - Tous les commentaires doivent être résolus

4. **Cliquez sur "Create"**

### Configurer les Notifications

1. **Settings** → **Notifications**

2. **Configurez les notifications pour :**
   - ✅ Pull Requests
   - ✅ Issues
   - ✅ Commits
   - ✅ CI/CD failures

---

## 📝 Étape 4 : Créer des Issues pour Répartir le Travail

### Exemples d'Issues à Créer

#### Issue 1 : Ajouter des Produits
```markdown
**Titre :** Ajouter 10 nouveaux produits dans le catalogue Shopify

**Description :**
Ajouter 10 nouveaux produits dans `shopify/init_data.py`

**Critères d'acceptation :**
- [ ] 10 produits ajoutés avec toutes les informations
- [ ] Images valides (URLs)
- [ ] Prix réalistes
- [ ] Descriptions en français
- [ ] MyPy passe
- [ ] Ruff passe

**Assigné à :** @alice-dev
**Labels :** enhancement, shopify
**Milestone :** v2.0
```

#### Issue 2 : Améliorer le Design
```markdown
**Titre :** Améliorer le design de la page d'accueil Shopify

**Description :**
Améliorer le CSS de la page d'accueil pour un rendu plus moderne

**Critères d'acceptation :**
- [ ] Hero section plus attractive
- [ ] Animations CSS
- [ ] Responsive design testé
- [ ] Compatible Chrome, Firefox, Safari

**Assigné à :** @bob-designer
**Labels :** enhancement, ui/ux
**Milestone :** v2.0
```

#### Issue 3 : Ajouter des Tests
```markdown
**Titre :** Ajouter des tests unitaires pour les modèles Shopify

**Description :**
Créer des tests pour les modèles dans `shopify/models.py`

**Critères d'acceptation :**
- [ ] Tests pour Product
- [ ] Tests pour User
- [ ] Tests pour Order
- [ ] Couverture > 80%
- [ ] MyPy passe

**Assigné à :** @charlie-tester
**Labels :** testing
**Milestone :** v2.0
```

### Comment Créer une Issue

1. **Allez sur l'onglet "Issues"**
2. **Cliquez sur "New issue"**
3. **Remplissez :**
   - Titre clair
   - Description détaillée
   - Assignez à un collaborateur
   - Ajoutez des labels
   - Définissez un milestone
4. **Cliquez sur "Submit new issue"**

---

## 🎯 Étape 5 : Organiser le Travail en Milestones

### Créer des Milestones

1. **Issues** → **Milestones** → **New milestone**

2. **Exemples de milestones :**

   **Milestone 1 : v1.0 - Version Stable**
   - Description : Version actuelle avec CI/CD + Chatbot + Shopify de base
   - Due date : Déjà atteint
   - Status : Closed

   **Milestone 2 : v2.0 - Améliorations**
   - Description : Nouveaux produits, design amélioré, tests
   - Due date : Dans 2 semaines
   - Issues : 10 produits, design, tests

   **Milestone 3 : v3.0 - Fonctionnalités Avancées**
   - Description : Paiement, avis clients, recherche avancée
   - Due date : Dans 1 mois
   - Issues : Stripe, reviews, search

---

## 📊 Étape 6 : Suivre l'Avancement

### Utiliser le Project Board

1. **Projects** → **New project** → **Board**

2. **Créer des colonnes :**
   - 📋 **To Do** (À faire)
   - 🚧 **In Progress** (En cours)
   - 👀 **In Review** (En revue)
   - ✅ **Done** (Terminé)

3. **Ajouter les issues dans les colonnes**

4. **Déplacer les cartes** au fur et à mesure

### Utiliser les Labels

Créez des labels pour organiser :
- 🐛 `bug` - Corrections de bugs
- ✨ `enhancement` - Nouvelles fonctionnalités
- 📚 `documentation` - Documentation
- 🧪 `testing` - Tests
- 🛍️ `shopify` - Fonctionnalités Shopify
- 🤖 `ci-cd` - Pipeline CI/CD
- 🎨 `ui/ux` - Design

---

## ✅ Checklist pour Chaque Nouveau Collaborateur

Envoyez cette checklist à chaque nouveau membre :

### Installation (30 minutes)
- [ ] Compte GitHub créé
- [ ] Invitation acceptée
- [ ] Repository cloné
- [ ] Python 3.10+ installé
- [ ] Environnement virtuel créé
- [ ] Dépendances installées (`pip install -r requirements.txt`)
- [ ] Fichier `.env` créé avec `GROQ_API_KEY`
- [ ] MyPy fonctionne (`python -m mypy --version`)
- [ ] Ruff fonctionne (`python -m ruff --version`)

### Tests (15 minutes)
- [ ] Chatbot testé (http://localhost:5000)
- [ ] Shopify testé (http://localhost:5001)
- [ ] Connexion client testée
- [ ] Connexion admin testée
- [ ] Auto-Fix testé dans le chatbot

### Documentation (30 minutes)
- [ ] QUICK_START.md lu
- [ ] GUIDE_COLLABORATEURS.md lu
- [ ] ARCHITECTURE_TECHNIQUE.md parcouru
- [ ] Compris pourquoi Ruff > Pylint
- [ ] Compris pourquoi MyPy > TypeScript

### Première Contribution (1 heure)
- [ ] Branche créée (`git checkout -b feature/mon-nom-test`)
- [ ] Modification faite (ex: ajout d'un produit)
- [ ] Vérifications passées (`mypy` + `ruff`)
- [ ] Commit fait avec message clair
- [ ] Push fait vers la branche
- [ ] Pull Request créée
- [ ] PR mergée après approbation

---

## 🆘 Problèmes Courants

### Collaborateur ne reçoit pas l'invitation

**Solution :**
1. Vérifiez l'email dans les paramètres GitHub du collaborateur
2. Demandez-lui de vérifier ses spams
3. Renvoyez l'invitation : Settings → Collaborators → Resend invitation

### Collaborateur ne peut pas push

**Erreur :**
```
remote: Permission to bengo2024/python-typed-project.git denied
```

**Solution :**
1. Vérifiez qu'il a accepté l'invitation
2. Vérifiez qu'il a les droits "Write"
3. Vérifiez qu'il utilise le bon compte GitHub :
   ```bash
   git config user.name
   git config user.email
   ```

### Collaborateur ne peut pas créer de branche

**Solution :**
1. Vérifiez les permissions (Write minimum)
2. Vérifiez qu'il a bien cloné le repo :
   ```bash
   git remote -v
   # Doit afficher : origin  https://github.com/bengo2024/python-typed-project.git
   ```

---

## 📞 Support

### Pour les Collaborateurs

1. **Consultez la documentation**
   - QUICK_START.md
   - GUIDE_COLLABORATEURS.md
   - ARCHITECTURE_TECHNIQUE.md

2. **Utilisez le chatbot IA**
   - http://localhost:5000
   - Posez vos questions sur les erreurs

3. **Créez une issue**
   - Si problème technique
   - Si question sur le projet

4. **Contactez le groupe**
   - Discord, WhatsApp, etc.

### Pour Vous (Propriétaire)

1. **Répondez aux Pull Requests rapidement**
2. **Donnez du feedback constructif**
3. **Organisez des réunions de suivi**
4. **Partagez les bonnes pratiques**

---

## 🎉 Félicitations !

Votre équipe est maintenant prête à collaborer efficacement sur le projet !

**Prochaines étapes :**
1. ✅ Tous les membres ont accepté l'invitation
2. ✅ Tous les membres ont installé le projet
3. ✅ Tous les membres ont fait leur première PR
4. ✅ Le travail est réparti via les issues
5. ✅ Le suivi est fait via le project board

**Bon travail d'équipe ! 🚀👥**

