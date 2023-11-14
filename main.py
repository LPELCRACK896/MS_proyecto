from Vehicle import Vehicle
from Road import Road
from IWay import IWay
from IEndRoad import IEndRoad
from EndRoad import  EndRoad
import random
from InputWay import InputWay

from VehiclesFactory import VehiclesFactory
import simpy
import stats as st

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

"""
vehicle_factory = VehiclesFactory(name="global_factory")

start_road_per_car_der_norte = InputWay("START AUX PERIFERICO DERECHO", 10, vehicle_factory)
start_road_per_car_izq_norte = InputWay("START AUX PERIFERICO IZQUIERDO", 10, vehicle_factory)

road_per_car_der_norte = Road("AUX PERIFERICO CARRIL DERECHO NORTE", 904.4, 11.11, 1.5)  # 0
road_per_car_izq_norte = Road("AUX PERIFERICO CARRIL IZQUIERDO NORTE", 904.4, 11.11, 1.5)  # 1

end_road_perifer_car_der_sur = EndRoad()
end_road_perifer_car_izq_sur = EndRoad()

villa_linda_car_der = Road("BOULEVAR VILLA LINDA CARRIL DERECHO", 800.6, 16.67, 1.5)  # 5
villa_linda_car_izq = Road("BOULEVAR VILLA LINDA CARRIL IZQUIERDO", 800.6, 16.67, 1.5)  # 4

puente_car_izq = Road("PUENTE VILLA LINDA CARRIL IZQUIERDO", 107.03, 8.33, 1.5)  # 10
puente_car_der = Road("PUENTE VILLA LINDA CARRIL DERECHO", 107.03, 8.33, 1.5)  # 11

roads = [
    road_per_car_der_norte,
    road_per_car_izq_norte,

    villa_linda_car_izq,
    villa_linda_car_der,

    puente_car_izq,
    puente_car_der
]

"""


def vehicle_arrival_process(env, input_way, road, arrival_cars):
    """Proceso para la llegada de vehículos a la carretera."""

    for vehicle, arrival_time in arrival_cars:
        yield env.timeout(arrival_time)
        input_way.queue.append(vehicle)
        print(f"{MAGENTA} Vehículo {vehicle.car_id} llegó a la entrada {input_way.name} en el tiempo {env.now} {RESET}")
        env.process(try_enter_road(env, vehicle, road, input_way))


def try_enter_road(env, vehicle, road, input_way):
    """Intenta que un vehículo entre en la carretera si hay espacio."""
    while True:
        if road.space_left >= vehicle.size:
            road.receive_next_vehicle(vehicle)
            print(f"{GREEN} Vehículo {vehicle.car_id} entró a {road.name} en el tiempo {env.now} {RESET}")
            env.process(vehicle_transit_process(env, vehicle, road))
            break
        print(f"{RED} Vehículo {vehicle.car_id} NO entró a {road.name} para el tiempo {env.now} {RESET}")
        yield env.timeout(1)  # Reintentar después de un breve tiempo


def vehicle_transit_process(env, vehicle, road: Road):
    """Procesa el tránsito del vehículo a través de la carretera."""
    while road.traffic_light == "red" or not road.is_at_the_front(vehicle):
        yield env.timeout(1)  # Esperar si el semáforo está en rojo o el vehículo no está al frente
    road.pass_the_one_in_front()  # El vehículo sale de la carretera
    print(f"{BLUE} Vehículo {vehicle.car_id} salió de {road.name} en el tiempo {env.now} {RESET}")


def traffic_light_process(env, road, green_duration, red_duration):
    """Controla el semáforo al final de la carretera."""
    while True:
        road.set_traffic_light("green")
        yield env.timeout(green_duration)
        road.set_traffic_light("red")
        yield env.timeout(red_duration)


def main():
    vehicle_factory = VehiclesFactory(name="global_factory")
    env = simpy.Environment()
    input_way = InputWay("START AUX PERIFERICO DERECHO", 5, vehicle_factory)
    road = Road("AUX PERIFERICO CARRIL DERECHO NORTE", 904.4, 11.11, 1.5)

    simulation_time = 3600  # Duración de la simulación en segundos (2 horas)
    arrival_cars = input_way.calcular_tiempos_llegada(simulation_time)

    green_duration = 40  # Duración luz verde en segundos
    red_duration = 20  # Duración luz roja en segundos

    env.process(vehicle_arrival_process(env, input_way, road,  arrival_cars))
    env.process(traffic_light_process(env, road, green_duration, red_duration))

    env.run(until=simulation_time)


if __name__ == '__main__':
    main()

