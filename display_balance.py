import utils
def display_balance():
    print(" ================== Display Balance =================")

    account_no = int(input("Enter your account number : "))
    pin = int(input("Enter your pin : "))
    if account_no in utils.transactions and pin == utils.transactions[account_no]['pin']:
        print("Your balance is: ",utils.transactions[account_no]['balance'])
    else:
        print("Invalid account number or pin.")