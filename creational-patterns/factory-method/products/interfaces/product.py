"""
    Product Interface Declaration.
"""

from abc import ABC, abstractmethod


class Product(ABC):
    """ Abstract Product. """

    @abstractmethod
    def set_color(self, color: str) -> None:
        """Set color on product.

        Args:
            color (str): color in hex format.
        """

    def make(self) -> None:
        """Build the product."""
