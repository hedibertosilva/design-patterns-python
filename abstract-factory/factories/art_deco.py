"""
    Concrete Art Deco Factory
"""

from factories.interfaces.factory import Factory
from products.chair import ChairArtDeco
from products.sofa import SofaArtDeco


class ArtDecoFactory(Factory):
    """ Concrete Factory """
    _product: str

    def __init__(self, product) -> None:
        self._product = product

    def setter(self) -> None:
        """ Defines what type of product must be returned. """

        products = {
            "chair": ChairArtDeco,
            "sofa": SofaArtDeco
        }

        return products[self._product]
