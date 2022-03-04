"""
    Concrete Factory Declaration.
"""

from products.chair import Chair
from products.interfaces.product import Product
from factories.interfaces.factory import Factory


class ChairFactory(Factory):
    """ Concrete Factory Chair. """

    def setter(self) -> Product:
        """ Sets Factory Method.

        Returns:
            Product: concrete product.
        """
        product = Chair()
        product.set_color(self._color)
        return product
