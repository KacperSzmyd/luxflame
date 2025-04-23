from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for,
    request,
    flash,
    send_from_directory,
)
from .models import Product, Order, OrderItem, GalleryImage
from app import db

main = Blueprint("main", __name__)


@main.route("/robots.txt")
def robots():
    return send_from_directory("static", "robots.txt")


@main.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/gallery")
def gallery():
    images = GalleryImage.query.all()
    return render_template("gallery.html", images=images)


@main.route("/terms")
def terms():
    return render_template("terms.html")


@main.route("/contact")
def contact():
    return render_template("contact.html")


@main.route("/product/<int:product_id>", methods=["POST", "GET"])
def product_details(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == "POST":
        quatnity = int(request.form.get("quantity", 1))
        cart = session.get("cart", [])

        for item in cart:
            if item["product_id"] == product_id:
                item["quantity"] += quatnity
                break
        else:
            cart.append({"product_id": product_id, "quantity": quatnity})

        session["cart"] = cart
        session.modified = True

        flash("Dodano do koszyka.")
        return redirect(url_for("main.index"))

    return render_template("product.html", product=product)


@main.route("/add-to-cart/<int:product_id>", methods=["POST"])
def add_to_cart(product_id):
    cart = session.get("cart", [])
    quantity = int(request.form.get("quantity", 1))

    for item in cart:
        if item["product_id"] == product_id:
            item["quantity"] += quantity
            break
    else:
        cart.append({"product_id": product_id, "quantity": quantity})

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("main.index"))


@main.route("/cart")
def cart():
    cart = session.get("cart", [])
    products = []

    for item in cart:
        product = Product.query.get(item["product_id"])
        if product:
            products.append(
                {
                    "product": product,
                    "quantity": item["quantity"],
                    "subtotal": round(product.price * item["quantity"], 2),
                }
            )

    total = round(sum([p["subtotal"] for p in products]), 2)

    return render_template("cart.html", products=products, total=total)


@main.route("/update-cart/<int:product_id>/<action>", methods=["POST"])
def update_cart(product_id, action):
    cart = session.get("cart", [])

    for item in cart:
        if item["product_id"] == product_id:
            if action == "increase":
                item["quantity"] += 1
            elif action == "decrease":
                item["quantity"] = max(1, item["quantity"] - 1)
            break

    session["cart"] = cart
    session.modified = True
    return redirect(url_for("main.cart"))


@main.route("/remove-from-cart/<int:product_id>", methods=["POST"])
def remove_from_cart(product_id):
    cart = session.get("cart", [])
    cart = [item for item in cart if item["product_id"] != product_id]

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("main.cart"))


@main.route("/order", methods=["POST", "GET"])
def order():
    cart = session.get("cart", [])
    if not cart:
        flash("Koszyk jest pusty!")
        return redirect(url_for("main.cart"))

    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        company_name = request.form.get("company_name")
        nip = request.form.get("nip")
        street = request.form.get("street")
        city = request.form.get("city")
        postal_code = request.form.get("postal_code")
        phone = request.form.get("phone")
        email = request.form.get("email")
        notes = request.form.get("notes")

        required_fields = [
            first_name,
            last_name,
            street,
            city,
            postal_code,
            phone,
            email,
        ]
        if not all(required_fields):
            flash("Wszystkie wymagane pola muszą być wypełnione.")
            return redirect(url_for("main.order"))

        new_order = Order(
            customer_first_name=first_name,
            customer_last_name=last_name,
            company_name=company_name or None,
            company_nip=nip or None,
            street=street,
            city=city,
            postal_code=postal_code,
            phone=phone,
            email=email,
            notes=notes or None,
        )
        db.session.add(new_order)
        db.session.commit()

        for item in cart:
            order_item = OrderItem(
                order_id=new_order.id,
                product_id=item["product_id"],
                quantity=item["quantity"],
            )
            db.session.add(order_item)
        db.session.commit()

        session.pop("cart", None)
        flash("Dziękujemy za zamówienie!")

        return redirect(url_for("main.index"))

    return render_template("order.html")


@main.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "password":
            session["admin_logged_in"] = True
            flash("Zalogowano pomyślnie!", "success")
            return redirect("/admin")

        flash("Nieprawidłowe dane logowania.", "danger")

    return render_template("admin_login.html")


@main.route("/admin/logout")
def admin_logout():
    session.pop("admin_logged_in", None)
    flash("Wylogowano pomyślnie.", "info")
    return redirect(url_for("main.admin_login"))
