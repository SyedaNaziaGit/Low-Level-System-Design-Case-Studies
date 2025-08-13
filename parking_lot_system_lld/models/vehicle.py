from abc import ABC
from vehicle_type import VehicleType


class Vehicle(ABC):
    def __init__(self,license_number,vehicle_type):
        self.license_number = license_number
        self.type = vehicle_type
        
    def get_type(self) -> VehicleType:
        return self.type