#!/usr/bin/env python3
"""
    Design Pattern: Factory Method

    Autor: Hediberto C. Silva
    E-mail: hed.cavalcante@gmail.com
"""

from products.interfaces.product import Product
from factories.interfaces.factory import Factory
from factories.chair import ChairFactory
from factories.sofa import SofaFactory


def decorate(factory: Factory) -> Product:
    """ Returns a built product.

    Args:
        factory (Factory): concrete creator class.

    Returns:
        Product: concrete product class.
    """
    return factory.buy()


def main() -> None:
    """ Initializer Method. """
    chair = ChairFactory(color="Red")
    sofa = SofaFactory(color="Gray")

    decorate(chair)
    decorate(sofa)


if __name__ == '__main__':
    main()
