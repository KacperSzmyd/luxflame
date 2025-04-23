from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask import redirect, url_for, request, session
from .models import Product, Order, OrderItem, GalleryImage
from . import db


class SecureModelView(ModelView):
    def is_accessible(self):
        return session.get("admin_logged_in")

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("main.admin_login"))


class OrderView(SecureModelView):
    column_list = [
        "id",
        "customer_first_name",
        "customer_last_name",
        "company_name",
        "company_nip",
        "items",
        "street",
        "postal_code",
        "email",
        "phone",
        "notes",
        "created_at",
    ]


class OrderItemView(SecureModelView):
    column_list = ["id", "order_id", "product_id", "quantity"]


def init_admin(app):
    admin = Admin(app, name="Panel Administracyjny", template_mode="bootstrap4")
    admin.add_view(SecureModelView(Product, db.session))
    admin.add_view(OrderView(Order, db.session))
    admin.add_view(OrderItemView(OrderItem, db.session))
    admin.add_view(SecureModelView(GalleryImage, db.session))
