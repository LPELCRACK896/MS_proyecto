from typing import List
from IWay import IWay
from Vehicle import Vehicle
from VehiclesFactory import VehiclesFactory

import random
from datetime import datetime as dt

DIAS_LABORALES = range(0, 5)  # Lunes(0) a Viernes(4)

LAMBDA_LLEGADA_PICO = 40
LAMBDA_LLEGADA_NORMAL = 30
LAMBDA_LLEGADA_BAJA = 20


class InputWay(IWay):

    name: str
    frequency: int
    car_rate: list
    queue: List[Vehicle]
    outputs: list

    lambda_llegada: float
    vehicles_factory: VehiclesFactory

    def __init__(self, name: str, lambda_llegada: float, vehicles_factory: VehiclesFactory):
        self.name = name
        self.lambda_llegada = lambda_llegada
        self.vehicles_factory = vehicles_factory
        self.queue = []

    def calcular_tiempos_llegada(self, tiempo_simulacion):
        """
        Calcula los tiempos de llegada de los vehículos durante el período de simulación.
        :param tiempo_simulacion: Tiempo total de la simulación en minutos.
        :return: Lista de tiempos (en minutos) en los que los vehículos llegan.
        """
        vehiculo_y_llegada = []
        tiempo_actual = 0
        total_carros = 0
        while tiempo_actual < tiempo_simulacion:
            tiempo_hasta_proximo = random.expovariate(self.lambda_llegada)
            tiempo_actual += tiempo_hasta_proximo
            if tiempo_actual < tiempo_simulacion:
                total_carros += 1
                print(f"Carros actuales: {total_carros}")
                vehiculo_y_llegada.append((self.vehicles_factory.get_a_car(), tiempo_actual))

        return vehiculo_y_llegada

    def connect_some_output(self, road):
        pass


    def get_next_in_line(self):
        """
        Called by some other Road that has this road as input
        Since this isn't a road it
        :return:
        """
        pass