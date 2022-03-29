"""
    Generic Test.
"""
from database import Database


def call_db_from_another_file():
    """ Testing if the create a new id calling from another file. """
    return Database()
