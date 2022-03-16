"""
    Concrete Product
"""


class ConcreteCar:
    """ Concrete Car. """

    def __init__(self) -> None:
        self._parts = []

    def add(self, part) -> None:
        """ Add new part to the car. """
        self._parts.append(part)

    def list_parts(self) -> str:
        """ Show all parts into the car. """
        print(f"Products parts -> {','.join(self._parts)}.", end="\n")
