"""
    Concrete Sofa Product
"""

from products.interfaces.sofa import AbstractSofa


class SofaArtDeco(AbstractSofa):
    """ Concrete Product """

    def useful_sofa_method(self) -> None:
        return None

    @staticmethod
    def make() -> None:
        """" Create the product. """
        print("Art Deco Sofa Created!")


class SofaModern(AbstractSofa):
    """ Concrete Product """

    def useful_sofa_method(self) -> None:
        return None

    @staticmethod
    def make() -> None:
        """" Create the product. """
        print("Modern Sofa Created!")


class SofaVictorian(AbstractSofa):
    """ Concrete Product """

    def useful_sofa_method(self) -> None:
        return None

    @staticmethod
    def make() -> None:
        """" Create the product. """
        print("Victorian Sofa Created!")
