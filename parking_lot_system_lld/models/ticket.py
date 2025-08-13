import time
from models.vehicle import Vehicle
from models.parking_spot import ParkingSpot

class Ticket:
    def __init__(self,vehicle,spot_id,ticket_id):
        self.ticket_id = ticket_id
        self.vehicle = vehicle
        self.spot_id = spot_id
        self.entry_time = time.time()
        
    