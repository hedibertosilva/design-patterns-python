#!/usr/bin/env python3
"""
    Design Pattern: Factory Method

    Autor: Hediberto C. Silva
    E-mail: hed.cavalcante@gmail.com
"""
from database import Database
from another_file import call_db_from_another_file


def main():
    """ Initializer """
    db_1 = Database()
    db_2 = Database()
    db_3 = call_db_from_another_file()

    if id(db_1) == id(db_2) == id(db_3):
        print("Singleton works!")
    else:
        print("Singleton failed!")


if __name__ == '__main__':
    raise SystemExit(main())
