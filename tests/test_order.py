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
