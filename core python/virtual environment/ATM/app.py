balance = 5000
pin = "1234"
transactions = []

def check_balance():
    print("\nYour balance is Rs.", balance)


def deposit():
    global balance
    amount = int(input("\nEnter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        transactions.append("Deposited Rs. " + str(amount))
        print("Money deposited successfully!")
    else:
        print("Invalid amount!")


def withdraw():
    global balance
    amount = int(input("\nEnter withdrawal amount: "))

    if amount > 0 and amount <= balance:
        balance = balance - amount
        transactions.append("Withdrawn Rs. " + str(amount))
        print("Please collect your cash!")
    else:
        print("Invalid amount or insufficient balance!")

entered_pin = input("Enter your ATM PIN: ")

if entered_pin == pin:
    print("\nWelcome to Python ATM!")

    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            check_balance()

        elif choice == 2:
            deposit()

        elif choice == 3:
            withdraw()

        elif choice == 4:
            print("Thank you for using Python ATM!")
            break

        else:
            print("Invalid choice!")

else:
    print("Incorrect PIN!")