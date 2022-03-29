# pylint: disable=too-few-public-methods
"""
    Temperature Sensor
"""
from .interfaces.sensors import Sensor


class Temperature(Sensor):
    """ Extract temperature data """

    SOURCE_PATH = 'adapter-method/contents/temperature_data.json'
    SOURCE_ENCONDING = 'utf-8'

    def get_data(self) -> str:
        """ Read data from source.

        Returns:
            str: data in string format.
        """
        with open(self.SOURCE_PATH, encoding=self.SOURCE_ENCONDING) as file:
            return file.read()
