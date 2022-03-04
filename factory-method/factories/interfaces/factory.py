"""
    Factory Interface Declaration.
"""

from abc import ABC, abstractmethod
from products.interfaces.product import Product


class Factory(ABC):
    """ Abstract Factory. """
    _color: str

    def __init__(self, color: str = "Black") -> None:
        self._color = color

    @abstractmethod
    def setter(self) -> None:
        """ Set factory method. """

    def buy(self) -> Product:
        """ Build the product.

        Returns:
            Product: concrete product.
        """
        product = self.setter()
        product.make()
        return product
