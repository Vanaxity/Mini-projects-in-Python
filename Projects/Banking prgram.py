#python Banker
balance = 0 
is_running = True

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: $"))
    if amount < 0:
        print("That's not a valid amount")
    else:
        return amount

def withdraw():
    amount = float(input("Enter amount to be withdrawn"))
    if amount > balance:
        print("Insufficeient funds")
    elif amount < 0:
        print("That ain't right.")
    else:
        return amount
 

while is_running:
    print("Hello! I am your virtual Banker")
    print("--Please select one of the options--")
    print("1. Deposit")
    print("2 .Withdraw")
    print("3 .Show balance")
    print("4. Exit")

    choice = input("enter your choice. (please Type the number only cause im a robot gng)")

    if choice == '1':
        balance += deposit()
    elif choice == '2':
        balance -= withdraw()
    elif choice == '3':
        show_balance()
    elif choice == '4':
        print("Bye cuh see u later")
        is_running = False

    else:
        print("That ain't no valid choice")


