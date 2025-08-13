from transaction import Transaction

class WithdrawTransaction(Transaction):
    def __init__(self, transaction_id, account, amount):
        super().__init__(transaction_id, account, amount)
    
    def execute(self):
        self.account.withdraw_amount(self.amount)