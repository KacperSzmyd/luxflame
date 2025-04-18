from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from .models import Product, Order, OrderItem
from app import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    products = Product.query.all()
    return render_template("index.html", products=products)


@main.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", [])

    # checking if item is already in cart
    for item in cart:
        if item["product_id"] == product_id:
            item["quantity"] += 1
            break
    else:
        cart.append({"product_id": product_id, "quantity": 1})

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


@main.route("/order", methods=["POST", "GET"])
def order():
    cart = session.get("cart", [])
    if not cart:
        flash("Koszyk jest pusty!")
        return redirect(url_for("main.cart"))

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        address = request.form.get("address")

        if not name or not email or not address:
            flash("Wszystkie pola są wymagane.")
            return redirect(url_for("main.order"))

        new_order = Order(
            customer_name=name, customer_email=email, customer_address=address
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
        flash("Dziekujemy za zamowienie!")

        return redirect(url_for("main.index"))
    return render_template("order.html")
