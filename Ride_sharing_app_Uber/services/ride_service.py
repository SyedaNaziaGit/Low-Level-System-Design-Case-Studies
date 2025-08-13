from concurrent.futures import ThreadPoolExecutor
from models.ride import Ride
from enums.ride_status import RideStatus
from enums.driver_status import DriverStatus
from models.driver import Driver
import math
import time
import random

class RideService:
    _instance = None
    _lock = ThreadPoolExecutor(max_workers=1)
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls=cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.passengers = {}
        self.drivers = {}
        self.rides = {}
        self.requested_rides = []
        
    def add_passenger(self,passenger):
        self.passengers[passenger.get_id()] = passenger
    
    def add_driver(self,driver):
        self.drivers[driver.get_id()] = driver
        
    def request_ride(self, passenger,source ,destination,vehicle_type):
        ride_id = self._generate_ride_id()
        ride = Ride(id=ride_id,passenger = passenger,driver=None,destination=destination,status=DriverStatus.REQUESTED,fare=0.0,vehicle_type=vehicle_type)
        self.requested_rides.append(ride)
        self._notify_drivers(ride)
        
    def accept_ride(self,driver,ride):
        if ride.get_status == RideStatus.REQUESTED:
            ride.set_driver(driver)
            ride.set_status( RideStatus.ASSIGNED)
            driver.set_status(DriverStatus.BUSY)
            self._notify_passenger(ride)
            
    def start_ride(self,ride):
        if ride.get_status() == RideStatus.ASSIGNED:
            ride.set_status(RideStatus.STARTED)
            self._notify_passenger(ride)
    
    def complete_ride(self,ride):
        if ride.get_status() == RideStatus.STARTED:
            ride.set_status(RideStatus.COMPLETED)
            ride.get_driver().set_status(DriverStatus.AVAILABLE)
            fare = self._calculate_fare(ride)
            ride.set_fare(fare)
            self._process_payment(ride,fare)
            self._notify_passenger(ride)
            self._notify_driver(ride)
    
    def cancel_ride(self,ride):
        if ride.get_status() in [RideStatus.REQUESTED, RideStatus.ASSIGNED]:
            ride.set_status(RideStatus.CANCELLED)
            if ride.get_driver():
                ride.get_driver().set_status(DriverStatus.AVAILABLE)
            self._notify_passenger(ride)
            self._notify_driver(ride)
    
    def _notify_drivers(self,ride):
        for driver in self.drivers.values():
            if driver.get_status() == DriverStatus.AVAILABLE:
                distance = self._calculate_distance(driver.get_location(),ride.get_source())
                if distance <= 5.0 : #notify the driver within 5km radius 
                    #send notification to the driver
                    print(f"Notifying driver: {driver.get_name()} about ride  request: {ride.get_id()}")
    
    def _notify_passenger(self,ride):
        passanger = ride.get_passanger()
        message = ""
        if ride.get_status() == RideStatus.ASSIGNED:
            message = f"Your ride has been assiagned to driver :{ride.get_driver().get_name()}"
        elif ride.get_status() ==  RideStatus.STARTED:
            message = f"Your ride has been Started"
        elif ride.get_status() == RideStatus.COMPLETED:
            message = f"Your ride has been completed"
        elif ride.get_status() == RideStatus.CANCELLED:
            message = f"Your ride has been Cancelled"
        #Send notification to the passenegr
        print(f"Notifying passenger:{passanger.get_name()} - {message}")
        
    def _notify_driver(self,ride):
        driver = ride.get_driver()
        if driver:
            message = ""
            if ride.get_status() ==  RideStatus.COMPLETED:
                message = f" Ride completed. Fare :${ride.get_fare():.2f}"
            elif ride.get_status() == RideStatus.CANCELLED:
                message = f"Ride cancelled by passanger"
            #send notification to the driver
            print(f"Notifying driver:{driver.get_name()} - {message}")
            
    def _calculate_fare(self,ride):
        base_fare = 2.0
        per_km_fare = 1.5
        per_min_fare = 0.25
        distance = self._calculate_distance(ride.get_source(),ride.get_distance())
        duration = self._calculate_duration(ride.get_source(),ride.get_destination())
        fare = base_fare + (distance*per_km_fare) +(duration*per_min_fare)
        return round(fare,2)
    
    def _calculate_distance(self,source,destination):
        #calculate the eta between source n destination
        return random.uniform(1,20)
    
    def _calculate_duration(self,source,destination):
        #lets assume average speed is 30kmph
        distance =  self._calculate_distance(source=source,destination=destination)
        return (distance/30)*60 #Converting hours to minutes
    
    def _process_payment(self,ride,amount):
        #processing payment for the ride
        pass
    
    def _generate_ride_id(self):
        return int(time.time())
    
    def get_rides(self):
        return self.rides
    
    def get_requested_rides(self):
        return self.requested_rides
        