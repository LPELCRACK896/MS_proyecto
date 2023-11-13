from typing import List

from Vehicle import Vehicle
from IWay import IWay
from IEndRoad import IEndRoad


class Road(IWay, IEndRoad):

    line: List[Vehicle]

    inputs: List[IWay]  # List of Roads
    outputs: List[IEndRoad]  # List of Roads or
    length: float  # Meters
    stress: float

    is_special_road: bool

    def __init__(self, length: float):
        pass

    def connect_some_output(self, road):
        pass

    def connect_some_input(self, road):
        pass

    def receive_next_car(self):
        pass

    def get_next_in_line(self):
        """
        Called by some other Road that has this road as input
        :return:
        """
        pass



