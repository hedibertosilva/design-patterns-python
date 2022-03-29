"""
    Concrete Product Declaration.
"""

from .interfaces.product import Product


class Chair(Product):
    """ Concrete Product Sofa. """
    _configurations = {}

    def set_color(self, color: str) -> None:
        """ Set product color.

        Args:
            color (str).

        """
        self._configurations['color'] = color

    def make(self) -> None:
        """ Returns the created product. """
        print(f"{self._configurations['color']} Chair created!")
