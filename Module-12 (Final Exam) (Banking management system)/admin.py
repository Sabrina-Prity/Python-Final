from user import User
from datetime import datetime

class Admin:
    def __init__(self):
        self.users = []

    def create_account(self, name, email, address, account_type, initial_balance=0):
        new_user = User(name, email, address, account_type, initial_balance)
        self.users.append(new_user)
        print(f"Account created for {name} with account number: {new_user.account_number} with Balance: {initial_balance} on {datetime.now()}")

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print(f"Account number {account_number} deleted.")
                return
        print("Account not found.")

    def view_accounts(self):
        if not self.users:
            print("No user accounts available.")
        else:
            for user in self.users:
                print(f"Account Number: {user.account_number}, Name: {user.name}, Balance: {user.curr_balance}, Account Type: {user.account_type}")

    def total_balance(self):
        total = sum(user.curr_balance for user in self.users)
        if total <= 0:
            print('The bank is bankrupt.')
        else:
            print(f"Total available balance of the bank: {total}")

    def total_loans(self):
        total_loans = sum(user.loan_taken for user in self.users)
        print(f"Total loans taken: {total_loans}")

    def loan_feature(self, status):
        if status:
            print("Loan feature is now ON.")
        else:
            print("Loan feature is now OFF.")

   