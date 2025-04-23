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

def init_admin(app):
    admin = Admin(app, name="Panel Administracyjny", template_mode="bootstrap4")
    admin.add_view(SecureModelView(Product, db.session))
    admin.add_view(SecureModelView(Order, db.session))
    admin.add_view(SecureModelView(OrderItem, db.session))
    admin.add_view(SecureModelView(GalleryImage, db.session))