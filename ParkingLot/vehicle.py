from typing import Tuple, TYPE_CHECKING
from utils.vehicleType import VehicleType
from spots import ParkingSpot

if TYPE_CHECKING:
    from levels import ParkingLevel



class Vehicle:
    
    def __init__(self,vehicle_type:VehicleType,number:str):
        self._vehicle_type = vehicle_type
        self._number = number
        self._spot = None
        self._level = None
        
    def park(self, spot:ParkingSpot,level:'ParkingLevel'):
        self._spot = spot
        self._level = level
        print(f'Vehicle  {self._number} parked at {self._spot.getId()}')
        
    def is_parked(self):
        return self._spot is not None
    
    def get_vehicle_type(self):
        return self._vehicle_type
    
    def unPark(self) -> Tuple[ParkingSpot,'ParkingLevel']:
        
        parking_spot = self._spot
        parking_level = self._level
        self._spot = None
        self._level = None
        return parking_spot, parking_level
        
    