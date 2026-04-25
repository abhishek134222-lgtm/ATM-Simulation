from display_balance import display_balance
from deposited_money import deposited_money 
from withdraw_money import withdraw_money
from statement import statement


def main():
    print(" ================== Welcome to Abhishek's ATM =================")
    
    print("Enter 1 to check balance")
    print("Enter 2 to deposit money")
    print("Enter 3 to withdraw money")
    print("Enter 4 For Mini Statement")
    print("Enter 5 to Exit")
    while True:
        choice = int(input("Enter your choice : "))

        if choice == 1: display_balance()
        elif choice == 2: deposited_money()
        elif choice == 3: withdraw_money()
        elif choice == 4: statement()
        elif choice == 5: 
            print("Thank you for using Abhishek's ATM. Have a nice day!")
            break
        else: print("Invalid Choice. Please try again.")

main()