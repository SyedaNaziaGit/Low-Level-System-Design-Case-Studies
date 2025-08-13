from atm.atm import ATM
from atm.bank_service import BankService
from atm.cash_dispenser import CashDispenser
from atm.card import Card


class MainDemo:
    @staticmethod
    def run():
        bankservice = BankService()
        cash_dispenser = CashDispenser()
        atm = ATM(bankservice,cash_dispenser)
        
        #creating sample accounts:
        bankservice.create_account("9876543210",1000.0)
        bankservice.create_account("1234567890",10000.0)
        
        #Perform ATM Operations:
        card = Card("1234567890","1234")
        atm.authenticate_user_account(card)
        
        balance = atm.check_balance("1234567890")
        print("Balance amount:",balance)
        
        atm.withdraw_cash("1234567890", 500.0)
        atm.deposit_cash("9876543210", 200.0)
        
        balance = atm.check_balance("1234567890")
        print("Updated Balance amount:",balance)
if __name__ == "__main__":
    MainDemo.run()