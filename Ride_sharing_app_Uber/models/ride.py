class Ride:
    def __init__(self,id,passanger,driver,source, destination,status, fare,vehicle_type):
        self.id = id
        self.passanger = passanger
        self.driver = driver
        self.source = source
        self.destination = destination
        self.status = status
        self.fare = fare
        self.vehicle_type = vehicle_type
        
    def set_driver(self,driver):
        self.driver = driver
    
    def set_status(self,status):
        self.status = status
    
    def set_fare(self,fare):
        self.fare = fare
    
    def set_vehicle_type(self,vehicle_type):
        self.vehicle_type = vehicle_type
        
    def get_id(self):
        return self.id
    
    def get_passanger(self):
        return self.passanger
    
    def get_driver(self):
        return self.driver
    
    def get_source(self):
        return self.source
    
    def get_destination(self):
        return self.destination
    
    def get_status(self):
        return self.status
    
    def get_fare(self):
        return self.fare
    