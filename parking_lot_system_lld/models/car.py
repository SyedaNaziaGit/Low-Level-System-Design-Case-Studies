from vehicle_type import VehicleType
from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, license_number, vehicle_type):
        super().__init__(license_number, VehicleType.Car)
        