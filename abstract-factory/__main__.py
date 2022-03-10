#!/usr/bin/env python3
"""
    Design Pattern: Abstract Factory

    Autor: Hediberto C. Silva
    E-mail: hed.cavalcante@gmail.com
"""

from factories.interfaces.factory import AbstractFactory
from factories.art_deco import ArtDecoFactory
from factories.modern import ModernFactory
from factories.victorian import VictorianFactory


def decorate(factory: AbstractFactory):
    """ Returns a built product.

    Args:
        factory (Factory): abstract factory.

    Returns:
        Product: concrete product.
    """
    return factory.create_product()


def main():
    """ Inicialize the Application. """
    sofa_art_deco = ArtDecoFactory(product="sofa")
    chair_modern = ModernFactory(product="chair")
    chair_victorian = VictorianFactory(product="chair")

    decorate(sofa_art_deco)
    decorate(chair_modern)
    decorate(chair_victorian)


if __name__ == '__main__':
    main()
