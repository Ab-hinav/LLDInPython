
from util import TRAFFIC_LIGHT,Subject

class TrafficLight(Subject):

    def __init__(self):
        self.__duration ={
            TRAFFIC_LIGHT.RED: 10,
            TRAFFIC_LIGHT.YELLOW: 2,
            TRAFFIC_LIGHT.GREEN: 5
        }
        self.__colorsequence = [TRAFFIC_LIGHT.RED, TRAFFIC_LIGHT.YELLOW, TRAFFIC_LIGHT.GREEN]
        self.__current_color = 0
        self.__roads=[]

    def register_observer(self, road):
        self.__roads.append(road)

    def remove_observer(self,road):
        for sroad in self.__roads:
            if sroad.get_id() == road.get_id():
                self.__roads.remove(sroad)
                break

    def show_light(self):
        print(f'${self.__colorsequence[self.__current_color]} for duration ${self.__duration[self.__current_color]}')
        
    def notify_observers(self):
        for road in self.__roads:
            road.update(self)

    def add_color(self, color,duration):
        self.__colorsequence.append(color)
        self.__duration[color] = duration

    def change(self):
        self.__current_color += 1
        self.__current_color %= len(self.__colorsequence)

    def change_duration(self, color, duration):
        self.__duration[color] = duration

