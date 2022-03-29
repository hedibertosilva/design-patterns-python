# pylint: disable=import-error
"""
    Adapter Class
"""
from typing import Dict
from typing import List
from sensors.interfaces.sensors import Sensor


class HumidityAdapter(Sensor):
    """ Humidity Adapter

        The objective is to return the data in a format
        compatible with the system.
    """

    _sensor = None

    def __init__(self, sensor) -> None:
        self._sensor = sensor

    def get_data(self) -> List[str]:
        """ Getting data from Humidity Instance

        Returns:
            List[str]: data splited.
        """
        return self._sensor.get_csv().splitlines()

    def get_results(self) -> Dict[str, int]:
        """ Returns data from Humidity Instance

        Returns:
            Dict[str, int]: JSON format.
        """
        data_json = {}
        for index, row in enumerate(self.get_data()):
            if index == 0:
                continue
            key = row.split(',')[0].strip()
            value = int(row.split(',')[1].strip())
            data_json[key] = value
        return data_json
