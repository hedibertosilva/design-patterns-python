"""
    Extended Abstraction.
"""
from .interfaces.shapes import Shapes


class Circle(Shapes):
    """ Circle shape. """
    _radius: int

    def set_radius(self, radius: int) -> None:
        """Set radius parameter.

        Args:
            radius (int): needed to calculate anything.
        """
        self._radius = radius

    def get_radius(self) -> None:
        """ Get calculated radius. """

    def get_area(self) -> None:
        """ Get calculated area. """

    def get_circumference(self) -> None:
        """ Get calculated circumference. """

    def get_diameter(self) -> None:
        """ Get calculated diameter. """
