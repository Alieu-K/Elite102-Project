import mysql.connector

connection = mysql.connector.connect(user = "root", database = "example", password = "FireCarpet657@")
cursor = connection.cursor()


def introduction():
    print("Quick and Easy Bank")
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
            #make_account()
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
    while (z):
        account_name = input("Type the name of the account you would like to use: ")

        if account_name in account_list:
            account_password = input("Ok, what is the password for this account? ")
            cursor.execute("SELECT password FROM online_banking")
            password = cursor.fetchone()
            password = ''.join(password)

            if account_password == password:
                print("yay")
                z = False

            else:
                print("nay")
                z = False
        else:
            print("Please select from the accounts listed above.")

def make_account():
    print("")


if __name__ == "__main__":
    introduction()
    cursor.close()
    connection.close()