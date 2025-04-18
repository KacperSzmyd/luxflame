from flask import Blueprint, render_template, session, redirect, url_for
from .models import Product

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
