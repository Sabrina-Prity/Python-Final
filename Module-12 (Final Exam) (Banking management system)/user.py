from abc import ABC
from datetime import datetime

class User(ABC):
    account_counter = 1000  

    def __init__(self, name, email, address, account_type, initial_balance=0):
        User.account_counter += 1
        self.account_number = User.account_counter
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type

        self.curr_balance = initial_balance
        self.history = []
        self.loan_taken = 0

    def deposit(self, amount):
        if amount > 0:
            self.curr_balance += amount
            self.history.append(f"Deposited: {amount} on {datetime.now()}")
            print(f"Successfully deposited: {amount}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if self.curr_balance <= 0:
            print("You have 0 balance in your account.")
            return
        
        if self.account_type == "Savings" and self.curr_balance <= 60000:
            print("Withdrawal not allowed: Balance must be greater than 60,000 for Savings accounts.")
            return
            
        if amount > self.curr_balance:
            print(f'Withdrawal amount exceeded!!! Your Current Amount: {self.curr_balance}')
        else:
            self.curr_balance -= amount
            self.history.append(f"Withdrawn: {amount} on {datetime.now()}")
            print(f"Successfully withdrawn: {amount}")

    def balance_check(self):
        print(f"Your Current Balance: {self.curr_balance}")

    def transaction_history(self):
        if not self.history:
            print("No transaction history available.")
        else:
            for record in self.history:
                print(record)

    def take_loan(self):
        if self.loan_taken < 2:
            self.loan_taken += 1
            print("Loan taken successfully.")
        else:
            print("You can only take loans 2 times.")

    def transfer_amount(self, other_user, amount):
        if not other_user:
            print("Account does not exist.")
            return
        
        if amount > self.curr_balance:
            print(f"You don't have enough funds. Your Current Amount: {self.curr_balance}")
            return
        else:
            self.curr_balance -= amount
            other_user.curr_balance += amount
            self.history.append(f"Transferred: {amount} to {other_user.name} on {datetime.now()}")
            other_user.history.append(f"Received: {amount} from {self.name} on {datetime.now()}")
            print(f"Successfully transferred: {amount} to {other_user.name}")



