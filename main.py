import mysql.connector

connection = mysql.connector.connect(user = "root", database = "example", password = "FireCarpet657@")
cursor = connection.cursor()
""""
testQuery = 'SELECT * FROM online_banking'

cursor.reset

cursor.execute(testQuery)

for item in cursor:
    print(item)
"""
user_logged_in = ''
special_charcters = "(''!@#$%^&*()_=+[]{\|;:/.,<>~`?}{)"

# Main Functions
def login_page(logged_user):
    x = True
    while (x):
        account_status = input(f"Hello {name}, do you have an account already? ")

        if account_status == "yes" or account_status == "Yes":
            print("Ok, please select which account you want to use below.")
            logged_user = select_account(logged_user)
            x = False
            return logged_user

        elif account_status == "no" or account_status == "No":
            print("Ok, lets get you with an account then.")
            logged_user = make_account(logged_user)
            x = False
            return logged_user
        else:
            print("Please type yes or no")

def home_screen(user_logged_in):
    function_loop = True
    while(function_loop):
        sorting_number = 1
        print("---------------------------------------------")
        print(f"Account: {user_logged_in}\n")

        action_list = ['Check Balance', 'Deposit', 'Withdraw', 'Create Account', 'Delete Account', 'Modify Account', 'Switch Accounts', 'Wire Transfer', 'Log out']
        for action in action_list:
            print(f"{sorting_number}: {action}")
            print("-------------------------")
            sorting_number += 1

        try:
            actions = int(input(f"\nOk {name}, type in the number that corresponds to the action you would like to do today. "))
        except ValueError:
            actions = 0

        if actions == 1:
            print("---------------------------------------------")
            cursor.execute(f"SELECT * FROM online_banking WHERE account_name = '{user_logged_in}'")
            account_info = cursor.fetchone()
            print(f"You have {account_info[4]} in your account now.")
            if account_info == 'N/A':
                print("No activity as of right now.")
            else:
                print(f"Your latest transaction was a {account_info[5]}")
                
            cursor.reset()

        elif actions == 2:
            deposit(user_logged_in)

        elif actions == 3:
            withdraw(user_logged_in)

        elif actions == 4:
            user_logged_in = make_account(user_logged_in)

        elif actions == 5:
            delete_account(user_logged_in)

        elif actions == 6:
            user_logged_in = modify_account(user_logged_in)

        elif actions == 7:
            user_logged_in = switch_accounts(user_logged_in)

        elif actions == 8:
            wire_transfer(user_logged_in)

        elif actions == 9:
            print("Logged out")
            function_loop = False

        else:
            print("Please type the number that corresponds to the action you would like to do.")

def deposit(username):

    print("---------------------------------------------")
    cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{username}'")
    current_amount = cursor.fetchone()
    print(f"Balance: {current_amount[0]}")
    try_deposit = True
    while(try_deposit):
        try:
            deposit_amount = float(input("How much would you like to deposit? "))

            if deposit_amount >= 1:
                new_amount = current_amount[0] + deposit_amount
                cursor.execute(f"UPDATE online_banking SET total_amount = {new_amount} WHERE account_name = '{username}'")
                cursor.execute(f"UPDATE online_banking SET latest_transaction = 'deposit of {deposit_amount} to the account' WHERE account_name = '{username}'")

                cursor.execute(f"SELECT * FROM online_banking WHERE account_name = '{username}'")
                account_info = cursor.fetchone()
                print(f"You have {account_info[4]} in your account now.")
                connection.commit()
                cursor.reset()
                try_deposit = False
            else:
                print("Please make sure the amount you want to deposit is greater than 1.")



        except ValueError:
            print("Please type in a numerical amount. Be sure to include .0 at the of whole numbers. ")

def withdraw(username):
    print("---------------------------------------------")
    cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{username}'")
    current_amount = cursor.fetchone()
    print(f"Balance: {current_amount[0]}")
    try_withdraw = True
    while(try_withdraw):
        try:
            withdraw_amount = float(input("How much would you like to withdraw? "))

            if withdraw_amount >= 1:
                cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{username}'")
                current_amount = cursor.fetchone()
                new_amount = current_amount[0] - withdraw_amount

                if new_amount >= 1:
                    cursor.execute(f"UPDATE online_banking SET total_amount = {new_amount} WHERE account_name = '{username}'")
                    cursor.execute(f"UPDATE online_banking SET latest_transaction = 'withdrawl of {withdraw_amount} to the account' WHERE account_name = '{username}'")

                    cursor.execute(f"SELECT * FROM online_banking WHERE account_name = '{username}'")
                    account_info = cursor.fetchone()
                    print(f"You have {account_info[4]} in your account now.")
                    connection.commit()
                    cursor.reset()
                    try_withdraw = False
                else:
                    print("The total balance in your account has to be greater or equal to 1, please try withdrawing a smaller amount.")
            else:
                print("Please make sure the amount you want to withdraw is greater than 1.")



        except ValueError:
            print("Please type in a numerical amount. Be sure to include .00 at the of whole numbers. ")

def delete_account(logged_user):
    account_list = [] 
    try_delete = True
    while(try_delete):
        account_list.clear()   
        testQuery = 'SELECT * FROM online_banking'
        cursor.reset
        cursor.execute(testQuery)

        for item in cursor:
            print("---------------------------------------------")
            print(f"Account Name: {item[1]}")
            print(f"Amount: {item[4]}")
            print(f"Latest Transaction: {item[5]}")
            account_list.append(item[1])

        print("---------------------------------------------")
        selected_account = input("What's the name of the account you would like to delete? ")
        
        if selected_account == logged_user:
            print("Please switch users before deleting an account.")
            try_delete = False
            account_list.clear()
        
        elif selected_account in account_list:
            account_delete = f'DELETE FROM online_banking WHERE account_name = "{selected_account}"'
            cursor.execute(account_delete)
            connection.commit()
            print(f"The account {selected_account} has been succesfully deleted.")
            try_delete = False
            account_list.clear()

        elif selected_account == 'home' or selected_account == 'Home':
            try_delete = False
    
        else:
            print("Please select an account from the list or type home to go back to the home screen.")

def select_account(logged_user):
    account_list = []
    cursor.execute("SELECT idOnline_Banking, account_name FROM online_banking")
    accounts = cursor.fetchall()
    print("---------------------------------------------")
    for account in accounts:
        print(f"{account[0]}: {account[1]}")
        account_list.append(account[1])
    print("---------------------------------------------")

    z = True
    password_tries = 3
    while (z):
        if password_tries == 0:
            print("You have run out of password tries, you will be kicked out now.")
            z = False
        if(z):
            account_name = input("Type the name of the account you would like to use: ")
        
            if account_name in account_list:

                account_password = input("Ok, what is the password for this account? ")
                cursor.execute(f"SELECT password FROM online_banking WHERE account_name = '{account_name}'")
                password = cursor.fetchone()
                cursor.reset()
                password = ''.join(password)

                if account_password == password:
                    logged_user = account_name
                    z = False
                    return logged_user

                else:
                    password_tries -= 1
                    print(f"Please make sure you typed in your password correctly, you have {password_tries} left.")

            else:
                print("Please select from the accounts listed above.")

def make_account(logged_user):
    username_creation_check = True

    while(username_creation_check):
        cursor.reset
        current_usernames = []
        taken_names = ("SELECT account_name FROM online_banking")
        cursor.execute(taken_names)
        for name in cursor:
            capitalize = name[0].upper()
            lowercase = name[0].lower()
            current_usernames.append(name[0])
            current_usernames.append(capitalize)
            current_usernames.append(lowercase)

        account_name = input("What do you want the name of your account to be? No numbers or special charcters. ")
        if name_has_number(account_name) == False and name_has_special_char(account_name) == True and account_name not in current_usernames:
            password_creation_check = True

            while(password_creation_check):
                cursor.reset
                current_passwords = []
                taken_passwords = ("SELECT password FROM online_banking")
                cursor.execute(taken_passwords)
                for password in cursor:
                    current_passwords.append(password[0])

                account_password = input("Ok, now what do you want your password to be? ")

                if password_char_count(account_password) and account_password not in current_passwords:
                    email_creation_check = True
                    while(email_creation_check):
                        cursor.reset
                        current_emails = []
                        taken_emails = ("SELECT account_email FROM online_banking")
                        cursor.execute(taken_emails)
                        for email in cursor:
                            current_emails.append(email[0])

                        account_email = input("Ok, what email do you want to use for this account? However, we only accept gmails and hotmails. ")

                        if email_char_check(account_email) and account_email not in current_emails:
                            starting_total = 0.0
                            account_adding = (f"INSERT INTO online_banking (account_name, password, account_email, total_amount, latest_transaction) VALUE ('{account_name}', '{account_password}', '{account_email}', {starting_total}, 'N/A')")
                            cursor.execute(account_adding)
                            connection.commit()
                            print("okay")
                            logged_user = account_name

                            email_creation_check = False
                            password_creation_check = False
                            username_creation_check = False

                            current_usernames.clear()
                            current_passwords.clear()
                            current_passwords.clear()
                        else:
                            print("Please make sure your email has an @gmail.com or a hotmail.com in it. ")  

                else:
                    print("Please type a password that has an upper case letter, a special character, a number, and is between 8-25 characters long.")
            
        else:
            print("Please don't include numbers or special charcters in the name. There may also be an account with this name already.")

    return logged_user       

def modify_account(logged_user):
    account_details = []

    print_account = f"SELECT * FROM online_banking WHERE account_name = '{logged_user}'"
    cursor.execute(print_account)
    for item in cursor:
        print("---------------------------------------------")
        print(f"Name: {item[1]}")
        print(f"Password: {item[2]}")
        print(f"Email: {item[3]}")
        print("---------------------------------------------")
        account_details.append((item[1], item[2], item[3]))
    
    modification = input("Type in the field you would like to modify about this account. ")
    get_modify = True

    while(get_modify):
        if modification == "name" or modification == "Name":
            get_name = True
            while(get_name):
                string_count = 0
                name_modify = input("What would you like for the name of this account to be? ")
                for char in name_modify:
                    string_count += 1
                if string_count >= 3 and string_count <= 25 and name_has_number(name_modify) == False and name_has_special_char(name_modify):

                    modify = f"UPDATE online_banking SET account_name = '{name_modify}' WHERE account_name = '{logged_user}'"
                    cursor.execute(modify)
                    connection.commit()
                    cursor.reset

                    cursor.execute(print_account)
                    for item in cursor:
                        print("---------------------------------------------")
                        print(f"Name: {item[1]}")
                        print(f"Password: {item[2]}")
                        print(f"Email: {item[3]}")
                    logged_user = name_modify
                    get_name = False
                    get_modify = False
                    return logged_user

                else:
                    print("Please type a name that is between 3-25 charcters long. Spaces count and no numbers.")
            
        elif modification == "password" or modification == "Password":
            get_password = True
            
            while(get_password):
                password_modify = input("What would you like for the password of this account to be? ")
                
                if password_char_count(password_modify):
                    modify = f"UPDATE online_banking SET password = '{password_modify}' WHERE account_name = '{logged_user}'"
                    cursor.execute(modify)
                    connection.commit()
                    cursor.reset

                    cursor.execute(print_account)
                    for item in cursor:
                        print("---------------------------------------------")
                        print(f"Name: {item[1]}")
                        print(f"Password: {item[2]}")
                        print(f"Email: {item[3]}")
                    get_password = False
                    get_modify = False
                    return logged_user

                else:
                    print("Please type a password that has an upper case letter, a special character, a number, and is between 8-25 characters long.")
            
        elif modification == "email" or modification == "email":
            get_email = True
            
            while(get_email):
                email_modify = input("What would you like for the email of this account to be? ")
                
                if email_char_check(email_modify):
                    modify = f"UPDATE online_banking SET account_email = '{email_modify}' WHERE account_name = '{logged_user}'"
                    cursor.execute(modify)
                    connection.commit()
                    cursor.reset

                    cursor.execute(print_account)
                    for item in cursor:
                        print("---------------------------------------------")
                        print(f"Name: {item[1]}")
                        print(f"Password: {item[2]}")
                        print(f"Email: {item[3]}")
                    get_email = False
                    get_modify = False
                    return logged_user

                else:
                    print("Please make sure your email has an @gmail.com or a hotmail.com in it. ")   

        else:
            print("Please type in email, name, or password to modify one of them.")

def switch_accounts(logged_user):
    account_list = []
    cursor.execute("SELECT idOnline_Banking, account_name FROM online_banking")
    accounts = cursor.fetchall()
    print("---------------------------------------------")
    for account in accounts:
        print(f"{account[0]}: {account[1]}")
        account_list.append(account[1])
    print("---------------------------------------------")
    get_switch = True

    while(get_switch):
        account_switch = input("What account would you like to switch to? ")
    
        if account_switch in account_list:
            logged_user = account_switch
            account_list.clear()
            get_switch = False
            return logged_user

        
        elif account_switch == 'cancel' or account_switch == 'Cancel':
            get_switch = False
            account_list.clear()
            return logged_user

        
        else:
            print("Please select an account in the list above or type cancel to exit out.")

def wire_transfer(logged_user):
    account_list = []
    cursor.execute("SELECT idOnline_Banking, account_name FROM online_banking")
    accounts = cursor.fetchall()
    print("---------------------------------------------")
    for account in accounts:
        print(f"{account[0]}: {account[1]}")
        account_list.append(account[1])
    print("---------------------------------------------")

    action = input("What would you like to do, deposit or withdraw money? ")

    if action == "deposit" or action == "Deposit":
        account_select = input("What account do you want to deposit into? ")

        if account_select in account_list:
            cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{account_select}'")
            deposit = cursor.fetchone()
            deposit = deposit[0]

            cursor.reset()

            cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{logged_user}'")
            deposit_from = cursor.fetchone()
            deposit_from = deposit_from[0]

            try:
                deposit_amount = int(input("How much do you want to deposit into this account? "))
                if (deposit_from - deposit_amount) >= 1:

                    transfer_amount = deposit_from - deposit_amount
                    deposit_from = deposit_from - deposit_amount

                    deposit = deposit + transfer_amount
                    breakpoint()
                    cursor.execute(f"UPDATE online_banking SET total_amount = {deposit_from} WHERE account_name = '{logged_user}'")
                    cursor.execute(f"UPDATE online_banking SET total_amount = {deposit} WHERE account_name = '{account_select}'")

                    connection.commit()






            except ValueError:
                pass


        else:
            print("Please type in an account name.")


    elif action == "withdraw" or action == "Withhdraw":
        pass
    else:
        print("Please type in withdraw or deposit in the text box")

# Background Checks
def name_has_number(input_string):
    return any(char.isdigit() for char in input_string)
def name_has_special_char(input_string):
    char_check = True
    for char in input_string:
        if char in special_charcters:
            char_check = False
    return char_check
def password_char_count(input_string):
    char_length = 0
    upper_count = 0
    special_char_count = 0
    number_count = 0
    space_count = 0

    for char in input_string:
        char_length += 1
        if char.isupper():
            upper_count += 1
        if char in special_charcters:
            special_char_count += 1
        if char.isdigit():
            number_count += 1
        if char == " ":
            space_count = 1


    if space_count ==  1:
        return False
    elif char_length >= 8 and char_length <= 25 and upper_count >= 1 and special_char_count >= 1 and number_count >= 1: 
        return True
    else:
        return False
def email_char_check(input_string):   
    atCount = 0      
    if '@hotmail.com' in input_string or '@gmail.com' in input_string:
        if input_string[-1] == "m" and input_string[-2] == "o" and input_string[-3] == 'c':
            atCount += 1
    
    if atCount == 1: 
        return True
    else: 
        return False

# Test Password BestPassword1234@

if __name__ == "__main__":
    print("\nQuick and Easy Bank")
    print("---------------------------------------------")
    name = input("Hello welcome to Quick and Easy Bank, what is your name? ")
    user_logged_in = login_page(user_logged_in)

    home_screen(user_logged_in)

    cursor.close()
    connection.close()
