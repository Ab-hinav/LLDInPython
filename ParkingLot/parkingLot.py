from typing import Optional, Tuple
from levels import ParkingLevel
from spots import ParkingSpot
from utils.observer import Observer
from vehicle import Vehicle
from utils.singleton import SingleTonMeta


class ParkingLot(metaclass=SingleTonMeta):
    
    def add_observer(self, observer:Observer):
        self._observers.append(observer)
        
    
    def __init__(self,name,levels:list[ParkingLevel]):
        self._name = name
        self._levels = levels
        self._observers:list[Observer] = []
        self._total_spots = sum([level.get_total_spots() for level in levels])
        self._occupied_spots = 0
        

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def getParkingSpot(self, vehicle:Vehicle) -> Optional[Tuple[ParkingSpot, ParkingLevel]]:
        
        for level in self._levels:
            spot = level.getSpot(vehicle.get_vehicle_type())
            if spot:
                return spot,level
    
    def notify(self, message=""):
        if not message.strip():
            message = f"{self._name} parking lot has now {self._occupied_spots} spots left out of {self._total_spots}"
        for observer in self._observers:
            observer.update(message)
            
    def assignParkingSpot(self,vehicle:Vehicle):
        result = self.getParkingSpot(vehicle)
        print(result)
        if result:
            spot,level = result
            spot.park(vehicle)
            vehicle.park(spot,level)
            level.increase_occupied_spots()
            self._occupied_spots += 1
            self.notify()
            return True
        
        return False
    
    
    def releaseParkingSpot(self, vehicle:Vehicle):
        
        if vehicle.is_parked():
            spot,level = vehicle.unPark()
            spot.remove()
            level.decrease_occupied_spots()
            self._occupied_spots -= 1
            self.notify()
            
            return True
            

        return False
            
            
            
    
    
    
    