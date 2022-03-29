# pylint: disable=too-few-public-methods
"""
    Sensor Interface
"""
import json

from abc import ABC, abstractmethod
from typing import Dict


class Sensor(ABC):
    """ Abstract Interface. """

    @abstractmethod
    def get_data(self) -> str:
        """ Read data from the source file. """

    def get_results(self) -> Dict[str, int]:
        """ Returns data collected by the sensor.

        Returns:
            Dict[str, int]: JSON format.
        """
        data = self.get_data()
        return json.loads(data)
