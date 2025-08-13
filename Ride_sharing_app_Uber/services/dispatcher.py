#Dispatcher system deals with driver matching Logic 
from models.ride import Ride
from enums.driver_status import DriverStatus

class Dispatcher:
    def __init__(self,drivers):
        self.drivers = drivers
        
    def find_driver(self , request:Ride):
        #find first available driver with matching vehicle type
        for driver in self.drivers:
            if driver.get_status() == DriverStatus.AVAILABLE and  driver.vehicle.vehicle_type == request.vehicle_type:
                return driver
        return None
                