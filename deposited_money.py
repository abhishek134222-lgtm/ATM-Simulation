import utils
from access import access_account
def deposited_money():
    print(" ================== Deposit Money =================")

    access, account_no = access_account()
    if access:
        amount = int(input("Enter the amount to deposit : "))
        utils.transactions[account_no]['deposited_history'].append(amount)
        utils.transactions[account_no]['balance'] += amount
        print("Amount deposited successfully. Your new balance is: ", utils.transactions[account_no]['balance'])
    else:
        print("Invalid account number or pin.")