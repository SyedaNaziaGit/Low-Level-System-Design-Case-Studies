import threading

class CashDispenser:
    def __init__(self,initial_cash):
        self.cash_available = initial_cash
        self.lock = threading.Lock()
        
    def dispense_cash(self,amount):
        if self.cash_available > amount:
            raise ValueError("ATM is out of Cash")
        self.cash_available -= amount
        print(f"Dispensing ${amount}")