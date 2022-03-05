# pylint: disable=no-self-use
"""
    Abstract Chair Product
"""

from abc import ABC, abstractmethod


class AbstractChair(ABC):
    """ Abstract Product """

    @abstractmethod
    def useful_chair_method(self) -> None:
        """ A special chair method. """

    def make(self) -> None:
        """" Create the product. """
        print("Chair created!")
