from enum import Enum
from abc import ABC, abstractmethod

class TRAFFIC_LIGHT(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3



class Observer(ABC):

    @abstractmethod
    def update(self, traffic_light):
        pass


class Subject(ABC):

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Road(Observer):


    def __init__(self,road_id,name):
        self.__id = road_id
        self.__name = name
        self.__traffic_light = None

    def set_traffic_light(self, traffic_light):
        self.__traffic_light = traffic_light

    def get_traffic_light(self):
        return self.__traffic_light

    def update(self, traffic_light):
        traffic_light.show_light()
        traffic_light.change()  