from typing import List
from Vehicle import Vehicle
import stats as st
import scipy.stats as stats


class VehiclesFactory:
    name: str
    count: int
    vehicles: List[Vehicle]

    average_acceleration: float
    de_acceleration: float

    average_reaction_delay: float
    de_reaction_delay: float

    average_max_speed: float
    de_max_speed: float

    average_size: float
    de_size: float

    def __init__(self, name,
                 average_acceleration: float = 1, de_acceleration: float = 0.1,
                 average_reaction_delay: float = 2, de_reaction_delay: float = 0.5,
                 average_max_speed: float = 8, de_max_speed: float = 5,
                 average_size: float = 5, de_size: float = 2
                 ):
        self.name = name
        self.count = 0
        self.vehicles = []

        self.average_acceleration = average_acceleration
        self.de_acceleration = de_acceleration
        self.average_reaction_delay = average_reaction_delay
        self.de_reaction_delay = de_reaction_delay
        self.average_max_speed = average_max_speed
        self.de_max_speed = de_max_speed
        self.average_size = average_size
        self.de_size = de_size

    def get_a_car(self) -> Vehicle:
        acceleration = st.inverse_transform(stats.norm(self.average_acceleration, self.de_acceleration), 1)[0]  # Ejemplo: distribución normal con media 1 y desviación 0.2
        reaction_delay = st.inverse_transform(stats.norm(self.average_reaction_delay, self.de_reaction_delay), 1)[0]  # Ejemplo: distribución normal con media 2 y desviación 0.5
        max_speed = st.inverse_transform(stats.norm(self.average_max_speed, self.de_max_speed), 1)[0]  # Ejemplo: distribución normal con media 100 y desviación 10
        size = st.inverse_transform(stats.norm(self.average_size, self.de_size), 1)[0]  # Ejemplo: distribución normal con media 2 y desviación 0.3
        self.count += 1
        return Vehicle(self.count, acceleration, reaction_delay, max_speed, size)

