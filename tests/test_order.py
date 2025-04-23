def test_order_flow(client):
    client.post("/add-to-cart/1", data={"quantity": 1})

    response = client.post(
        "/order",
        data={
            "first_name": "Jan",
            "last_name": "Kowalski",
            "street": "Testowa 1",
            "city": "Miasto",
            "postal_code": "00-001",
            "phone": "123456789",
            "email": "jan@kowalski.pl",
        },
        follow_redirects=True,
    )

    assert b"Dzi\xc4\x99kujemy" in response.data


def test_order_quantity(client, app):
    client.post("/add-to-cart/1", data={"quantity": 3}, follow_redirects=True)

    response = client.post(
        "/order",
        data={
            "first_name": "Anna",
            "last_name": "Nowak",
            "street": "Testowa 12",
            "city": "Miasto",
            "postal_code": "00-000",
            "phone": "123456789",
            "email": "anna@nowak.pl",
        },
        follow_redirects=True,
    )

    assert b"Dzi" in response.data

    with app.app_context():
        from app.models import OrderItem

        item = OrderItem.query.first()
        assert item is not None
        assert item.quantity == 3
