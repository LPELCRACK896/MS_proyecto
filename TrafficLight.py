from typing import Tuple, List
from IWay import IWay
from IEndRoad import IEndRoad


class TrafficLight:
    states: List[Tuple[int, List[Tuple[IWay, IEndRoad]]]]

    allowed_connections: List[Tuple[IWay, IEndRoad]]
    time_left: int
    current_state_index: int

    def __init__(self, states):
        self.states = states
        self.timer = 0

        self.current_state_index = 0
        self.allowed_connections = states[0][1]
        self.time_left = states[0][0]

    def next_state(self):
        self.current_state_index = (self.current_state_index + 1) % len(self.states)
        self.allowed_connections = self.states[self.current_state_index][1]
        self.time_left = self.states[self.current_state_index][0]

    def tick(self):
        self.time_left -= 1
        if self.time_left == 0:
            self.next_state()
