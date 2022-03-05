"""
    Concrete Modern Factory
"""

from factories.interfaces.factory import Factory
from products.chair import ChairModern
from products.sofa import SofaModern


class ModernFactory(Factory):
    """ Concrete Factory """
    _product: str

    def __init__(self, product) -> None:
        self._product = product

    def setter(self) -> None:
        """ Defines what type of product must be returned. """

        products = {
            "chair": ChairModern,
            "sofa": SofaModern
        }

        return products[self._product]
