import utils
from access import access_account
def display_balance():
    print(" ================== Display Balance =================")

    access, account_no = access_account()

    if access:
        print("Your balance is: ",utils.transactions[account_no]['balance'])
    else:
        print("Invalid account number or pin.")