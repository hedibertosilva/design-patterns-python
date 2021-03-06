"""
    Concrete Victorian Factory
"""

from factories.interfaces.factory import AbstractFactory
from products.chair import ChairVictorian
from products.sofa import SofaVictorian


class VictorianFactory(AbstractFactory):
    """ Concrete Factory """
    _product: str

    def __init__(self, product) -> None:
        self._product = product

    def setter(self) -> None:
        """ Defines what type of product must be returned. """

        products = {
            "chair": ChairVictorian,
            "sofa": SofaVictorian
        }

        return products[self._product]
