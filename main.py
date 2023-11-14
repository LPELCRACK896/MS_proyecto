from Vehicle import Vehicle
from Road import Road
from IWay import  IWay
from IEndRoad import IEndRoad

import simpy as sp
import stats as st

road_per_car_der_norte = Road("AUX PERIFERICO CARRIL DERECHO NORTE", 904.4)  # 0


road_per_car_izq_norte = Road("AUX PERIFERICO CARRIL IZQUIERDO NORTE", 904.4)  # 1

villa_linda_car_der = Road("BOULEVAR VILLA LINDA CARRIL DERECHO", 800.6)  # 5
villa_linda_car_izq = Road("BOULEVAR VILLA LINDA CARRIL IZQUIERDO", 800.6)  # 4

puente_car_izq = Road("PUENTE VILLA LINDA CARRIL IZQUIERDO", 107.03)  # 10
puente_car_der = Road("PUENTE VILLA LINDA CARRIL DERECHO", 107.03)  # 11

roads = [
    road_per_car_der_norte,
    road_per_car_izq_norte,

    villa_linda_car_izq,
    villa_linda_car_der,

    puente_car_izq,
    puente_car_der
]


def main():
    pass


if __name__ == '__main__':
    main()

