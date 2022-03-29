# pylint: disable=too-few-public-methods
"""
    Abstract Sofa Product
"""

from abc import ABC, abstractmethod


class AbstractSofa(ABC):
    """ Abstract Product """

    @abstractmethod
    def useful_sofa_method(self) -> None:
        """ A special sofa method. """
