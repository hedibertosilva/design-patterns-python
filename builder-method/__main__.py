#! /usr/local/env python3
"""
    Design Pattern: Builder Method

    Autor: Hediberto C. Silva
    E-mail: hed.cavalcante@gmail.com
"""
from director import Director
from builders.car import Car


def main() -> None:
    """ Initializer Method. """
    car_store = Director()
    car_a = Car()
    car_b = Car()
    car_c = Car()

    car_store.product = car_a
    car_store.make_sports_car()
    car_store.product.get_result()

    car_store.product = car_b
    car_store.make_suv_car()
    car_store.product.get_result()

    car_c.set_seat(7)
    car_c.set_engine("Normal")
    car_c.set_gps()
    car_c.get_result()


if __name__ == '__main__':
    main()
