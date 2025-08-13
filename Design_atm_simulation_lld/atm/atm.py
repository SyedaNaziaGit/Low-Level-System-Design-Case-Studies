from atm.cash_dispenser import CashDispenser
from atm.withdraw_transaction import WithdrawTransaction
from atm.balance_enquiry import BalanceEnquiry
from atm.deposit_transaction import DepositTransaction
from datetime import datetime
import threading
#from bank_service import BankService
from card import Card

class ATM:
    def __init__(self,bankservice,transaction_counter):
        self.bankservice = bankservice
        self.transaction_couter = transaction_counter
        self.cash_dispenser = CashDispenser()
        self.transaction_lock = threading.Lock()
    
    def create_transaction_id(self):
        with self.transaction_lock:
            self.transaction_couter+=1
            transaction_time = datetime.now().strftime("%Y%m%d%H%M%S")
            return f"BANK-TXN{transaction_time}{self.transaction_counter:010d}"
    
    def authenticate_user_account(self,card_number,entered_pin):
        #session started:
        if self.card.get_pin() != entered_pin:
            print("Incorrect PIN.")
            print("Try Again")
            return
        account = self.bankservice.get_account(card_number)
        print("Login successful.")
        
    def check_balance(self,account_number):
        txn = BalanceEnquiry(self.create_transaction_id(),account=account_number )
        txn.execute()
        
    def withdraw_cash(self,account_number,amount):
        account = self.bankservice.get_account(account_number)
        txn = WithdrawTransaction(self.create_transaction_id(),account=account,amount=amount)
        txn.execute()
        self.cash_dispenser.dispense_cash(amount=int(amount))
        
    def deposit_cash(self,account_number,amount):
        account = self.bankservice.get_account(account_number)
        txn = DepositTransaction(self.create_transaction_id(),account=account,amount=amount)
        txn.execute()
        
    
        