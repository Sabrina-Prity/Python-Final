from user import User
from admin import Admin

admin = Admin()
admin_password = 'admin123'

# Create initial users
admin.create_account('Rohim', 'rahim@gmail.com', 'Dhaka', 'Savings', 60000)
admin.create_account("karim", "karim@gmail.com", "Ctg", "General", 3000)
admin.create_account("Cuhi", "cuhi@gmail.com", "Noakhali", "Savings", 50000)

run = True

while run:
    option = input("Are you an Admin or User? (A/U) or Q to Quit: ").upper()
    
    # Admin Menu 
    if option == 'A':
        password = input("Enter Admin Password: ")
        if password == admin_password:
            while True:
                print("\n\t<----- Admin Options ----->")
                print("\t1 : Create New Account")
                print("\t2 : Delete any Account")
                print("\t3 : View All Accounts")
                print("\t4 : Total Balance")
                print("\t5 : Total Loans")
                print("\t6 : Set Loan Feature")
                print("\t7 : Logout")

                choose = int(input("\nEnter Option: "))

                if choose == 1:
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    address = input("Enter address: ")
                    account_type = input("Enter account type eg.(Savings or General): ").lower()
                    initial_balance = int(input("Enter initial balance: "))
                    admin.create_account(name, email, address, account_type, initial_balance)

                elif choose == 2:
                    account_number = int(input("Enter account number to delete: "))
                    admin.delete_account(account_number)

                elif choose == 3:
                    admin.view_accounts()

                elif choose == 4:
                    admin.total_balance()

                elif choose == 5:
                    admin.total_loans()

                elif choose == 6:
                    status = input("Enable loan feature? (yes/no): ").lower() == 'yes'
                    admin.loan_feature(status)

                elif choose == 7:
                    print("\n\tLogged out successfully.")
                    break

                else:
                    print("\n\tInvalid option. Please try again.")
        else:
            print("\n\tIncorrect Password. Please enter correct password.")

    # User Menu
    elif option == 'U':
        account_number = int(input("Enter your account number: "))
        
        found_user = None  
        for u in admin.users:
            if u.account_number == account_number:
                found_user = u
                break  

        if found_user is None:
            print("Account not found. Please enter a valid account number.")
            continue
        else:
            user = found_user

        while True:
            print("\n\t<----- User Options ----->")
            print("\t1 : Deposit")
            print("\t2 : Withdraw")
            print("\t3 : Check Balance")
            print("\t4 : Transaction History")
            print("\t5 : Transfer Amount")
            print("\t6 : Take Loan")
            print("\t7 : Logout")

            choose = int(input("\nEnter Option: "))

            if choose == 1:
                amount = int(input("Enter amount to deposit: "))
                user.deposit(amount)

            elif choose == 2:
                amount = int(input("Enter amount to withdraw: "))
                user.withdraw(amount)

            elif choose == 3:
                user.balance_check()

            elif choose == 4:
                user.transaction_history()

            elif choose == 5:
                if user.account_type == "Savings":
                    print("Transfer not allowed: It\'s a Savings account.")
                else:
                    other_account_number = int(input("Enter recipient account number: "))
                    other_user = next((u for u in admin.users if u.account_number == other_account_number), None)
                    if other_user is None:
                        print("Recipient account not found.")
                        continue
                    amount = int(input("Enter amount to transfer: "))
                    user.transfer_amount(other_user, amount)

            elif choose == 6:
                if not admin.loan_feature:
                    print("Loan feature is currently OFF.")
                else:
                    user.take_loan()

            elif choose == 7:
                print("\n\tLogged out successfully.")
                break

            else:
                print("\n\tInvalid option. Please try again.")

    # Exit Menu
    elif option == 'Q':
        run = False
        print("\n\tExiting the system. Goodbye!")
    else:
        print("\n\tInvalid option. Please enter 'A' for Admin, 'U' for User, or 'Q' to Quit.")
