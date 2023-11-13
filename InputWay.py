from typing import List
from IWay import IWay
from Vehicle import Vehicle


class InputWay(IWay):
    frequency: int
    car_rate: list
    queue: List[Vehicle]

    def a_second_goes(self):  # Change name
        """
        Using probability on simulation time decides to either add some car
        :return:
        """
        pass

    def get_next_in_line(self):
        """
        Called by some other Road that has this road as input
        Since this isn't a road it
        :return:
        """
        pass