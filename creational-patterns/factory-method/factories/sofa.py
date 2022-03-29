"""
    Concrete Factory Declaration.
"""

from products.sofa import Sofa
from products.interfaces.product import Product
from factories.interfaces.factory import Factory


class SofaFactory(Factory):
    """ Concrete Factory Sofa. """

    def setter(self) -> Product:
        """ Sets Factory Method.

        Returns:
            Product: concrete product.
        """
        product = Sofa()
        product.set_color(self._color)
        return product
