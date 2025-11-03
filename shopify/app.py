"""
Shopify - Application E-Commerce Flask
Intégrée avec le système CI/CD
"""
import hashlib
import os
from typing import Any

from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)
from werkzeug.wrappers.response import Response

from shopify.database import Database
from shopify.models import CartItem, Order, OrderStatus, Product, User, UserRole


# Obtenir le chemin du répertoire parent (racine du projet)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)
app.secret_key = "shopify-secret-key-change-in-production"
app.config["SESSION_TYPE"] = "filesystem"

# Initialiser la base de données
db = Database()

@app.context_processor
def inject_globals() -> dict[str, Any]:
    """Injecte des variables globales dans tous les templates."""
    user = get_current_user()
    cart = get_cart()
    cart_count = sum(item.quantity for item in cart)
    return {
        "user": user,
        "cart_count": cart_count,
    }

def hash_password(password: str) -> str:
    """Hash un mot de passe avec SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def get_current_user() -> User | None:
    """Récupère l'utilisateur connecté."""
    if "user_email" in session:
        return db.get_user_by_email(session["user_email"])
    return None

def get_cart() -> list[CartItem]:
    """Récupère le panier de la session."""
    if "cart" not in session:
        session["cart"] = []
    cart_data: list[dict[str, Any]] = session["cart"]
    cart: list[CartItem] = []
    for item_data in cart_data:
        cart.append(
            CartItem(
                product_id=item_data["product_id"],
                product_name=item_data["product_name"],
                product_price=item_data["product_price"],
                product_image=item_data["product_image"],
                quantity=item_data["quantity"],
            )
        )
    return cart

def save_cart(cart: list[CartItem]) -> None:
    """Sauvegarde le panier dans la session."""
    session["cart"] = [item.to_dict() for item in cart]

def calculate_cart_total(cart: list[CartItem]) -> float:
    """Calcule le total du panier."""
    return sum(item.subtotal() for item in cart)

@app.route("/")
def index() -> str:
    """Page d'accueil."""
    products = db.get_all_products()
    user = get_current_user()
    cart = get_cart()
    return render_template(
        "shopify/index.html",
        products=products[:8],  # Afficher les 8 derniers produits
        user=user,
        cart_count=sum(item.quantity for item in cart),
    )

@app.route("/products")
def products() -> str:
    """Page catalogue de produits."""
    category = request.args.get("category")
    search = request.args.get("search")
    if search:
        products_list = db.search_products(search)
    elif category:
        products_list = db.get_products_by_category(category)
    else:
        products_list = db.get_all_products()
    user = get_current_user()
    cart = get_cart()
    return render_template(
        "shopify/products.html",
        products=products_list,
        user=user,
        cart_count=sum(item.quantity for item in cart),
        current_category=category,
        search_query=search,
    )

@app.route("/product/<int:product_id>")
def product_detail(product_id: int) -> str | Response:
    """Page détail d'un produit."""
    product = db.get_product_by_id(product_id)
    if not product:
        flash("Produit introuvable", "error")
        return redirect(url_for("products"))
    user = get_current_user()
    cart = get_cart()
    return render_template(
        "shopify/product_detail.html",
        product=product,
        user=user,
        cart_count=sum(item.quantity for item in cart),
    )

@app.route("/cart")
def cart() -> str:
    """Page panier."""
    cart_items = get_cart()
    total = calculate_cart_total(cart_items)
    user = get_current_user()
    return render_template(
        "shopify/cart.html",
        cart=cart_items,
        total=total,
        user=user,
        cart_count=sum(item.quantity for item in cart_items),
    )

@app.route("/cart/add/<int:product_id>", methods=["POST"])
def add_to_cart(product_id: int) -> Any:
    """Ajoute un produit au panier."""
    product = db.get_product_by_id(product_id)
    if not product:
        flash("Produit introuvable", "error")
        return redirect(url_for("products"))
    if not product.is_available():
        flash("Produit en rupture de stock", "error")
        return redirect(url_for("product_detail", product_id=product_id))
    cart_items = get_cart()
    # Vérifier si le produit est déjà dans le panier
    found = False
    for item in cart_items:
        if item.product_id == product_id:
            item.quantity += 1
            found = True
            break
    if not found:
        cart_items.append(
            CartItem(
                product_id=product.id,
                product_name=product.name,
                product_price=product.price,
                product_image=product.image_url,
                quantity=1,
            )
        )
    save_cart(cart_items)
    flash(f"{product.name} ajouté au panier", "success")
    return redirect(url_for("cart"))

@app.route("/cart/remove/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id: int) -> Any:
    """Retire un produit du panier."""
    cart_items = get_cart()
    cart_items = [item for item in cart_items if item.product_id != product_id]
    save_cart(cart_items)
    flash("Produit retiré du panier", "success")
    return redirect(url_for("cart"))

@app.route("/cart/update/<int:product_id>", methods=["POST"])
def update_cart(product_id: int) -> Any:
    """Met à jour la quantité d'un produit dans le panier."""
    quantity = int(request.form.get("quantity", 1))
    if quantity < 1:
        return remove_from_cart(product_id)
    cart_items = get_cart()
    for item in cart_items:
        if item.product_id == product_id:
            item.quantity = quantity
            break
    save_cart(cart_items)
    flash("Panier mis à jour", "success")
    return redirect(url_for("cart"))

@app.route("/checkout")
def checkout() -> str | Any:
    """Page de paiement."""
    user = get_current_user()
    if not user:
        flash("Vous devez être connecté pour passer commande", "error")
        return redirect(url_for("login"))
    cart_items = get_cart()
    if not cart_items:
        flash("Votre panier est vide", "error")
        return redirect(url_for("products"))
    total = calculate_cart_total(cart_items)
    return render_template(
        "shopify/checkout.html",
        cart=cart_items,
        total=total,
        user=user,
        cart_count=sum(item.quantity for item in cart_items),
    )

@app.route("/checkout/process", methods=["POST"])
def process_checkout() -> Any:
    """Traite le paiement."""
    user = get_current_user()
    if not user:
        flash("Vous devez être connecté pour passer commande", "error")
        return redirect(url_for("login"))
    cart_items = get_cart()
    if not cart_items:
        flash("Votre panier est vide", "error")
        return redirect(url_for("products"))
    shipping_address = request.form.get("shipping_address", "")
    if not shipping_address:
        flash("Adresse de livraison requise", "error")
        return redirect(url_for("checkout"))
    total = calculate_cart_total(cart_items)
    # Créer la commande
    order = Order(
        id=0,  # Sera généré par la base de données
        user_id=user.id,
        items=cart_items,
        total=total,
        status=OrderStatus.PAID,
        shipping_address=shipping_address,
    )
    order_id = db.create_order(order)
    # Vider le panier
    session["cart"] = []
    flash(f"Commande #{order_id} passée avec succès !", "success")
    return redirect(url_for("orders"))

@app.route("/orders")
def orders() -> str | Any:
    """Page des commandes de l'utilisateur."""
    user = get_current_user()
    if not user:
        flash("Vous devez être connecté pour voir vos commandes", "error")
        return redirect(url_for("login"))
    user_orders = db.get_user_orders(user.id)
    cart = get_cart()
    return render_template(
        "shopify/orders.html",
        orders=user_orders,
        user=user,
        cart_count=sum(item.quantity for item in cart),
    )

@app.route("/login", methods=["GET", "POST"])
def login() -> str | Any:
    """Page de connexion."""
    from shopify.app import get_cart  # si ce n'est pas déjà importé
    cart = get_cart()  # récupère le panier actuel
    cart_count = sum(item.quantity for item in cart)  # calcul du nombre d'articles
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        if not email or not password:
            flash("Email et mot de passe requis", "error")
            return render_template("shopify/login.html", cart_count=cart_count)
        user = db.get_user_by_email(email)
        if not user or user.password_hash != hash_password(password):
            flash("Email ou mot de passe incorrect", "error")
            return render_template("shopify/login.html", cart_count=cart_count)
        session["user_email"] = user.email
        flash(f"Bienvenue {user.first_name} !", "success")
        return redirect(url_for("index"))
    # GET request
    return render_template("shopify/login.html", cart_count=cart_count)

@app.route("/register", methods=["GET", "POST"])
def register() -> str | Any:
    """Page d'inscription."""
    cart = get_cart()
    cart_count = sum(item.quantity for item in cart)
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")
        first_name = request.form.get("first_name", "")
        last_name = request.form.get("last_name", "")
        if not all([email, password, first_name, last_name]):
            flash("Tous les champs sont requis", "error")
            return render_template("shopify/register.html", cart_count=cart_count)
        existing_user = db.get_user_by_email(email)
        if existing_user:
            flash("Cet email est déjà utilisé", "error")
            return render_template("shopify/register.html", cart_count=cart_count)
        user = User(
            id=0,
            email=email,
            password_hash=hash_password(password),
            first_name=first_name,
            last_name=last_name,
            role=UserRole.CUSTOMER,
        )
        db.add_user(user)
        session["user_email"] = email
        flash(f"Compte créé avec succès ! Bienvenue {first_name} !", "success")
        return redirect(url_for("index"))
    return render_template("shopify/register.html", cart_count=cart_count)

@app.route("/logout")
def logout() -> Any:
    """Déconnexion."""
    session.pop("user_email", None)
    flash("Vous êtes déconnecté", "success")
    return redirect(url_for("index"))

@app.route("/admin")
def admin_dashboard() -> str | Any:
    """Tableau de bord admin."""
    user = get_current_user()
    if not user or not user.is_admin():
        flash("Accès refusé", "error")
        return redirect(url_for("index"))
    products = db.get_all_products()
    cart = get_cart()
    return render_template(
        "shopify/admin/dashboard.html",
        products=products,
        user=user,
        cart_count=sum(item.quantity for item in cart),
    )

@app.route("/admin/product/add", methods=["POST"])
def admin_add_product() -> Any:
    """Ajoute un produit (admin)."""
    user = get_current_user()
    if not user or not user.is_admin():
        flash("Accès refusé", "error")
        return redirect(url_for("index"))
    name = request.form.get("name", "")
    description = request.form.get("description", "")
    price = float(request.form.get("price", 0))
    image_url = request.form.get("image_url", "")
    category = request.form.get("category", "")
    stock = int(request.form.get("stock", 0))
    if not all([name, description, price, image_url, category]):
        flash("Tous les champs sont requis", "error")
        return redirect(url_for("admin_dashboard"))
    product = Product(
        id=0,  # Sera généré par la base de données
        name=name,
        description=description,
        price=price,
        image_url=image_url,
        category=category,
        stock=stock,
    )
    db.add_product(product)
    flash(f"Produit {name} ajouté avec succès !", "success")
    return redirect(url_for("admin_dashboard"))

if __name__ == "__main__":
    app.run(debug=True, port=5001)
