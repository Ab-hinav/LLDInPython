
from trafficLight import TrafficLight
from util import Road

class TrafficLightController:

    __instance = None
    __isInialized = False

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(TrafficLightController,cls).__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if self.__isInialized:
            return
        self.__isInialized = True
        self.traffic_lights = []

        for i in range(4):

            traffic_light = TrafficLight()
            road = Road('123','abdf')
            road.set_traffic_light(traffic_light)
            traffic_light.register_observer(road)
            self.traffic_lights.append(traffic_light)

    def start(self):
        for traffic_light in self.traffic_lights:
            traffic_light.notify_observers()
            print('\n')


