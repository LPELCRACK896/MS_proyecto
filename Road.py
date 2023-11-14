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
    limit_speed: float
    de_limit_speed: float

    traffic_light: str

    space_left: float

    def __init__(self, name, length: float, limit_speed:float, de_limit_speed: float):
        self.name = name
        self.length = length
        self.limit_speed = limit_speed
        self.de_limit_speed = de_limit_speed
        self.traffic_light = "red"
        self.space_left = length
        self.line = []

    def set_traffic_light(self, color):
        self.traffic_light = color

    def connect_some_output(self, road):
        self.outputs.append(road)

    def connect_some_input(self, road):
        self.inputs.append(road)

    def receive_next_vehicle(self, vehicle: Vehicle):
        if vehicle.size <= self.space_left:
            self.line.append(vehicle)
            self.space_left -= vehicle.size
            return True
        return False

    def pass_the_one_in_front(self):
        self.space_left += self.line[0].size
        self.line.pop(0)

    def get_next_in_line(self):
        pass

    def is_at_the_front(self, vehicle):
        return vehicle == self.line[0]



