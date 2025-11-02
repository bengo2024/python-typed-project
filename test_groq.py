"""Test de la clé API Groq."""

import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


def test_groq_api() -> None:
    """Teste la connexion à l'API Groq."""
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        print("❌ GROQ_API_KEY non trouvée dans .env")
        return

    try:
        client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": "Dis bonjour en français"}],
        )

        print("✅ Connexion à Groq réussie !")
        print(f"Réponse: {response.choices[0].message.content}")

    except Exception as e:
        print(f"❌ Erreur: {e}")


if __name__ == "__main__":
    test_groq_api()
