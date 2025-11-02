@echo off
echo ========================================
echo   Demarrage du Chatbot CI/CD
echo ========================================
echo.

REM Verifier si .env existe
if not exist .env (
    echo ERREUR: Le fichier .env n'existe pas !
    echo.
    echo Creez un fichier .env avec votre cle Groq :
    echo GROQ_API_KEY=gsk_votre_cle_ici
    echo.
    echo Obtenez votre cle sur : https://console.groq.com/keys
    echo.
    pause
    exit /b 1
)

echo Chargement de la configuration...
echo.

REM Lancer le chatbot
python chatbot_app.py

pause

