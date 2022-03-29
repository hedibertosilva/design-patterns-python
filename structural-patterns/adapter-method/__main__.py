#! /usr/local/env python3
"""
    Design Pattern: Adapter Method

    Autor: Hediberto C. Silva
    E-mail: hed.cavalcante@gmail.com
"""
from sensors.libraries.humidity import Humidity
from sensors.temperature import Temperature
from sensors.plugins.humidity_adapter import HumidityAdapter
from sensors.interfaces.sensors import Sensor


def read_sensor(sensor: Sensor) -> None:
    """ Show the sensor data collected.

        The sensor reader only accepts JSON Format.

    Args:
        sensor (Sensor): Sensor Instance
    """
    print(sensor.get_results())


def main() -> None:
    """ Application """
    humidity = HumidityAdapter(Humidity())
    temperature = Temperature()
    read_sensor(humidity)
    read_sensor(temperature)


if __name__ == '__main__':
    raise SystemExit(main())
