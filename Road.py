from typing import List

from Vehicle import Vehicle
from IWay import IWay
from IEndRoad import IEndRoad


class Road(IWay, IEndRoad):

    name: str

    line: List[Vehicle]

    inputs: List[IWay]  # List of Roads
    outputs: List[IEndRoad]  # List of Roads or
    length: float  # Meters
    stress: float

    is_special_road: bool

    def __init__(self, name, length: float):
        self.name = name
        self.length = length

    def connect_some_output(self, road):
        pass

    def connect_some_input(self, road):
        pass

    def receive_next_vehicle(self):
        pass

    def get_next_in_line(self):
        """
        Called by some other Road that has this road as input
        :return:
        """
        pass



