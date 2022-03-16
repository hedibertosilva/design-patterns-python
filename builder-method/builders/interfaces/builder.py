"""
    Abstract Builder
"""


from abc import ABC, abstractmethod


class Builder(ABC):
    """ Builder Interface """

    @staticmethod
    @abstractmethod
    def reset() -> None:
        """ Returns a new concrete product. """

    @abstractmethod
    def get_result(self) -> None:
        """ Show parts included in the car. """
