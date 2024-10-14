from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс, родительский для классов продукции."""
    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
