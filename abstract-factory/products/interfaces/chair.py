# pylint: disable=too-few-public-methods
"""
    Abstract Chair Product
"""

from abc import ABC, abstractmethod


class AbstractChair(ABC):
    """ Abstract Product """

    @abstractmethod
    def useful_chair_method(self) -> None:
        """ A special chair method. """
