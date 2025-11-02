import os  # Import inutilisé pour tester Discord
import sys  # Import inutilisé pour tester Discord
import json  # Encore un import inutilisé

def add_numbers(a: int, b: int) -> int:
    """Ajoute deux nombres entiers."""
    return a + b

def process_users(users: list[dict[str, str]]) -> str | None:
    """Traite une liste d'utilisateurs et retourne un message."""
    if not users:
        return None
    return f"Nombre d'utilisateurs : {len(users)}"

def greet_user(name: str, language: str = "fr") -> str:
    """Salutation typée en français par défaut."""
    if language == "fr":
        return f"Bonjour, {name} !"
    return f"Hello, {name} !"


def multiply_numbers(x: int, y: int) -> int:
    """Multiplie deux nombres entiers."""
    return x * y


def divide_numbers(a: float, b: float) -> float:
    """Divise deux nombres flottants."""
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


def fonction_sans_types(x, y):
    """Fonction sans annotations de types - va générer une erreur MyPy."""
    return x + y


def test_discord_notification(x, y):
    """Fonction sans types pour tester Discord + MyPy."""
    return x * y


if __name__ == "__main__":
    print(add_numbers(2, 3))
    users = [{"name": "Alice"}, {"name": "Bob"}]
    print(process_users(users))
    print(greet_user("Charlie"))
    print(test_discord_notification(5, 10))
