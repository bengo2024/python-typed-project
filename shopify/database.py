"""
Gestion de la base de données SQLite pour Shopify
Toutes les fonctions sont typées pour passer MyPy
"""

import sqlite3
from datetime import datetime
from pathlib import Path

from shopify.models import (
    CartItem,
    Order,
    OrderStatus,
    Product,
    User,
    UserRole,
)


class Database:
    """Gestionnaire de base de données SQLite."""

    def __init__(self, db_path: str = "shopify/shopify.db") -> None:
        """Initialise la connexion à la base de données."""
        self.db_path = db_path
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        self.init_database()

    def get_connection(self) -> sqlite3.Connection:
        """Retourne une connexion à la base de données."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_database(self) -> None:
        """Crée les tables si elles n'existent pas."""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Table des produits
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                price REAL NOT NULL,
                image_url TEXT NOT NULL,
                category TEXT NOT NULL,
                stock INTEGER NOT NULL,
                rating REAL DEFAULT 0.0,
                reviews_count INTEGER DEFAULT 0,
                created_at TEXT NOT NULL
            )
        """
        )

        # Table des utilisateurs
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                role TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """
        )

        # Table des commandes
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                total REAL NOT NULL,
                status TEXT NOT NULL,
                shipping_address TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """
        )

        # Table des articles de commande
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS order_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                product_name TEXT NOT NULL,
                product_price REAL NOT NULL,
                product_image TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (order_id) REFERENCES orders (id),
                FOREIGN KEY (product_id) REFERENCES products (id)
            )
        """
        )

        # Table des avis
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                user_name TEXT NOT NULL,
                rating INTEGER NOT NULL,
                comment TEXT NOT NULL,
                created_at TEXT NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products (id),
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """
        )

        conn.commit()
        conn.close()

    def add_product(self, product: Product) -> int:
        """Ajoute un produit à la base de données."""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO products (name, description, price, image_url, category, stock, rating, reviews_count, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
            (
                product.name,
                product.description,
                product.price,
                product.image_url,
                product.category,
                product.stock,
                product.rating,
                product.reviews_count,
                product.created_at.isoformat(),
            ),
        )

        product_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return product_id if product_id else 0

    def get_all_products(self) -> list[Product]:
        """Récupère tous les produits."""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products ORDER BY created_at DESC")
        rows = cursor.fetchall()
        conn.close()

        products: list[Product] = []
        for row in rows:
            products.append(
                Product(
                    id=row["id"],
                    name=row["name"],
                    description=row["description"],
                    price=row["price"],
                    image_url=row["image_url"],
                    category=row["category"],
                    stock=row["stock"],
                    rating=row["rating"],
                    reviews_count=row["reviews_count"],
                    created_at=datetime.fromisoformat(row["created_at"]),
                )
            )

        return products

    def get_product_by_id(self, product_id: int) -> Product | None:
        """Récupère un produit par son ID."""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        return Product(
            id=row["id"],
            name=row["name"],
            description=row["description"],
            price=row["price"],
            image_url=row["image_url"],
            category=row["category"],
            stock=row["stock"],
            rating=row["rating"],
            reviews_count=row["reviews_count"],
            created_at=datetime.fromisoformat(row["created_at"]),
        )

    def search_products(self, query: str) -> list[Product]:
        """Recherche des produits par nom ou description."""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM products
            WHERE name LIKE ? OR description LIKE ?
            ORDER BY created_at DESC
        """,
            (f"%{query}%", f"%{query}%"),
        )

        rows = cursor.fetchall()
        conn.close()

        products: list[Product] = []
        for row in rows:
            products.append(
                Product(
                    id=row["id"],
                    name=row["name"],
                    description=row["description"],
                    price=row["price"],
                    image_url=row["image_url"],
                    category=row["category"],
                    stock=row["stock"],
                    rating=row["rating"],
                    reviews_count=row["reviews_count"],
                    created_at=datetime.fromisoformat(row["created_at"]),
                )
            )

        return products

    def get_products_by_category(self, category: str) -> list[Product]:
        """Récupère les produits d'une catégorie."""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM products WHERE category = ? ORDER BY created_at DESC",
            (category,),
        )

        rows = cursor.fetchall()
        conn.close()

        products: list[Product] = []
        for row in rows:
            products.append(
                Product(
                    id=row["id"],
                    name=row["name"],
                    description=row["description"],
                    price=row["price"],
                    image_url=row["image_url"],
                    category=row["category"],
                    stock=row["stock"],
                    rating=row["rating"],
                    reviews_count=row["reviews_count"],
                    created_at=datetime.fromisoformat(row["created_at"]),
                )
            )

        return products

    def add_user(self, user: User) -> int:
        """Ajoute un utilisateur."""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users (email, password_hash, first_name, last_name, role, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (
                user.email,
                user.password_hash,
                user.first_name,
                user.last_name,
                user.role.value,
                user.created_at.isoformat(),
            ),
        )

        user_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return user_id if user_id else 0

    def get_user_by_email(self, email: str) -> User | None:
        """Récupère un utilisateur par email."""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        return User(
            id=row["id"],
            email=row["email"],
            password_hash=row["password_hash"],
            first_name=row["first_name"],
            last_name=row["last_name"],
            role=UserRole(row["role"]),
            created_at=datetime.fromisoformat(row["created_at"]),
        )

    def create_order(self, order: Order) -> int:
        """Crée une commande."""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Insérer la commande
        cursor.execute(
            """
            INSERT INTO orders (user_id, total, status, shipping_address, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
            (
                order.user_id,
                order.total,
                order.status.value,
                order.shipping_address,
                order.created_at.isoformat(),
                order.updated_at.isoformat(),
            ),
        )

        order_id = cursor.lastrowid

        # Insérer les articles
        for item in order.items:
            cursor.execute(
                """
                INSERT INTO order_items (order_id, product_id, product_name, product_price, product_image, quantity)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    order_id,
                    item.product_id,
                    item.product_name,
                    item.product_price,
                    item.product_image,
                    item.quantity,
                ),
            )

        conn.commit()
        conn.close()

        return order_id if order_id else 0

    def get_user_orders(self, user_id: int) -> list[Order]:
        """Récupère les commandes d'un utilisateur."""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM orders WHERE user_id = ? ORDER BY created_at DESC",
            (user_id,),
        )

        orders_rows = cursor.fetchall()
        orders: list[Order] = []

        for order_row in orders_rows:
            # Récupérer les articles de la commande
            cursor.execute(
                "SELECT * FROM order_items WHERE order_id = ?", (order_row["id"],)
            )
            items_rows = cursor.fetchall()

            items: list[CartItem] = []
            for item_row in items_rows:
                items.append(
                    CartItem(
                        product_id=item_row["product_id"],
                        product_name=item_row["product_name"],
                        product_price=item_row["product_price"],
                        product_image=item_row["product_image"],
                        quantity=item_row["quantity"],
                    )
                )

            orders.append(
                Order(
                    id=order_row["id"],
                    user_id=order_row["user_id"],
                    items=items,
                    total=order_row["total"],
                    status=OrderStatus(order_row["status"]),
                    shipping_address=order_row["shipping_address"],
                    created_at=datetime.fromisoformat(order_row["created_at"]),
                    updated_at=datetime.fromisoformat(order_row["updated_at"]),
                )
            )

        conn.close()
        return orders

