import uuid
import time
from models.ticket import Ticket
from models.parking_floor import Parking_Floor

class ParkingLot:
    _instance = None
    
    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This Class is singleton")
        else:
            ParkingLot._instance = self
            self.floors : List[floor_number ] = []
            self.tickets = {}
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            ParkingLot()
        return ParkingLot._instance
    
    def add_floors(self,floor):
        self.floors.append(floor)
        
    def find_available_parkingspot(self,vehicle_type):
        for eachfloor in self.floors:
            eachfloor.display_spot_availability()
            
    def park_vehicle(self,vehicle,vehicle_type):
        spot = find_available_parkingspot(vehicle_type)
        if not spot :
            print("No free spot available for", vehicle_type)
            return None
        if spot.park_vehicle(vehicle):
            ticket_id = str(uuid.uuid4)
            ticket = Ticket(ticket_id,vehicle,spot.spot_id)
            self.tickets[ticket_id] = ticket
            print(f"Vehicle parked. Ticket ID: {ticket_id}")
            return ticket
        return None
    
    def remove_vehicle(self,ticket_id):
        ticket = self.tickets.get(ticket_id)
        if not ticket:
            print("Invalid ticket")
            return

        for eachfloor in self.floors:
            for eachspot in eachfloor.spots:
               if eachspot.spot_id == ticket.spot_id:
                   eachspot.remove_vehicle()
                   duration = time.time() - ticket.entry_time
                   print(f"Vehicle unparked. Duration: {duration:.2f} seconds")
                   del self.tickets[ticket_id]
                   return 
        print("Spot not found")
        
        
            
        
                            