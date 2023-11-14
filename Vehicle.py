from typing import List


class Vehicle:

    acceleration: float
    reaction_delay: float
    max_speed: float
    current_velocity: float
    size: float

    def __init__(self, car_id: int, acceleration: float, reaction_delay: float, max_speed: float, size: float):
        self.acceleration = acceleration
        self.reaction_delay = reaction_delay
        self.max_speed = max_speed
        self.size = size

        self.next_road_target = None
        self.current_velocity = max_speed/2

        self.car_id = car_id


    def set_next_road_target(self, next_road_target):
        self.next_road_target = next_road_target

    def go(self, space_ahead: float):
        pass

