#user or passenger is an abstract class
class Passenger:
    def __init__(self, id,name, contact, location):
        self.id = id
        self.name = name
        self.contact = contact
        self.location = location
    
    def get_id(self):
        return self.id
    
    def get_location(self):
        return self.location
    
    def get_contact(self):
        return self.contact
    