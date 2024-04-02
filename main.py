import mysql.connector

connection = mysql.connector.connect(user = "root", database = "example", password = "FireCarpet657@")
cursor = connection.cursor()
testQuery = ("SELECT * FROM online_banking")
cursor.execute(testQuery)

for item in cursor:
    print(item)

cursor.close()
connection.close()


account_list = {
    "personal":5738299
}

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
    y = 0
    for account in account_list:
        y += 1
        print(f"{y}: {account}")
    z = True
    while (z):
        account_name = input("Type the name of the account you would like to use: ")

        if account_name in account_list:
            account_password = int(input("Ok, what is the password for this account? "))
            if account_password == account_list.get(account_name):
                print("yay")
                z = False

            else:
                print("nay")
                z = False
        else:
            print("Please select from the accounts listed above.")

    
"""
if __name__ == "__main__":
    introduction()

"""