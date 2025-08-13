class Account:
    def __init__(self,account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance
        
    def get_account_number(self):
        return self.account_number
    
    def get_balance(self):
        return self.balance
    
    def withdraw_amount(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
        else:
            print("Insufficient Balance")
    
    def deposit_amount(self,amount):
        self.balance += amount
        print(f"Deposited:${amount}")
        print(f"Available balance:${self.balance}")
        