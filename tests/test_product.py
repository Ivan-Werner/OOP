

from src.product import Product


def test_product_init(product):
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8


def test_product_added():
    product = Product("Smartphone", "Phone", 100.50, 2)
    product.name = "Smartphone"
    product.description = "Phone"
    product.price = 100.50
    product.quantity = 2


def test_product_update(capsys, product):
    product.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_str(product):
    assert str(product) == "Iphone 15, 210000.0 руб. : 8шт."


def test_product_add(product_with_price_1, product_with_price_2):
    assert product_with_price_1 + product_with_price_2 == 2580000.0

