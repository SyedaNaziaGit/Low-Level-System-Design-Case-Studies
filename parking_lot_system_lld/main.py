from models.vehicle import Vehicle
from models.car import Car
from models.motorcycle import Motorcycle
from models.truck import Truck
from models.vehicle_type import VehicleType
from models.parking_floor import Parking_Floor
from models.parking_spot import ParkingSpot
from services.parking_lot import ParkingLot

if __name__ == "__main___":
    lot = ParkingLot.get_instance()
    lot.add_floors(1,100)
    lot.add_floors(2,100)
    
    car = Car("1234")
    truck = Truck("5678")
    motorcycle = Motorcycle("ABCD")
    
    #ParkVehicles:
    ticket1 = lot.park_vehicle(car,"car")
    if ticket1:
        input("Press Enter to unpark...")
        lot.remove_vehicle(ticket1.ticket_id)
    lot.park_vehicle(truck)
    lot.park_vehicle(motorcycle)
    
    #Display Parking spot availibility:
    lot.find_available_parkingspot()
    
    #Remove vehicle or unpark:
    lot.remove_vehicle(motorcycle)
    
    #Display parking spot availibilty Update
    lot.find_available_parkingspot()
    
    