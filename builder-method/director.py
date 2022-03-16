"""
    The Director.

    It controls all processes to build the concrete builder.
"""


class Director:
    """
        Offer all options available.
    """
    product: str

    def make_sports_car(self):
        """ Step-by-step how to factory a sports car. """
        self.product.set_seat(2)
        self.product.set_engine("Sport")

    def make_suv_car(self):
        """ Step-by-step how to factory a SUB car. """
        self.product.set_seat(4)
        self.product.set_engine("Manual")
        self.product.set_gps()
