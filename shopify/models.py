"""
Modèles de données pour Shopify
Tous les modèles sont typés pour passer MyPy
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class OrderStatus(Enum):
    """Statut d'une commande."""

    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class UserRole(Enum):
    """Rôle d'un utilisateur."""

    CUSTOMER = "customer"
    ADMIN = "admin"


@dataclass
class Product:
    """Modèle de produit."""

    id: int
    name: str
    description: str
    price: float
    image_url: str
    category: str
    stock: int
    rating: float = 0.0
    reviews_count: int = 0
    created_at: datetime = field(default_factory=datetime.now)

    def is_available(self) -> bool:
        """Vérifie si le produit est disponible."""
        return self.stock > 0

    def to_dict(self) -> dict[str, str | int | float]:
        """Convertit le produit en dictionnaire."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_url": self.image_url,
            "category": self.category,
            "stock": self.stock,
            "rating": self.rating,
            "reviews_count": self.reviews_count,
            "created_at": self.created_at.isoformat(),
        }


@dataclass
class User:
    """Modèle d'utilisateur."""

    id: int
    email: str
    password_hash: str
    first_name: str
    last_name: str
    role: UserRole = UserRole.CUSTOMER
    created_at: datetime = field(default_factory=datetime.now)

    def is_admin(self) -> bool:
        """Vérifie si l'utilisateur est admin."""
        return self.role == UserRole.ADMIN

    def full_name(self) -> str:
        """Retourne le nom complet."""
        return f"{self.first_name} {self.last_name}"


@dataclass
class CartItem:
    """Article dans le panier."""

    product_id: int
    product_name: str
    product_price: float
    product_image: str
    quantity: int

    def subtotal(self) -> float:
        """Calcule le sous-total."""
        return self.product_price * self.quantity

    def to_dict(self) -> dict[str, str | int | float]:
        """Convertit en dictionnaire."""
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "product_price": self.product_price,
            "product_image": self.product_image,
            "quantity": self.quantity,
            "subtotal": self.subtotal(),
        }


@dataclass
class Order:
    """Modèle de commande."""

    id: int
    user_id: int
    items: list[CartItem]
    total: float
    status: OrderStatus
    shipping_address: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def items_count(self) -> int:
        """Retourne le nombre total d'articles."""
        return sum(item.quantity for item in self.items)

    def to_dict(
        self,
    ) -> dict[str, str | int | float | list[dict[str, str | int | float]]]:
        """Convertit en dictionnaire."""
        return {
            "id": self.id,
            "user_id": self.user_id,
            "items": [item.to_dict() for item in self.items],
            "total": self.total,
            "status": self.status.value,
            "shipping_address": self.shipping_address,
            "items_count": self.items_count(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }


@dataclass
class Review:
    """Avis client sur un produit."""

    id: int
    product_id: int
    user_id: int
    user_name: str
    rating: int  # 1-5 étoiles
    comment: str
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict[str, str | int]:
        """Convertit en dictionnaire."""
        return {
            "id": self.id,
            "product_id": self.product_id,
            "user_id": self.user_id,
            "user_name": self.user_name,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at.isoformat(),
        }
