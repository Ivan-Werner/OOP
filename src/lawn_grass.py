from src.product import Product


class LawnGrass(Product):

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is self.__class__:
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


# if __name__ == '__main__':
#     grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
#     grass2 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
#
#     print(grass.name)
#     print(grass.description)
#     print(grass.price)
#     print(grass.quantity)
#     print(grass.country)
#     print(grass.germination_period)
#     print(grass.color)
#
#     print(grass + grass2)
