# pylint: disable=import-error
"""
    Concrete Builder
"""
from products.car import ConcreteCar
from builders.interfaces.builder import Builder


class BuilderCar(Builder):
    """ Concrete Builder """

    def __init__(self) -> None:
        self.car = self.reset()

    @staticmethod
    def reset() -> Builder:
        """ Returns a new Concrete Product.

        Returns:
            Builder: Concrete Product
        """
        return ConcreteCar()

    def set_seat(self, number: int) -> None:
        """ Set the number of seats. """
        self.car.add(f"sets: {number}")

    def set_engine(self, engine: str) -> None:
        """ Set the engine type. """
        self.car.add(f"engine type: {engine}")

    def set_gps(self) -> None:
        """ Enable GPS. """
        self.car.add("GPS enabled")

    def get_result(self) -> None:
        """ Show parts included in the car. """
        self.car.list_parts()
