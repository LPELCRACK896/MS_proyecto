from typing import List


class Vehicle:

    car_id: int
    acceleration: float
    reaction_delay: float
    max_velocity: float
    current_velocity: float
    size: float

    def __init__(self, car_id: int, acceleration: float, next_road_target):
        self.car_id = car_id
        self.acceleration = acceleration

        self.next_road_target = next_road_target

    def go(self, space_ahead: float):
        pass

