from abc import ABC, abstractmethod


class IWay(ABC):

    @abstractmethod
    def connect_some_output(self, road):
        pass

    @abstractmethod
    def get_next_in_line(self):
        """
        Called by some other Road that has this road as input
        :return:
        """
        pass


