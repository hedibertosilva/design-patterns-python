# pylint: disable=too-few-public-methods
"""
    Abstract Implementation.
"""
from abc import ABC


class Colors(ABC):
    """ Colors Interface. """
    _color: str

    def __repr__(self):
        return self._color
