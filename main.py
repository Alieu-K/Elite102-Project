import mysql.connector

connection = mysql.connector.connect(user = "root", database = "example", password = "FireCarpet657@")
cursor = connection.cursor()
testQuery = 'SELECT * FROM online_banking'

cursor.reset

cursor.execute(testQuery)


for item in cursor:
    print(item)
 



special_charcters = "(''!@#$%^&*()_=+[]{\|;:/.,<>~`?}{)"

def introduction():
    print("\nQuick and Easy Bank")
    print("---------------------------------------------")
    name = input("Hello welcome to Quick and Easy Bank, what is your name? ")
    x = True
    while (x):
        account_status = input(f"Hello {name}, do you have an account already? ")

        if account_status == "yes" or account_status == "Yes":
            print("Ok, please select which account you want to use below.")
            select_account()
            x = False

        elif account_status == "no" or account_status == "No":
            print("Ok, lets get you with an account then.")
            make_account()
            x = False
        else:
            print("Please type yes or no")

def select_account():
    account_list = []
    y = 0
    cursor.execute("SELECT idOnline_Banking, account_name FROM online_banking")
    accounts = cursor.fetchall()
    for account in accounts:
        print(f"{account[0]}: {account[1]}")
        account_list.append(account[1])

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
                password = ''.join(password)

                if account_password == password:
                    print("yay")
                    z = False

                else:
                    password_tries -= 1
                    print(f"Please make sure you typed in your password correctly, you have {password_tries} left.")

            else:
                print("Please select from the accounts listed above.")

def make_account():
    account_name = input("What do you want the name of your account to be? No numbers or special charcters. ")

    if name_has_number(account_name) == False and name_has_special_char(account_name) == True:
    
        password_creation_check = True
        while(password_creation_check):
            account_password = input("Ok, now what do you want your password to be? ")

            if password_char_count(account_password):
                email_creation_check = True
                while(email_creation_check):
                    account_email = input("Ok, what email do you want to use for this account? We only accept gmails and hotmails however. ")

                    if email_char_check(account_email):
                        starting_total = 0.0
                        account_adding = (f"INSERT INTO online_banking (account_name, password, account_email, total_amount, latest_transaction) VALUE ('{account_name}', '{account_password}', '{account_email}', {starting_total}, 'N/A')")
                        cursor.execute(account_adding)
                        connection.commit()
                        
                        print("okay")
                        email_creation_check = False
                        password_creation_check = False
                    else:
                        print("Please make sure your email has an @gmail.com or a hotmail.com in it. ")  

            else:
                print("Please type a password that has an upper case letter, a special character, a number, and is between 8-25 characters long.")
        
    else:
        print("Please don't include numbers or special charcters in the name.")
        make_account()

def home_screen():
    pass

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

current_user = ''


if __name__ == "__main__":
    introduction()
    cursor.close()
    connection.close()
