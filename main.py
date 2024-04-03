from random import randint
from datetime import datetime


def mainMenu():
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t\tWELCOME TO BANKING SERVICE SYSTEM")
    print("\nHere are the User Type for this Banking System")
    print("\n\tChoose user Type(1/2/3): ")
    print("\t1. Super User Account")
    print("\t2. ADMIN")
    print("\t3. CUSTOMER")
    print("\t0. Terminate Program")
    menuc = int(input("\nEnter Your Choice: "))

    if menuc == 1:
        print("You've Chosen the Super User Account.")
        superUserLogin()
    elif menuc == 2:
        print("\nYou've Chosen the Admin User Type.")
        adminLogin()
    elif menuc == 3:
        print("\n\t1. Do you have Account? Register Now.")
        print("\t2. Login. If you have Account")
        c1 = int(input("\nEnter Your Choice: "))

        if c1 == 1:
            registerCustomerAccount()
        elif c1 == 2:
            customerLogin()
        else:
            mainMenu()
    elif menuc == 0:
        print("Program Terminated. Good Bye!")
    else:
        print("Wrong Input.")
        mainMenu()






###################################################     SUPER USER       #########################################################
def superUserLogin():
    print("\n\tLOGIN TO USE SUPER USER ACCOUNT SYSTEMS\n")

    print("Enter your username: ")
    username = input()
    print("Enter your password: ")
    password = input()
    if username == "Super User" and password == "444602":
        print("\nLogin Successful. Welcome to Super User Account System.")
        superUserMenu()
    else:
        print("Wrong Password!")
        superUserLogin()


def superUserMenu():
    print("\n\nHere are the functionalities for Super User Account")
    print("\t1. Create Admin Account")
    print("\t2. View Admin Information")
    print("\t3. Update Admin Password")
    print("\t4. Delete Admin Information")
    print("\t5. Logout")
    superc1 = int(input("\nEnter Your Choice(1/2/3/4/5): "))

    if superc1 == 1:
        createAdminAccount()
    elif superc1 == 2:
        viewAdminAccount()
    elif superc1 == 3:
        updateAdminPassword()
    elif superc1 == 4:
        deleteAdminAccount()
    elif superc1 == 5:
        mainMenu()
    else:
        print("Invalid Input.")
        superUserMenu()


def createAdminAccount():
    admin_id = input("Enter Admin ID: ")
    admin_password = input("Enter Admin Password: ")
    branch_name = input("Enter Branch Name: ")

    # Check if the admin ID already exists
    admin_ids = set()
    try:
        with open("adminInfo.txt", "r") as file:
            for line in file:
                admin_data = line.strip().split(", ")
                admin_ids.add(admin_data[0])
    except FileNotFoundError:
        pass

    if admin_id in admin_ids:
        print("\nAdmin ID already exists. Please choose a different ID.")
        superUserMenu()
        return

    # Writing admin information to a text file
    with open("adminInfo.txt", "a") as file:
        file.write(f"{admin_id}, {admin_password}, {branch_name}\n")

    print("\nAdmin Account Created Successfully")

    print("\nDo You Want To Create Another Admin Account [0-Yes/1-No]")
    choice = int(input("Enter Your Choice: "))
    if choice == 0:
        createAdminAccount()
    elif choice == 1:
        superUserMenu()
    else:
        superUserMenu()


def viewAdminAccount():
    try:
        with open("adminInfo.txt", "r") as file:
            admin_info = [line.strip().split(", ") for line in file]

        print("\nAll Admin Information:")
        for admin in admin_info:
            print(f"Admin ID: {admin[0]}, Admin Password: {admin[1]}, Branch Name: {admin[2]}")
        superUserMenu()
    except FileNotFoundError:
        print("Admin information file not found.")
        superUserMenu()


def updateAdminPassword():
    try:
        with open("adminInfo.txt", "r") as file:
            info = [line.strip().split(", ") for line in file]

        print("\nAll Admin Information")
        for admin in info:
            print(f"Admin ID: {admin[0]}, Admin Password: {admin[1]}, Branch Name: {admin[2]}")

        admin_id_to_update = input("\nEnter the Admin ID you want to update password for: ")
        found = False

        for i in range(len(info)):
            admin_data = info[i]
            if admin_data[0] == admin_id_to_update:
                found = True
                new_password = input("Enter the new password: ")
                admin_data[1] = new_password
                info[i] = admin_data
                break

        if found:
            with open("adminInfo.txt", "w") as file:
                for admin in info:
                    file.write(", ".join(admin) + "\n")
            print("\nPassword updated successfully!")
            superUserMenu()
        else:
            print("Admin ID not found!")
            superUserMenu()

    except FileNotFoundError:
        print("Admin information file not found.")
        superUserMenu()


def deleteAdminAccount():
    try:
        with open("adminInfo.txt", "r") as file:
            info = [line.strip().split(", ") for line in file]

        print("\nCurrent Admin Information")
        for admin in info:
            print(f"Admin ID; {admin[0]}, Admin Password: {admin[1]}, Branch Name: {admin[2]}")

        admin_id_to_delete = input("Enter the Admin ID you want to delete: ")
        found = False
        updated_info = []

        for admin_data in info:
            if admin_data[0] == admin_id_to_delete:
                found = True
            else:
                updated_info.append(admin_data)

        if found:
            with open("adminInfo.txt", "w") as file:
                for admin_data in updated_info:
                    file.write(", ".join(admin_data) + "\n")
            print("Admin information deleted successfully!")
            superUserMenu()
        else:
            print("Admin ID not found!")
            superUserMenu()

    except FileNotFoundError:
        print("Admin information file not found.")






##############################################     ADMIN FUNCTIONALITIES      #####################################################
def adminLogin():
    admin_id = input("Enter Admin ID: ")
    admin_password = input("Enter Admin Password: ")

    try:
        with open("adminInfo.txt", "r") as file:
            for line in file:
                admin_data = line.strip().split(", ")
                if admin_data[0] == admin_id and admin_data[1] == admin_password:
                    print("\nLogin Successful. Welcome to Banking Service Admin System.\n")
                    adminMenu()
                    return
            print("\nInvalid Admin ID or Password\n")
            adminLogin()
    except FileNotFoundError:
        print("\nAdmin information file not found.\n")


def adminMenu():
    print("\nHere Are The Functionalities for Admin")
    print("\n\tChoose One Menu")
    print("\t1. Approve Customer Registration.")
    print("\t2. Create Customer Account.")
    print("\t3. Display Customer Information.")
    print("\t4. Update Customer Account Password.")
    print("\t5. Delete Customer Account.")
    print("\t6. View Statement by Daily, Monthly, Yearly.")
    print("\t7. Update Customer Info.")
    print("\t8. Logout.")

    adminc = int(input("\nEnter Your Choice: "))

    if adminc == 1:
        approveRegistration()
    elif adminc == 2:
        createCustomerAccount()
    elif adminc == 3:
        displayCustomerInformation()
    elif adminc == 4:
        updateCustomerPassword()
    elif adminc == 5:
        deleteCustomerAccount()
    elif adminc == 6:
        viewStatementByAdmin()
    elif adminc == 7:
        updateCustomerInfo()
    elif adminc == 8:
        mainMenu()
    else:
        print("Invalid Input. Enter the Correct Choice.")
        adminMenu()


def approveRegistration():
    pending_customers = []
    try:
        with open("customerInfo.txt", "r") as file:
            for line in file:
                customer_data = line.strip().split(", ")
                if customer_data[-1] == "pending":
                    pending_customers.append(customer_data)
    except FileNotFoundError:
        print("\nCustomer information file not found.\n")
        adminMenu()
        return

    if not pending_customers:
        print("\nNo pending registrations at the moment.\n")
        adminMenu()
        return

    print("\nPending Registrations:")
    for index, customer in enumerate(pending_customers):
        print(f"{index+1}. Customer Name: {customer[0]}, Passport/IC Number: {customer[5]}")

    passport_number = input("\nEnter Passport Number to approve or decline registration: ")

    found = False
    for i in range(len(pending_customers)):
        if pending_customers[i][5] == passport_number:
            found = True
            status = input("Enter status (confirmed/declined): ")
            if status == "confirmed":
                account_number = generateAccountNumber()

                pending_customers[i][-1] = "confirmed"
                pending_customers[i] += [account_number]

                with open("customerInfo.txt", "w") as file:
                    for customer in pending_customers:
                        file.write(", ".join(customer) + "\n")

                print(f"\nRegistration for {passport_number} confirmed. Name: {customer[0]}, Account Number: {account_number}\n")

                print("Do you want to create account for this customer now?[0-Yes/1-No]")
                c2 = int(input("Enter Your Choice(0/1): "))

                if c2 == 0:
                    createCustomerAccount()
                elif c2 == 1:
                    approveRegistration()
                else:
                    print("Invalid Input")
                    adminMenu()

            elif status == "declined":
                pending_customers[i][-1] = "declined"

                with open("customerInfo.txt", "w") as file:
                    for customer in pending_customers:
                        file.write(", ".join(customer) + "\n")

                print(f"\nRegistration for {passport_number} declined.\n")

                print("Do you want to  confirmed/declined another account[0-Yes/1-No]")
                c1 = int(input("Enter Your Choice: "))
                if c1 == 0:
                    approveRegistration()
                elif c1 == 1:
                    adminMenu()
                else:
                    print("Wrong Input!")
                    adminMenu()

            else:
                print("\nInvalid status. Please enter 'confirmed' or 'declined'.\n")
                adminMenu()

    if not found:
        print("\nPassport Number not found or already processed.\n")
        adminMenu()
        return


def generateAccountNumber():
    account_numbers = set()
    try:
        with open("customerInfo.txt", "r") as file:
            for line in file:
                customer_data = line.strip().split(", ")
                if len(customer_data) > 6 and customer_data[6] != "pending":
                    account_numbers.add(customer_data[6])
    except FileNotFoundError:
        pass

    while True:
        account_number = randint(10000000, 99999999)
        if account_number not in account_numbers:
            return str(account_number)


def createCustomerAccount():
    customer_name = input("Enter Customer Name: ")
    account_number = input("Enter Account Number: ")
    default_password = input("Enter Default Password: ")
    account_type = input("Enter Account Type (Savings Account or Current Account): ")
    if account_type == "Savings Account":
        initial_balance = 100
    elif account_type == "Current Account":
        initial_balance = 500
    else:
        print("Wrong Input")
        return

    with open("customerAccountInfo.txt", "a") as file:
        file.write(f"{customer_name}, {account_number}, {default_password}, {account_type}, {initial_balance}\n")

    print("\nCustomer Account Created Successfully\n")
    print("Do you want to  confirmed/declined another account[0-Yes/1-No]")
    c1 = int(input("Enter Your Choice: "))
    if c1 == 0:
        approveRegistration()
    elif c1 == 1:
        adminMenu()
    else:
        print("Wrong Input!")
        adminMenu()


def displayCustomerInformation():
    try:
        with open("customerAccountInfo.txt", "r") as file:
            print("\nCustomer Information:")
            for line in file:
                customer_data = line.strip().split(", ")
                print(f"Name: {customer_data[0]}, Account Number: {customer_data[1]}, Account Type: {customer_data[3]}, Balance: RM {customer_data[4]}")
    except FileNotFoundError:
        print("\nCustomer account information file not found.\n")
    adminMenu()


def updateCustomerPassword():
    account_number = input("Enter Account Number: ")
    new_password = input("Enter New Password: ")

    try:
        with open("customerAccountInfo.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("customerAccountInfo.txt", "w") as file:
            for line in lines:
                customer_data = line.strip().split(", ")
                if customer_data[1] == account_number:
                    customer_data[2] = new_password
                    updated_line = ", ".join(customer_data)
                    file.write(updated_line + "\n")
                    found = True
                else:
                    file.write(line)

        if not found:
            print("\nInvalid Account Number or Password\n")
            return

        print("\nPassword Updated Successfully!\n")
    except FileNotFoundError:
        print("\nCustomer account information file not found.\n")
    adminMenu()


def deleteCustomerAccount():
    try:
        with open("customerAccountInfo.txt", "r") as file:
            lines = file.readlines()

        print("\nCustomer Accounts:")
        for line in lines:
            customer_data = line.strip().split(", ")
            print(f"Name: {customer_data[0]}, Account Number: {customer_data[1]}, Account Type: {customer_data[3]}, Balance: RM {customer_data[4]}")

        account_number = input("\nEnter Account Number to Delete: ")
        found = False
        with open("customerAccountInfo.txt", "w") as file:
            for line in lines:
                customer_data = line.strip().split(", ")
                if customer_data[1] == account_number:
                    found = True
                else:
                    file.write(line)

        if found:
            print("\nCustomer Account Deleted Successfully!\n")
            adminMenu()
        else:
            print("\nAccount Number not found.\n")
            adminMenu()
    except FileNotFoundError:
        print("\nCustomer account information file not found.\n")
        adminMenu()


def viewStatementByAdmin():
    account_number = input("Enter your account number: ")
    print("Select the type of transaction details you want to view: ")
    print("\n\t1. Daily")
    print("\t2. Monthly")
    print("\t3. Yearly")
    choice = input("Enter your choice (1/2/3): ")

    try:
        with open("transactionHistory.txt", "r") as file:
            transactions = file.readlines()

        account_transactions = [t for t in transactions if t.split(', ')[1] == account_number]
        if not account_transactions:
            print("No transactions found for this account number.")
            return

        if choice == '1':
            date_input = input("Enter the date in YYYY-MM-DD format to view daily transactions: ")
            date_filter = lambda date: date.startswith(date_input)
        elif choice == '2':
            month_input = input("Enter the month in YYYY-MM format to view monthly transactions: ")
            date_filter = lambda date: date.startswith(month_input)
        elif choice == '3':
            year_input = input("Enter the year in YYYY format to view yearly transactions: ")
            date_filter = lambda date: date.split('-')[0] == year_input
        else:
            print("Invalid choice.")
            return

        print("\nTransactions:\n")
        has_transactions = False
        for transaction in account_transactions:
            transaction_details = transaction.split(', ')
            date_time = transaction_details[3]
            if date_filter(date_time):
                has_transactions = True
                print(f"Transaction Type: {transaction_details[0]}, Amount: {transaction_details[2]}, Date & Time: {date_time}, New Balance: {transaction_details[4].strip()}")

        if not has_transactions:
            print("No transactions found for this period.")

    except FileNotFoundError:
        print("Transaction history file not found.")
    adminMenu()


def updateCustomerInfo():
    passport_number = input("Enter Passport Number: ")

    try:
        with open("customerInfo.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("customerInfo.txt", "w") as file:
            for line in lines:
                customer_data = line.strip().split(", ")
                if customer_data[5] == passport_number:
                    new_dob = input("Enter New Date of Birth (DD/MM/YYYY): ")
                    new_email = input("Enter New Email: ")
                    new_phone = input("Enter New Phone Number: ")
                    customer_data[1] = new_dob
                    customer_data[2] = new_email
                    customer_data[3] = new_phone
                    updated_line = ", ".join(customer_data)
                    file.write(updated_line + "\n")
                    found = True
                else:
                    file.write(line)

        if not found:
            print("\nPassport Number not found\n")
            adminMenu()
            return

        print("\nCustomer Information Updated Successfully!\n")
        adminMenu()
    except FileNotFoundError:
        print("\nCustomer information file not found.\n")
    adminMenu()











##############################################     CUSTOMER FUNCTIONALITIES      #####################################################
def registerCustomerAccount():
    customer_info = []
    try:
        with open("customerInfo.txt", "r") as file:
            for line in file:
                customer_data = line.strip().split(", ")
                customer_info.append(customer_data[5])
    except FileNotFoundError:
        pass

    customer_name = input("Enter Customer Name: ")
    dob = input("Enter Date of Birth (DD/MM/YYYY): ")
    email = input("Enter Email: ")
    phone_number = input("Enter Phone Number: ")
    country = input("Enter Country: ")
    passport_number = input("Enter IC/Passport Number: ")
    gender = input("Enter Gender: ")

    if passport_number in customer_info:
        print("\nPassport Number already exists. Please choose a different Passport Number.\n")
        registerCustomerAccount()
        return

    with open("customerInfo.txt", "a") as file:
        file.write(f"{customer_name}, {dob}, {email}, {phone_number}, {country}, {passport_number}, {gender}, pending\n")

    print("\nCustomer Account Registration Successful. Please wait for the Approval.\n")
    mainMenu()


def customerLogin():
    account_number = input("Enter Account Number: ")
    password = input("Enter Password: ")

    try:
        with open("customerAccountInfo.txt", "r") as file:
            for line in file:
                customer_data = line.strip().split(", ")
                if customer_data[1] == account_number and customer_data[2] == password:
                    print("\nLogin Successful!\nWelcome to Banking Service Customer System.")
                    customerMenu(customer_data[0], account_number, customer_data[4])
                    return
            print("\nInvalid Account Number or Password\n")
            customerLogin()
    except FileNotFoundError:
        print("\nCustomer account information file not found.\n")


def customerMenu(customer_name, account_number, balance):
    print(f"\n\n\t\t\t\t\t\tCustomer Name: {customer_name} \t\t\t\t\tAccount Number: {account_number} \t\t\t\t\tBalance: RM {balance}")
    print(f"\n\nHere Are The Functionalities for {customer_name}")
    print("\n\tChoose One Menu")
    print("\t1. Deposit Money")
    print("\t2. Cash Withdrawal")
    print("\t3. Bank Statement by Daily, Monthly, and Yearly")
    print("\t4. Change Your Password")
    print("\t5. Logout")
    customerc = int(input("Enter Your Choice: "))

    if customerc == 1:
        depositMoney()
    elif customerc == 2:
        cashWithdrawal()
    elif customerc == 3:
        bankStatementByCustomer()
    elif customerc == 4:
        updateCustomerAccountPassword()
    elif customerc == 5:
        mainMenu()
    else:
        customerMenu(customer_name, account_number, balance)


def depositMoney():
    account_number = input("Enter Account Number: ")
    password = input("Enter Password: ")
    deposit_amount = float(input("Enter Amount to Deposit: "))

    try:
        with open("customerAccountInfo.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("customerAccountInfo.txt", "w") as file:
            for line in lines:
                customer_data = line.strip().split(", ")
                if customer_data[1] == account_number and customer_data[2] == password:
                    current_balance = float(customer_data[-1])
                    new_balance = current_balance + deposit_amount
                    customer_data[-1] = str(new_balance)
                    updated_line = ", ".join(customer_data)
                    file.write(updated_line + "\n")
                    found = True
                else:
                    file.write(line)

        if not found:
            print("\nInvalid Account Number or Password\n")
            customerMenu(customer_data[0], account_number, customer_data[4])
            return

        with open("transactionHistory.txt", "a") as file:
            transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Deposit, {account_number}, {deposit_amount}, {transaction_time}, New Balance = {new_balance}\n")

        print("\nDeposit Successful!\n")

        print("Do you want to deposit again or go back to customer menu? [0-Yes/1-No]: ")
        c1 = int(input("Enter Your Choice: "))

        if c1 == 0:
            depositMoney()
        elif c1 == 1:
            customerMenu(customer_data[0], account_number, customer_data[4])
        else:
            print("Invalid Input!")
            customerMenu(customer_data[0], account_number, customer_data[4])
    except FileNotFoundError:
        print("\nCustomer account information file not found.\n")
        customerMenu(customer_data[0], account_number, customer_data[4])


def cashWithdrawal():
    account_number = input("Enter Account Number: ")
    password = input("Enter Password: ")
    withdrawal_amount = float(input("Enter Amount to Withdraw: "))

    try:
        with open("customerAccountInfo.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("customerAccountInfo.txt", "w") as file:
            for line in lines:
                customer_data = line.strip().split(", ")
                if customer_data[1] == account_number and customer_data[2] == password:
                    current_balance = float(customer_data[-1])
                    account_type = customer_data[3]
                    if account_type == "Savings Account" and current_balance - withdrawal_amount < 100:
                        print("\nWithdrawal amount would result in balance below minimum for Savings Account (100 RM).\n")
                        customerMenu(customer_data[0], account_number, customer_data[4])
                        return
                    elif account_type == "Current Account" and current_balance - withdrawal_amount < 500:
                        print("\nWithdrawal amount would result in balance below minimum for Current Account (500 RM).\n")
                        customerMenu(customer_data[0], account_number, customer_data[4])
                        return
                    elif current_balance < withdrawal_amount:
                        print("\nInsufficient balance for withdrawal.\n")
                        customerMenu(customer_data[0], account_number, customer_data[4])
                        return
                    else:
                        new_balance = current_balance - withdrawal_amount
                        customer_data[-1] = str(new_balance)
                        updated_line = ", ".join(customer_data)
                        file.write(updated_line + "\n")
                        found = True
                else:
                    file.write(line)

        if not found:
            print("\nInvalid Account Number or Password\n")
            customerMenu(customer_data[0], account_number, customer_data[4])
            return

        with open("transactionHistory.txt", "a") as file:
            transaction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"Withdrawal, {account_number}, {withdrawal_amount}, {transaction_time}, New Balance = {new_balance}\n")

        print("\nWithdrawal Successful!\n")

        print("Do you want to withdraw money again or go back to customer menu? [0-Yes/1-No]: ")
        c1 = int(input("Enter Your Choice: "))

        if c1 == 0:
            cashWithdrawal()
        elif c1 == 1:
            customerMenu(customer_data[0], account_number,customer_data[4])
        else:
            print("Invalid Input!")
            customerMenu(customer_data[0], account_number,customer_data[4])
    except FileNotFoundError:
        print("\nCustomer account information file not found.\n")
        customerMenu(customer_data[0], account_number,customer_data[4])






def bankStatementByCustomer():
    account_number = input("Enter Account Number: ")
    password = input("Enter Password: ")

    try:
        with open("customerAccountInfo.txt", "r") as file:
            account_found = False
            for line in file:
                customer_data = line.strip().split(", ")
                if customer_data[1] == account_number and customer_data[2] == password:
                    account_found = True
                    break

            if not account_found:
                print("\nInvalid Account Number or Password\n")
                customerMenu(customer_data[0], account_number, customer_data[4])
                return

        with open("transactionHistory.txt", "r") as file:
            transactions = []
            for line in file:
                transaction_data = line.strip().split(", ")
                if transaction_data[1] == account_number:
                    transactions.append(transaction_data)

            if not transactions:
                print("\nNo transactions found for this account number.\n")
                customerMenu(customer_data[0], account_number, customer_data[4])
                return

        print("\nSelect Option:\n")
        print("\t1. Daily Statement")
        print("\t2. Monthly Statement")
        print("\t3. Yearly Statement")
        option = int(input("\nEnter Your Choice: "))

        if option == 1:
            date = input("Enter Date (YYYY-MM-DD): ")
            print(f"\nDaily Statement for {date}:")
            for transaction in transactions:
                if transaction[3].startswith(date):
                    print(f"Transaction Type: {transaction[0]}, Transaction Amount: {transaction[2]}, Date & Time: {transaction[3]}, New Balance: RM {transaction[4]}")

        elif option == 2:
            month = input("Enter Month (YYYY-MM): ")
            print(f"\nMonthly Statement for {month}:")
            for transaction in transactions:
                if transaction[3].startswith(month):
                    print(f"Transaction Type: {transaction[0]}, Transaction Amount: {transaction[2]}, Date & Time: {transaction[3]}, New Balance: RM {transaction[4]}")
        elif option == 3:
            year = input("Enter Year (YYYY): ")
            print(f"\nYearly Statement for {year}:")
            for transaction in transactions:
                if transaction[3].startswith(year):
                    print(f"Transaction Type: {transaction[0]}, Transaction Amount: {transaction[2]}, Date & Time: {transaction[3]}, New Balance: RM {transaction[4]}")
        else:
            print("\nInvalid Option\n")
    except FileNotFoundError:
        print("\nTransaction history file not found.\n")
    customerMenu(customer_data[0], account_number, customer_data[4])


def updateCustomerAccountPassword():
    account_number = input("Enter Account Number: ")
    current_password = input("Enter Current Password: ")
    new_password = input("Enter New Password: ")

    try:
        with open("customerAccountInfo.txt", "r") as file:
            lines = file.readlines()

        found = False
        with open("customerAccountInfo.txt", "w") as file:
            for line in lines:
                customer_data = line.strip().split(", ")
                if customer_data[1] == account_number and customer_data[2] == current_password:
                    customer_data[2] = new_password
                    updated_line = ", ".join(customer_data)
                    file.write(updated_line + "\n")
                    found = True
                else:
                    file.write(line)

        if not found:
            print("\nInvalid Account Number or Password\n")
            customerMenu(customer_data[0], account_number, customer_data[4])
            return

        print("\nPassword Updated Successfully!\n")
        customerMenu(customer_data[0], account_number, customer_data[4])
    except FileNotFoundError:
        print("\nCustomer account information file not found.\n")
        customerMenu(customer_data[0], account_number, customer_data[4])


mainMenu()