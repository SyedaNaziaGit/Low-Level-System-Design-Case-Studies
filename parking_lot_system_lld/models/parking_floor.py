from models.parking_spot import ParkingSpot
from models.vehicle import Vehicle
from models.vehicle_type import VehicleType

class Parking_Floor:
    def __init__(self,floor_number):
        self.floor_number = floor_number
        self.parking_spots = [] #list of parking spots
    
    def park_vehicle(self,vehicle):
        for eachspot in self.parking_spots:
            if not eachspot.parkingspot_available() and eachspot.get_vehicle_type == vehicle.get_type():
                eachspot.park_vehicle(vehicle)
                return True
        return False
    
    def remove_vehicle(self,vehicle):
        for eachspot in self.parking_spots:
            if not eachspot.parkingspot_available() and  eachspot.get_parked_vehicle == vehicle:
                eachspot.remove_vehicle()
                return True
        return False
    
    def display_spot_availability(self):
        print(f"Level {self.floor_number} Availability")
        for eachspot in self.parking_spots:
            print(f"Spot {eachspot.get_spot_id()}:{'Available' if eachspot.parkingspot_available() else 'Occupied'}")