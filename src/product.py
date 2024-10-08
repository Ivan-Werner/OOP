class Product:

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. : {self.quantity}шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            return (self.__price * self.quantity) + (other.__price * other.quantity)
        raise TypeError

    @classmethod
    def new_product(cls, product_dict: dict):
        return cls(**product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price


# if __name__ == '__main__':
#     product = Product("Smartphone", "Phone", 100.50, 2)
#     print(product.name)
#     print(product.description)
#     print(product.price)
#     print(product.quantity)
#
#     product2 = Product.new_product({"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#          "quantity": 5})
#     print(product2.name)
#     print(product2.description)
#     print(product2.price)
#     print(product2.quantity)
#
#     product2.price = -100
#     print(product2.price)
#     product2.price = 100
#     print(product2.price)
#
#     print(product + product2)
