import mysql.connector
import tkinter as tk
from tkinter import ttk

connection = mysql.connector.connect(user = "root", database = "example", password = "FireCarpet657@")
cursor = connection.cursor()
""""
testQuery = 'SELECT * FROM online_banking'

cursor.reset

cursor.execute(testQuery)

for item in cursor:
    print(item)
"""
special_charcters = "(''!@#$%^&*()_=+[]{\|;:/.,<>~`?}{)"


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

def clearFrame(frame):
    # destroy all widgets from frame
    for widget in frame.winfo_children():
        widget.destroy()
            

class main_loop(tk.Tk):    
    def __init__(self):
        super().__init__()

        self.title("Easy Banking")
        self.style = ttk.Style(self)
        self.geometry("1000x1000")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)    
        self.columnconfigure(2, weight=1)    
        self.columnconfigure(3, weight=1)    
        self.columnconfigure(4, weight=1)    


        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        frame0 = ttk.Frame(self)
        frame1 = ttk.Frame(self)

        frame0.grid(column=2, row=0)
        frame1.grid(column=2, row=1)

        frame2 = ttk.Frame(self)
        frame2.grid(column=1, row=1)
        frame3 = ttk.Frame(self)
        frame3.grid(column=2, row=2)

        user_logged_in = ''
        back_button = False


        ttk.Label(frame0, text="Quick and Easy Bank", font=("Arial", 40)).grid(sticky= 'n')
        ttk.Label(frame0, text="---------------------------------------------", font=("Arial", 40)).grid()

        # Main Functions
        def login_page(logged_user):
            user_input = tk.StringVar(self)

            login_button = ttk.Button(frame1, text="Login", command = lambda: select_account(back_button), width=75).grid(sticky= 'n')
            sign_up_button = ttk.Button(frame1, text="Sign Up", command= lambda: make_account(user_logged_in), width=75).grid(row = 1)
#
        def log_out():
            self.destroy()
#       
        def return_home(username):
            home_screen(username)
#
        def home_screen(user_logged_in):
            back_button = True
            username = user_logged_in
            clearFrame(frame0)
            clearFrame(frame1)

            
            self.rowconfigure(2, weight=1)
            self.rowconfigure(1, weight=1)
   

            ttk.Label(frame0, text="Quick and Easy Bank", font=("Arial", 40)).grid(sticky= 'n')
            ttk.Label(frame0, text="---------------------------------------------", font=("Arial", 40)).grid()
            ttk.Label(frame0, text = f"Current Account: {username}", font=('Arial', 15)).grid(sticky='n')

            #Functions
            Check_balance = ttk.Button(frame0, text="Check Balance", command= lambda: check_balance(username), width=25).grid(row = 2, sticky='w')
            Deposit = ttk.Button(frame0, text="Deposit", command= lambda: deposit(user_logged_in), width=25).grid(row = 3, sticky='w')
            Withdraw = ttk.Button(frame0, text="Withdraw", command= lambda: withdraw(user_logged_in), width=25).grid(row = 4, sticky='w')
            Create_Account = ttk.Button(frame0, text="Create Account", command= lambda: make_account(username), width=25).grid(row = 5, sticky='w')
            Delete_Account = ttk.Button(frame0, text="Delete Account", command= lambda: delete_account(user_logged_in), width=25).grid(row = 2, sticky='e')
            Modify_Account = ttk.Button(frame0, text="Modify Account", command= lambda: modify_account(), width=25).grid(row = 3, sticky='e')
            Switch_Account = ttk.Button(frame0, text="Switch Account", command= lambda: select_account(back_button), width=25).grid(row = 4, sticky='e')
            Wire_Transfer = ttk.Button(frame0, text="Wire Transfer", command= lambda: wire_transfer(), width=25).grid(row = 5, sticky='e')
            Log_Out = ttk.Button(frame0, text="Log Out", command= lambda: log_out(), width=25).grid(sticky='s')
#
        def deposit(username):
            deposit_number = tk.DoubleVar(self)
            clearFrame(frame0)
            clearFrame(frame1)
            clearFrame(frame2)
            clearFrame(frame3)
            self.rowconfigure(1, weight=1)


            cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{username}'")
            current_amount = cursor.fetchone()

            ttk.Label(frame0, text="Deposit", font=("Arial", 40)).grid(sticky= 'n')
            ttk.Label(frame0, text="---------------------------------------------", font=("Arial", 40)).grid()

            ttk.Label(frame0, text=f"Balance: {current_amount[0]}", font=('Arial', 20)).grid(sticky='s')
            ttk.Label(frame0, text=f"How much would you like to deposit?", font=('Arial', 15)).grid(sticky='s')

            ttk.Entry(frame0, textvariable=deposit_number, width=25).grid(row = 5, sticky='s')
            ttk.Button(frame0, text="Confirm", command=lambda: calculate(deposit_number.get())).grid(row = 9)

            def calculate(deposit_amount):
                try:
                    if deposit_amount >= 1.0:
                        new_amount = current_amount[0] + deposit_amount
                        cursor.execute(f"UPDATE online_banking SET total_amount = {new_amount} WHERE account_name = '{username}'")
                        cursor.execute(f"UPDATE online_banking SET latest_transaction = 'deposit of {deposit_amount} to the account' WHERE account_name = '{username}'")
                        cursor.execute(f"SELECT * FROM online_banking WHERE account_name = '{username}'")
                        account_info = cursor.fetchone()
                        connection.commit()
                        cursor.reset()
                        return_home(username)
                    else:
                        clearFrame(frame0)
                        ttk.Label(frame0, text=f"Balance: {current_amount[0]}", font=('Arial', 20)).grid(sticky='n')
                        ttk.Label(frame0, text=f"Please make sure that you're depsoting amounts greater than 1.", font=('Arial', 15)).grid(sticky='n')
                        ttk.Entry(frame0, textvariable=deposit_number)
                        ttk.Button(frame0, text="Confirm", command=lambda: calculate(deposit_number))
            
                except ValueError:
                    clearFrame(frame0)
                    ttk.Label(frame0, text=f"Balance: {current_amount[0]}", font=('Arial', 20)).grid(sticky='n')
                    ttk.Label(frame0, text=f"Please type in a number for the depsoit.", font=('Arial', 15)).grid(sticky='n')
#
        def withdraw(username):
            withdraw_number = tk.DoubleVar(self)
            clearFrame(frame0)
            clearFrame(frame1)
            clearFrame(frame2)
            clearFrame(frame3)
            self.rowconfigure(1, weight=1)


            cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{username}'")
            current_amount = cursor.fetchone()

            ttk.Label(frame0, text="Withdraw", font=("Arial", 40)).grid(sticky= 'n')
            ttk.Label(frame0, text="---------------------------------------------", font=("Arial", 40)).grid()

            ttk.Label(frame0, text=f"Balance: {current_amount[0]}", font=('Arial', 20)).grid(sticky='s')
            ttk.Label(frame0, text=f"How much would you like to withdraw?", font=('Arial', 15)).grid(sticky='s')

            ttk.Entry(frame0, textvariable=withdraw_number, width=25).grid(row = 5, sticky='s')
            ttk.Button(frame0, text="Confirm", command=lambda: calculate(withdraw_number.get())).grid(row = 9)

            def calculate(withdraw_amount):
                try:
                    if withdraw_amount >= 1.0 and current_amount[0] - withdraw_amount >= 1.0:
                        new_amount = current_amount[0] - withdraw_amount
                        cursor.execute(f"UPDATE online_banking SET total_amount = {new_amount} WHERE account_name = '{username}'")
                        cursor.execute(f"UPDATE online_banking SET latest_transaction = 'deposit of {withdraw_amount} to the account' WHERE account_name = '{username}'")
                        cursor.execute(f"SELECT * FROM online_banking WHERE account_name = '{username}'")
                        account_info = cursor.fetchone()
                        connection.commit()
                        cursor.reset()
                        return_home(username)
                    else:
                        clearFrame(frame0)
                        ttk.Label(frame0, text=f"Balance: {current_amount[0]}", font=('Arial', 20)).grid(sticky='n')
                        ttk.Label(frame0, text=f"Please make sure that you're withdrawing amounts greater than 1 as well as leaving at least $1 in the account.", font=('Arial', 15)).grid(sticky='n')
                        ttk.Entry(frame0, textvariable=withdraw_amount)
                        ttk.Button(frame0, text="Confirm", command=lambda: calculate(withdraw_amount))
            
                except ValueError:
                    clearFrame(frame0)
                    ttk.Label(frame0, text=f"Balance: {current_amount[0]}", font=('Arial', 20)).grid(sticky='n')
                    ttk.Label(frame0, text=f"Please type in a number for the withdrawl.", font=('Arial', 15)).grid(sticky='n')

        def delete_account(logged_user):
            clearFrame(frame0)
            clearFrame(frame1)
            clearFrame(frame2)
            clearFrame(frame3)
            account_list = [] 
            account_list.clear()   
            testQuery = 'SELECT * FROM online_banking'
            cursor.reset
            cursor.execute(testQuery)

            for item in cursor:
                account_list.append(item[1])

            ttk.Label(frame0, text="Delete", font=("Arial", 40)).grid(sticky= 'n')
            ttk.Label(frame0, text="---------------------------------------------", font=("Arial", 40)).grid()

            ttk.Label(frame0, text="Would you like to delete this account?", font=('Arial', 20)).grid(sticky='s')

            ttk.Button(frame0, text="Yes", command=lambda: remove_current(logged_user)).grid(row = 9, sticky='w')
            ttk.Button(frame0, text="No", command=lambda: home_screen(logged_user)).grid(row = 9, sticky='e')

            def remove_current(logged_user):
                x = 0
                for item in account_list:
                    x += 1
                
                if x > 1:
                    account_delete = f'DELETE FROM online_banking WHERE account_name = "{logged_user}"'
                    cursor.execute(account_delete)
                    connection.commit()
                    select_account(logged_user)
                
                else:
                    clearFrame(frame0)
                    ttk.Label(frame0, text="Delete", font=("Arial", 40)).grid(sticky= 'n')
                    ttk.Label(frame0, text="---------------------------------------------", font=("Arial", 40)).grid()

                    ttk.Label(frame0, text="Please make sure that you have two account before one is deleted.", font=('Arial', 20)).grid(sticky='s')

                    ttk.Button(frame0, text="Yes", command=lambda: remove_current(logged_user)).grid(row = 9, sticky='w')
                    ttk.Button(frame0, text="No", command=lambda: home_screen(logged_user)).grid(row = 9, sticky='e')
#
        def select_account(back_button):
            clearFrame(frame0)
            clearFrame(frame1)

            frame2 = ttk.Frame(self)
            frame2.grid(column=2, row=1)

            frame3 = ttk.Frame(self)
            frame3.grid(column=2, row=2)


            account_list = []
            cursor.execute("SELECT idOnline_Banking, account_name FROM online_banking")
            accounts = cursor.fetchall()
            for account in accounts:
                account_list.append(account[1])


            clearFrame(frame2)

            account_name = tk.StringVar(self)
            account_password = tk.StringVar(self)

            ttk.Label(frame0, text="Log In", font=("Arial", 40)).grid(sticky= 'n')
            ttk.Label(frame0, text="---------------------------------------------", font=("Arial", 40)).grid()

            ttk.Label(frame2, text = "Username: ", font=('Arial', 15)).grid(row = 1, sticky='w')
            ttk.Label(frame2, text = "Password: ", font=('Arial', 15)).grid(row = 3, sticky='w')

            ttk.Entry(frame2, textvariable = account_name, width=75).grid(row = 1, column = 1, sticky='e')
            ttk.Entry(frame2, textvariable = account_password, width=75).grid(row = 3, column = 1, sticky='e')

            ttk.Button(frame3, text="Confirm", command= lambda: check_credentials(), width=20).grid(sticky='n')

            def check_credentials():
                if account_name.get() in account_list:
                    cursor.execute(f"SELECT password FROM online_banking WHERE account_name = '{account_name.get()}'")
                    password = cursor.fetchone()
                    cursor.reset()
                    password = ''.join(password)

                    if account_password.get() == password:
                        logged_user = account_name.get()
                        user_logged_in = account_name.get()
                        clearFrame(frame2)
                        clearFrame(frame3)
                        home_screen(user_logged_in)

                    else:
                        clearFrame(frame3)
                        ttk.Button(frame3, text="Confirm", command= lambda: check_credentials(), width=20).grid()
                        ttk.Label(frame3, text = f"Please make sure your username or password is correct.", font=('Arial', 15)).grid(sticky='n')

                else:
                    clearFrame(frame3)
                    ttk.Button(frame3, text="Confirm", command= lambda: check_credentials(), width=20).grid()
                    ttk.Label(frame3, text = f"Please make sure your username or password is correct.", font=('Arial', 15)).grid(sticky='n')
#
        def make_account(logged_user):
                clearFrame(frame0)
                clearFrame(frame1)
                clearFrame(frame3)

                name_input = tk.StringVar(self)
                password_input = tk.StringVar(self)
                email_input = tk.StringVar(self)


                frame2 = ttk.Frame(self)
                frame2.grid(column=2, row=1)

                cursor.reset

                current_usernames = []
                current_passwords = []
                current_emails = []

                ttk.Label(frame0, text="Create a New Account", font=("Arial", 40)).grid(sticky= 'n')
                ttk.Label(frame0, text="---------------------------------------------", font=("Arial", 40)).grid()


                def name_check(account_name):
                    clearFrame(frame2)
                    if name_has_number(account_name) == False and name_has_special_char(account_name) == True and account_name not in current_usernames:
                        cursor.reset
                        taken_passwords = ("SELECT password FROM online_banking")
                        cursor.execute(taken_passwords)
                        for password in cursor:
                            current_passwords.append(password[0])

                        ttk.Label(frame2, text = "What do you want the password of your account to be? Make sure it's 8-25 characters long with at least a capital letter, number, and special charcter without any spaces.", font=('Arial', 15)).grid(sticky='n')
                        ttk.Entry(frame2, textvariable=password_input, width=25).grid(sticky='s')
                        ttk.Button(frame2, text="Confirm", command = lambda: password_check(password_input.get()), width=10).grid()

                    else:
                        clearFrame(frame2)
                        ttk.Label(frame2, text = "Please type in a name that doesn't have a special charcter or number in it.", font=('Arial', 15)).grid(sticky='n')
                        ttk.Entry(frame2, textvariable=name_input, width = 25).grid(sticky='s')
                        ttk.Button(frame2, text="Confirm", command = lambda: name_check(name_input.get()), width=10).grid()
     
                def password_check(account_password):
                    clearFrame(frame2)
                    if password_char_count(account_password) and account_password not in current_passwords:
                        cursor.reset
                        taken_emails = ("SELECT account_email FROM online_banking")
                        cursor.execute(taken_emails)
                        for email in cursor:
                            current_emails.append(email[0])

                        ttk.Label(frame2, text = "What do you want the email of your account to be? We only accept hotmails and gmails.", font=('Arial', 15)).grid(sticky='n')
                        ttk.Entry(frame2, textvariable=email_input, width=25).grid(sticky='s')
                        ttk.Button(frame2, text="Confirm", command = lambda: email_check(email_input.get()), width=10).grid()
                    
                    else:
                        clearFrame(frame2)
                        ttk.Label(frame2, text = "Please type in a Password. Make sure it has a capital letter, number, and a special charcter in it.", font=('Arial', 15)).grid(sticky='n')
                        ttk.Entry(frame2, textvariable=password_input, width=25).grid(sticky='s')
                        ttk.Button(frame2, text="Confirm", command = lambda: password_check(password_input.get()), width=10).grid()  

                def email_check(account_email):
                    clearFrame(frame2)
                    if email_char_check(account_email) and account_email not in current_emails:
                        account_name = name_input.get()
                        account_password = password_input.get()

                        starting_total = 0.0
                        account_adding = (f"INSERT INTO online_banking (account_name, password, account_email, total_amount, latest_transaction) VALUE ('{account_name}', '{account_password}', '{account_email}', {starting_total}, 'N/A')")
                        cursor.execute(account_adding)
                        connection.commit()
                        print("okay")
                        logged_user = account_name


                        current_usernames.clear()
                        current_passwords.clear()
                        current_emails.clear()
                        home_screen(logged_user)

                    else:
                        clearFrame(frame2)
                        ttk.Label(frame2, text = "This email is already in use or it is not a hotmail.com or gmail.com email.", font=('Arial', 15)).grid(sticky='n')
                        ttk.Entry(frame2, textvariable=email_input, width=25).grid(sticky='s')
                        ttk.Button(frame2, text="Confirm", command = lambda: email_check(email_input.get()), width=10).grid() 


                taken_names = ("SELECT account_name FROM online_banking")
                cursor.execute(taken_names)
                for name in cursor:
                    capitalize = name[0].upper()
                    lowercase = name[0].lower()
                    current_usernames.append(name[0])
                    current_usernames.append(capitalize)
                    current_usernames.append(lowercase)

                ttk.Label(frame2, text = "What do you want the name of your account to be? No numbers or special charcters.", font=('Arial', 15)).grid(sticky='n')
                ttk.Entry(frame2, textvariable=name_input, width = 25).grid(sticky='s')
                ttk.Button(frame2, text="Confirm", command = lambda: name_check(name_input.get()), width=10).grid()

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
                    z = True
                    password_tries = 3
                    while (z):
                        if password_tries == 0:
                            print("You have run out of password tries, you will be kicked out now.")
                            z = False
                        if(z):                
                            account_password = input("Ok, what is the password for this account? ")
                            cursor.execute(f"SELECT password FROM online_banking WHERE account_name = '{account_switch}'")
                            password = cursor.fetchone()
                            cursor.reset()
                            password = ''.join(password)

                            if account_password == password:
                                logged_user = account_switch
                                account_list.clear()
                                get_switch = False
                                z = False
                                return logged_user

                            else:
                                password_tries -= 1
                                print(f"Please make sure you typed in your password correctly, you have {password_tries} left.")


                
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
            action_loop = True
            while(action_loop):
                action = input("What would you like to do, deposit or withdraw money? ")

                if action == "deposit" or action == "Deposit":
                    account_get = True
                    while(account_get):
                        account_select = input("What account do you want to deposit into? ")

                        if account_select in account_list and account_select != logged_user:
                            cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{account_select}'")
                            deposit = cursor.fetchone()
                            deposit = deposit[0]

                            cursor.reset()

                            cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{logged_user}'")
                            deposit_from = cursor.fetchone()
                            deposit_from = deposit_from[0]
                            deposit_get = True 
                            while(deposit_get):
                                try:
                                    deposit_amount = float(input("How much do you want to deposit into this account? "))
                                    if (deposit_from - deposit_amount) >= 1:

                                        transfer_amount = deposit_from - deposit_amount
                                        deposit_from = deposit_from - deposit_amount

                                        deposit = deposit + transfer_amount
                                        cursor.execute(f"UPDATE online_banking SET total_amount = {deposit_from} WHERE account_name = '{logged_user}'")
                                        cursor.execute(f"UPDATE online_banking SET total_amount = {deposit} WHERE account_name = '{account_select}'")

                                        cursor.execute(f"UPDATE online_banking SET latest_transaction = 'transfer of {deposit_amount} into {account_select}' WHERE account_name = '{logged_user}'")
                                        cursor.execute(f"UPDATE online_banking SET latest_transaction = 'transfer of {deposit_amount} from {logged_user}' WHERE account_name = '{account_select}'")


                                        action_loop = False
                                        account_get = False
                                        deposit_get = False

                                        connection.commit()
                                    else:
                                        print("Please make sure you are not over withdrawing funds from an account.")

                                except ValueError:
                                    print("Please type in a number showing how much you would like to transfer.")
                        else:
                            print("Please type in an account name from the list above. Make sure it is not the current active account.")
                
                elif action == "withdraw" or action == "Withdraw":
                    account_get = True
                    while(account_get):
                        account_select = input("What account do you want to withdraw from? ")

                        if account_select in account_list and account_select != logged_user:
                            cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{account_select}'")
                            withdraw_from = cursor.fetchone()
                            withdraw_from = withdraw_from[0]

                            cursor.reset()

                            cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{logged_user}'")
                            withdraw_into = cursor.fetchone()
                            withdraw_into = withdraw_into[0]

                            withdraw_get = True
                            while(withdraw_get):
                                try:
                                    withdraw_amount = float(input("How much do you want to withdraw from this account? "))
                                    if (withdraw_into + withdraw_amount) >= 1:

                                        withdraw_into = withdraw_into + withdraw_amount
                                        withdraw_from = withdraw_from - withdraw_amount

                                        cursor.execute(f"UPDATE online_banking SET total_amount = {withdraw_into} WHERE account_name = '{logged_user}'")
                                        cursor.execute(f"UPDATE online_banking SET total_amount = {withdraw_from} WHERE account_name = '{account_select}'")

                                        cursor.execute(f"UPDATE online_banking SET latest_transaction = 'transfer of {withdraw_amount} from {account_select}' WHERE account_name = '{logged_user}'")
                                        cursor.execute(f"UPDATE online_banking SET latest_transaction = 'transfer of {withdraw_amount} into {logged_user}' WHERE account_name = '{account_select}'")

                                        action_loop = False
                                        account_get = False
                                        withdraw_get = False

                                        connection.commit()
                                    else:
                                        print("Please make sure you are not over withdrawing funds from an account.")


                                except ValueError:
                                    print("Please type in a number showing how much you would like to transfer.")
                        else:
                            print("Please type in an account name from the list above. Make sure it is not the current active account")
                
                else:
                    print("Please type in withdraw or deposit in the text box")
#
        def check_balance(logged_user):
            clearFrame(frame0)
            clearFrame(frame3)
            cursor.execute(f"SELECT total_amount FROM online_banking WHERE account_name = '{logged_user}'")
            balance = cursor.fetchone()
            ttk.Label(frame0, text = f"Total Balance: {balance[0]}.", font=('Arial', 15)).grid(sticky='n')
            ttk.Button(frame0, text="Back", command= lambda: home_screen(logged_user), width=25).grid(row = 5, sticky='s')




        login_page(user_logged_in)
        # home_screen(user_logged_in)

        





if __name__ == "__main__":
    logged_in = ''
    app = main_loop()
    app.mainloop()

    cursor.close()
    connection.close()
