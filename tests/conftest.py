import pytest
from app import create_app, db
from app.models import Product


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        {
            "TESTING": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
            "WTF_CSRF_ENABLED": False,
            "SECRET_KEY": "test",
        }
    )

    with app.app_context():
        db.create_all()
        product = Product(
            name="test product",
            price=123.45,
            description="test description 12345",
            image_filename="test.jpg",
        )
        db.session.add(product)
        db.session.commit()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()
