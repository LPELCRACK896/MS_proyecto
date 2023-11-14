from typing import List

from IEndRoad import IEndRoad
from IWay import IWay
from Road import Road
from Vehicle import Vehicle
from EndRoad import EndRoad
from InputWay import InputWay
from TrafficLight import TrafficLight


class Map:
    name: str
    roads: List[Road]
    road_ends: List[EndRoad]
    road_inputs: List[InputWay]
    traffic_lights: List[TrafficLight]

    def __init__(self, name, roads: list, road_ends: list, road_inputs):
        self.name = name
        self.roads = roads
        self.road_inputs = road_inputs
        self.road_ends = road_ends

    def connect_roads(self, road_start: IWay, road_end: IEndRoad):
        pass

    def disconnect_roads(self, road_start: IWay, road_end: IEndRoad):
        pass

    def vehicle_join_road(self, vehicle: Vehicle, road: Road):
        pass

