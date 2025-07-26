from typing import  TYPE_CHECKING
from utils.utility import generate_id
from utils.vehicleType import VehicleType

if TYPE_CHECKING:
    from vehicle import Vehicle


class ParkingSpot:
    
    def __init__(self, vehicle_type:VehicleType):
        self._id = generate_id("SPOT")
        self.is_available = True
        self._vehicle_type = vehicle_type
        self._vehicle = None
        
    def get_vehicle(self):
        return self._vehicle
    
    def get_vehicle_type(self):
        return self._vehicle_type 
        
    def park(self, vehicle:'Vehicle'):
        
        if not self.is_available:
            raise Exception("Spot is not available")
        
        if vehicle.get_vehicle_type() != self._vehicle_type:
            raise Exception("Vehicle type does not match")
        
        self.is_available = False
        self._vehicle = vehicle
        self._vehicle_type = vehicle.get_vehicle_type()
        print(f"Vehicle {vehicle._number} parked at spot {self._id}")
        return True
        
    def remove(self):
        self.is_available = True
        self.vehicle = None
        
        return True
    
    def isAvailable(self):
        return self.is_available
    
    def getId(self):
        return self._id
        
    