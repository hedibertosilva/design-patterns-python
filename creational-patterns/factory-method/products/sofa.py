# pylint: disable=no-self-use
"""
    Concrete Product Declaration.
"""

from .interfaces.product import Product


class Sofa(Product):
    """ Concrete Product Sofa. """
    _configurations = {}

    def set_color(self, color: str) -> None:
        """ Sets the product color.

        Args:
            color (str): color in hex format.

        """
        self._configurations['color'] = color

    def make(self) -> None:
        """ Returns the created product. """
        print(f"{self._configurations['color']} Sofa created!")
