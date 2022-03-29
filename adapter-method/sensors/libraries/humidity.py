"""
    Humidity Sensor
"""


class Humidity:
    """ 3rd-party library. """

    SOURCE_PATH = 'adapter-method/contents/humidity_data.csv'
    SOURCE_ENCONDING = 'utf-8'

    def get_data(self) -> str:
        """ Load data from source.

        Returns:
            str: csv data in string format.
        """
        with open(self.SOURCE_PATH, encoding=self.SOURCE_ENCONDING) as file:
            return file.read()

    def get_csv(self) -> str:
        """ Returns data in CSV format.

        Returns:
            str: CSV Format.
        """
        return self.get_data()
