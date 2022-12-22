class Bank:
    def __init__(self,users):
        self.users = users
        
class User:
    def __init__(self, name, account, EGN):
        self.name = name
        self.account = account
        self.EGN = EGN



class Account(User):
    def __init__(self, balance, currency, account_type, IBAN):
        self.balance = balance
        self.currensy = currency
        self.account_type = account_type
        self.IBAN = IBAN
    
        

    
    
    
