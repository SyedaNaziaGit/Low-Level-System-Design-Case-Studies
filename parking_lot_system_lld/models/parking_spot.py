from vehicle import Vehicle
from vehicle_type import VehicleType

class ParkingSpot:
    def __init__(self,spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.parked_vehicle = None
    
    def parkingspot_available(self)-> bool:
        return self.parked_vehicle is None
    
    def park_vehicle(self,vehicle):
        if self.parkingspot_available() and vehicle.get_type() == self.vehicle_type:
            self.parked_vehicle = vehicle
        else:
            raise ValueError("spot is already occupied")
    
    def remove_vehicle(self):
        self.parked_vehicle = None
        
    def get_spot_id(self):
        return self.spot_id
    
    def get_parked_vehicle(self):
        return self.parked_vehicle
    
    def get_vehicle_type(self):
        return self.vehicle_type