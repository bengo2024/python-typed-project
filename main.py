from typing import List, Dict, Optional

def add_numbers(a: int, b: int) -> int:
    """Ajoute deux nombres entiers."""
    return a + b

def process_users(users: List[Dict[str, str]]) -> Optional[str]:
    """Traite une liste d'utilisateurs et retourne un message."""
    if not users:
        return None
    return f"Nombre d'utilisateurs : {len(users)}"

def greet_user(name: str, language: str = "fr") -> str:
    """Salutation typée en français par défaut."""
    if language == "fr":
        return f"Bonjour, {name} !"
    return f"Hello, {name} !"

if __name__ == "__main__":
    print(add_numbers(2, 3))
    users = [{"name": "Alice"}, {"name": "Bob"}]
    print(process_users(users))
    print(greet_user("Charlie"))