"""
Script d'initialisation de la base de données avec des données de démonstration
"""

import hashlib
import secrets


# import hashlib


def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    return (
        hashlib.pbkdf2_hmac("sha256", password.encode(), salt.encode(), 100000).hex()
        + ":"
        + salt
    )


from shopify.database import Database
from shopify.models import Product, User, UserRole


def hash_password(password: str) -> str:
    """Hash un mot de passe."""
    return hashlib.sha256(password.encode()).hexdigest()


def init_demo_data() -> None:
    """Initialise la base de données avec des données de démonstration."""
    db = Database()

    print("🔧 Initialisation de la base de données Shopify...")

    # Créer un utilisateur admin
    admin = User(
        # id=0,
        email="admin@shopify.com",
        password_hash=hash_password("admin123"),
        first_name="Admin",
        last_name="Shopify",
        role=UserRole.ADMIN,
    )

    # Vérifier si l'admin existe déjà
    existing_admin = db.get_user_by_email("admin@shopify.com")
    if not existing_admin:
        db.add_user(admin)
        print("✅ Utilisateur admin créé (admin@shopify.com / admin123)")
    else:
        print("ℹ️  Utilisateur admin déjà existant")

    # Créer un utilisateur client
    customer = User(
        # id=0,
        email="client@example.com",
        password_hash=hash_password("client123"),
        first_name="Jean",
        last_name="Dupont",
        role=UserRole.CUSTOMER,
    )

    existing_customer = db.get_user_by_email("client@example.com")
    if not existing_customer:
        db.add_user(customer)
        print("✅ Utilisateur client créé (client@example.com / client123)")
    else:
        print("ℹ️  Utilisateur client déjà existant")

    # Produits de démonstration
    demo_products = [
        Product(
            #   id=0,
            name='MacBook Pro 16"',
            description="Ordinateur portable professionnel avec puce M3 Pro, 16 Go RAM, 512 Go SSD. Parfait pour le développement et la création de contenu.",
            price=2499.99,
            image_url="https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500",
            category="Électronique",
            stock=15,
            rating=4.8,
            reviews_count=127,
        ),
        Product(
            #   id=0,
            name="iPhone 15 Pro",
            description="Smartphone haut de gamme avec puce A17 Pro, appareil photo 48MP, écran Super Retina XDR 6.1 pouces.",
            price=1199.99,
            image_url="https://images.unsplash.com/photo-1592286927505-c0d5e9d6e87e?w=500",
            category="Électronique",
            stock=25,
            rating=4.9,
            reviews_count=342,
        ),
        Product(
            #  id=0,
            name="AirPods Pro 2",
            description="Écouteurs sans fil avec réduction de bruit active, audio spatial, jusqu'à 6h d'autonomie.",
            price=279.99,
            image_url="https://images.unsplash.com/photo-1606841837239-c5a1a4a07af7?w=500",
            category="Électronique",
            stock=50,
            rating=4.7,
            reviews_count=89,
        ),
        Product(
            #  id=0,
            name="Nike Air Max 2024",
            description="Chaussures de sport confortables avec amorti Air Max, design moderne et respirant.",
            price=159.99,
            image_url="https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500",
            category="Mode",
            stock=40,
            rating=4.6,
            reviews_count=156,
        ),
        Product(
            #  id=0,
            name="Sac à dos Eastpak",
            description="Sac à dos résistant 24L, compartiment laptop, garantie 30 ans. Idéal pour l'école ou le travail.",
            price=79.99,
            image_url="https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=500",
            category="Mode",
            stock=30,
            rating=4.5,
            reviews_count=78,
        ),
        Product(
            #  id=0,
            name="Montre Casio G-Shock",
            description="Montre sport résistante aux chocs, étanche 200m, chronomètre, alarme, rétroéclairage LED.",
            price=129.99,
            image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
            category="Mode",
            stock=20,
            rating=4.8,
            reviews_count=234,
        ),
        Product(
            #   id=0,
            name="PlayStation 5",
            description="Console de jeu nouvelle génération avec SSD ultra-rapide, ray tracing, 4K 120fps.",
            price=499.99,
            image_url="https://images.unsplash.com/photo-1606813907291-d86efa9b94db?w=500",
            category="Gaming",
            stock=10,
            rating=4.9,
            reviews_count=567,
        ),
        Product(
            # id=0,
            name="Manette DualSense",
            description="Manette sans fil pour PS5 avec retour haptique, gâchettes adaptatives, micro intégré.",
            price=69.99,
            image_url="https://images.unsplash.com/photo-1592840496694-26d035b52b48?w=500",
            category="Gaming",
            stock=35,
            rating=4.7,
            reviews_count=189,
        ),
        Product(
            #  id=0,
            name="Casque Gaming HyperX",
            description="Casque gaming avec son surround 7.1, micro antibruit, coussinets en mousse à mémoire de forme.",
            price=99.99,
            image_url="https://images.unsplash.com/photo-1599669454699-248893623440?w=500",
            category="Gaming",
            stock=25,
            rating=4.6,
            reviews_count=145,
        ),
        Product(
            #  id=0,
            name="Kindle Paperwhite",
            description="Liseuse électronique avec écran 6.8 pouces, éclairage réglable, étanche IPX8, 16 Go.",
            price=149.99,
            image_url="https://images.unsplash.com/photo-1592496431122-2349e0fbc666?w=500",
            category="Livres",
            stock=45,
            rating=4.8,
            reviews_count=892,
        ),
        Product(
            # id=0,
            name="Caméra GoPro Hero 12",
            description="Caméra d'action 5.3K60, stabilisation HyperSmooth 6.0, étanche 10m, écran tactile.",
            price=399.99,
            image_url="https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?w=500",
            category="Électronique",
            stock=18,
            rating=4.7,
            reviews_count=267,
        ),
        Product(
            # id=0,
            name="Clavier Mécanique Logitech",
            description="Clavier gaming mécanique RGB, switches tactiles, repose-poignet, touches programmables.",
            price=149.99,
            image_url="https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=500",
            category="Électronique",
            stock=22,
            rating=4.6,
            reviews_count=178,
        ),
    ]

    # Ajouter les produits s'ils n'existent pas déjà
    existing_products = db.get_products()  # ou db.list_products()

    if len(existing_products) == 0:
        for product in demo_products:
            db.add_product(product)
        print(f"✅ {len(demo_products)} produits de démonstration ajoutés")
    else:
        print(f"ℹ️  {len(existing_products)} produits déjà existants")

    print("\n🎉 Initialisation terminée !")
    print("\n📝 Comptes de test :")
    print("   Admin: admin@shopify.com / admin123")
    print("   Client: client@example.com / client123")
    print("\n🚀 Lancez l'application avec: python -m shopify.app")


if __name__ == "__main__":
    init_demo_data()
