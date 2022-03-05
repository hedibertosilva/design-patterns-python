"""
    Abstract Factory
"""

from abc import ABC, abstractmethod


class Factory(ABC):
    """ Abstract Factory """

    @abstractmethod
    def setter(self) -> None:
        """ Factory Method """

    def create_product(self) -> None:
        """ Create the product defined by setter method. """
        product = self.setter()
        product.make()
        return product
