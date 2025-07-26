from spots import ParkingSpot
from utils.utility import generate_id
from utils.vehicleType import VehicleType


class ParkingLevel:
    
    def __init__(self, spots:list[ParkingSpot]):
        self._spots = spots
        # generate level id
        self._level_id = generate_id("LEVEL")
        self._occupied_spots = 0
        
    def set_name(self, name):
        self.name = name
        
    def get_total_spots(self):
        return len(self._spots)
    
    def getId(self):
        return self._level_id
    
    def get_available_spots(self):
        return len(self._spots) - self._occupied_spots
    
    def increase_occupied_spots(self):
        self._occupied_spots += 1
        
    def decrease_occupied_spots(self):
        self._occupied_spots -= 1
        
    def getSpot(self,vehicle_type:VehicleType):
        for spot in self._spots:
            if spot.isAvailable() and spot.get_vehicle_type() == vehicle_type :
                return spot
        return None
        
        
    
        
    
    