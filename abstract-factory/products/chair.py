"""
    Concrete Chair Product
"""

from products.interfaces.chair import AbstractChair


class ChairArtDeco(AbstractChair):
    """ Concrete Product """

    def useful_chair_method(self) -> None:
        return None

    @staticmethod
    def make() -> None:
        """" Create the product. """
        print("Art Deco Chair Created!")


class ChairModern(AbstractChair):
    """ Concrete Product """

    def useful_chair_method(self) -> None:
        return None

    @staticmethod
    def make() -> None:
        """" Create the product. """
        print("Modern Chair Created!")


class ChairVictorian(AbstractChair):
    """ Concrete Product """

    def useful_chair_method(self) -> None:
        return None

    @staticmethod
    def make() -> None:
        """" Create the product. """
        print("Victorian Chair Created!")
