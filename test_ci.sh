#!/bin/bash
# Script de test CI/CD en local

echo "🚀 Test du système CI/CD en local"
echo "=================================="
echo ""

# Couleurs
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Compteur d'erreurs
ERRORS=0

# Test 1: MyPy
echo "📝 Test 1: Vérification des types avec MyPy..."
if python -m mypy main.py > /dev/null 2>&1; then
    echo -e "${GREEN}✅ MyPy: Aucune erreur de type${NC}"
else
    echo -e "${RED}❌ MyPy: Erreurs détectées${NC}"
    python -m mypy main.py
    ERRORS=$((ERRORS + 1))
fi
echo ""

# Test 2: Ruff
echo "🔍 Test 2: Vérification du style avec Ruff..."
if python -m ruff check . > /dev/null 2>&1; then
    echo -e "${GREEN}✅ Ruff: Code conforme aux normes${NC}"
else
    echo -e "${RED}❌ Ruff: Erreurs de style détectées${NC}"
    python -m ruff check .
    ERRORS=$((ERRORS + 1))
fi
echo ""

# Test 3: Vérifier que les secrets ne sont pas commitées
echo "🔐 Test 3: Vérification des fichiers sensibles..."
if grep -r "sk-proj-" . --exclude-dir=.git --exclude="*.md" --exclude="test_ci.sh" > /dev/null 2>&1; then
    echo -e "${RED}❌ ATTENTION: Clé API OpenAI détectée dans le code !${NC}"
    ERRORS=$((ERRORS + 1))
else
    echo -e "${GREEN}✅ Aucune clé API exposée${NC}"
fi
echo ""

# Résumé
echo "=================================="
if [ $ERRORS -eq 0 ]; then
    echo -e "${GREEN}🎉 TOUS LES TESTS SONT PASSÉS !${NC}"
    echo "Vous pouvez pusher en toute sécurité."
    exit 0
else
    echo -e "${RED}❌ $ERRORS test(s) échoué(s)${NC}"
    echo "Corrigez les erreurs avant de pusher."
    exit 1
fi

