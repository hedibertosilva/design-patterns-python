#! /usr/local/env python3
"""
    Design Pattern: Bridge Method

    Autor: Hediberto C. Silva
    E-mail: hed.cavalcante@gmail.com
"""
from shapes.interfaces.shapes import Shapes
from shapes.circle import Circle
from shapes.square import Square
from colors.blue import Blue
from colors.red import Red


def show_color(shape: Shapes) -> None:
    """Show shape color.

    Args:
        shape (Shapes): custom shape.
    """
    shape.show_color()


def main() -> None:
    """ Application """

    circle_blue = Circle(color=Blue())
    square_blue = Square(color=Blue())
    circle_red = Circle(color=Red())
    square_red = Square(color=Red())

    show_color(circle_blue)
    show_color(square_blue)
    show_color(circle_red)
    show_color(square_red)


if __name__ == '__main__':
    raise SystemExit(main())
