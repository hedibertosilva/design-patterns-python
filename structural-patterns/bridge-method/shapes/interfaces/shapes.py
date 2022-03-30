# pylint: disable=too-few-public-methods
"""
    Abstract Interface.
"""
from abc import ABC


class Shapes(ABC):
    """ Shapes Interface. """
    _color = ""

    def __init__(self, color: str) -> None:
        """Settings default parameters.

        Args:
            color (str): color concrete object.
        """
        self._color = color

    def show_color(self) -> None:
        """ Show the type of shape and its color. """
        print(f'{type(self).__name__} {self._color}')
