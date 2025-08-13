from enums.driver_status import DriverStatus
from models.vehicle import Vehicle
class Driver:
    def __init__(self, id, name, contact, location, license_plate,status,vehicle):
        self.id = id
        self.name = name
        self.contact = contact
        self.license_plate = license_plate
        self.status =  status
        self.vehicle = vehicle
        
    def set_id(self,id):
        self.id = id
    
    def set_name(self,name):
        self.name = name
    
    def set_location(self,location):
        self.location = location
        
    def set_contact(self,contact):
        self.contact = contact
        
    def set_license_plate(self,license_plate):
        self.license_plate = license_plate
        
    def set_status(self,status):
        self.status = status
        
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_conatct(self):
        return self.contact
    
    def get_license_plate(self):
        return self.license_plate
    
    def get_location(self):
        return self.location
    
    def get_status(self):
        return self.status
    