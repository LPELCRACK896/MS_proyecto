from abc import ABC, abstractmethod


class IEndRoad(ABC):

    @abstractmethod
    def connect_some_input(self, road):
        pass

    @abstractmethod
    def receive_next_car(self):
        pass
