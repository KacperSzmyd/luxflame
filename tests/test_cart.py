def test_empty_cart(client):
    response = client.get("/cart")
    assert b"Koszyk jest pusty" in response.data


def test_add_to_cart(client):
    client.post("/add-to-cart/1", data={"quantity": 2})

    response = client.get("/cart")

    assert b"test product" in response.data
    assert b"Ilo" in response.data
    assert b"2" in response.data


def test_remove_from_cart(client):
    client.post("/add-to-cart/1", data={"quantity": 2})
    response = client.post("/remove-from-cart/1", follow_redirects=True)
    assert b"Koszyk jest pusty" in response.data


def test_cart_quantity_change(client):
    client.post("/add-to-cart/1", data={"quantity": 2})
    client.get("/cart/increase/1")
    client.get("/cart/decrease/1")
    response = client.get("/cart")
    assert b"Ilo" in response.data
    assert b"2" in response.data
