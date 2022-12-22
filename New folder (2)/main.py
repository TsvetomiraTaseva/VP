from errors import *
from entities import *

all_names = []
users = []
class Menu:
    def print_menu(self):
        print("1. Create new User")
        print("2. Create new Accout")
        print("3. Show all users")
        print("4. Show all accounts")
        print("5. Make deposit")
        print("6. Make withdrawing money from an account")
        print("7. Exit")

    def command_create_user(self, name, account, EGN):
        return name, account, EGN

    def command_create_account(self, balance, currency, account_type, IBAN):
        return balance,currency,account_type,IBAN

    def run(self):
        while True:
            self.print_menu()

            choice = input("Choose a step from the menu: ")

            try:
                if choice == "1":
                    name = input("Enter the person name: ") 
                    account = input("Enter an account: ")
                    EGN = input("Enter EGN number. Only digits and len 10: ")
                    if len(EGN) != 10:
                        raise InvalidDataFormat("EGN len is 10")
                    all_names.append(name)
                    print (all_names)
                    usser = self.command_create_user(name, account, EGN)
                    users.append(usser)
                    continue
                if choice == "2":
                    EGN = input("Enter EGN number. Only digits and len 10: ")
                    if EGN in users:
                        balance = float(input("Enter sum of balance: "))
                        currency = input("Enter BGN, EUR, USD or JPY")
                        account_type = input("Enter Current, Savings, Credits")
                        if currency != "BGN" or currency != "EUR" or currency != "USD" or currency != "JPY":
                            raise InvalidAccountCurrency("The currency is not valid")
                        elif account_type != "Currens" or account_type != "Savings" or account_type != "Credits":
                            raise InvalidAccountType
                        
                if choice == "3":
                    print(f"All users are: {users}")
                if choice == "4":
                    pass
                if choice == "5":
                    pass
                if choice == "6":
                    pass
                if choice == "7":
                    break
                else:
                    raise InvalidCommand("The step does not exist!")
            except Exception as ex:
                print("Error: {str(ex)}")

            print()

if __name__ == '__main__':
    menu = Menu()
    menu.run()

    