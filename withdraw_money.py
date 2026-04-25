import utils
from access import access_account
def withdraw_money():
    print(" ================== Withdraw Money =================")
    access, account_no = access_account()
    if access:
        amount = int(input("Enter the amount to withdraw : "))
        if amount <= utils.transactions[account_no]['balance']:
            utils.transactions[account_no]['withdrawal_history'].append(amount)
            utils.transactions[account_no]['balance'] -= amount
            print("Amount withdrawn successfully. Your new balance is: ", utils.transactions[account_no]['balance'])
        else:
            print("Insufficient balance.")
    else:
        print("Invalid account number or pin.")