"""
    Singleton Class.
"""
from meta.singleton import SingletonMeta


class Database(metaclass=SingletonMeta):
    """
        Database Singleton.
    """
    def connect(self):
        """ Any Useful Method. """

    def disconnect(self):
        """ Any Useful Method. """

    def query(self):
        """ Any Useful Method. """
