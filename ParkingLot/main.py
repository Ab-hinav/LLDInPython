from parkingLot import ParkingLot
from levels import ParkingLevel
from vehicle import Vehicle
from spots import ParkingSpot
from utils.vehicleType import VehicleType


if __name__ == '__main__':
    
    no_of_levels = int(input("Enter the number of levels: "))
    
    levels = []
    for _ in range(no_of_levels):
        no_of_parking_spots_per_level = int(input("Enter the number of parking spots per level: "))
        level_spot = []
        for _ in range(no_of_parking_spots_per_level):
            options = [f"{vehicle.name}({vehicle.value})" for vehicle in VehicleType]
            vehicle_type = int(input(f"Enter the vehicle value {options}: "))
            vehicle_type = VehicleType(vehicle_type)
            spot = ParkingSpot(vehicle_type)
            level_spot.append(spot)
        
        level = ParkingLevel(level_spot)
        levels.append(level)
    
    print('------- lets create the parking lot')
    parkingLotName = input("Enter the parking lot name: ")
    parking_lot = ParkingLot(parkingLotName,levels)
            
    print('------- lets create some vehicles')
    no_of_vehicles = int(input("Enter the number of vehicles: "))
    
    for _ in range(no_of_vehicles):
        options = [f"{vehicle.name}({vehicle.value})" for vehicle in VehicleType]
        vehicle_type = int(input(f"Enter the vehicle value {options}: "))
        vehicle_type = VehicleType(vehicle_type)
        number = input("Enter the vehicle number: ")
        vehicle = Vehicle(vehicle_type,number)
        print('------- lets park the vehicle')
        parking_lot.assignParkingSpot(vehicle)
        print('------- lets unpark the vehicle')
        parking_lot.releaseParkingSpot(vehicle)
    
    print('------- end')
        
        
            
        
            
    
        
    
    
    
