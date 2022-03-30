"""
    Extended Abstraction.
"""
from .interfaces.shapes import Shapes


class Square(Shapes):
    """ Square Shape. """
    _side_length: int

    def set_side(self, side_length: int) -> None:
        """Set side length.

        Args:
            side_length (int): needed to calculate anything.
        """
        self._side_length = side_length

    def get_area(self) -> None:
        """ Get calculated area. """

    def get_perimeter(self) -> None:
        """ Get calculated perimeter. """

    def get_diagonal(self) -> None:
        """ Get calculated diagonal. """
