import utils
def withdraw_money():
    print(" ================== Withdraw Money =================")
    account_no = int(input("Enter you account number : "))
    pin = int(input("Enter your pin : "))
    if account_no in utils.transactions and pin == utils.transactions[account_no]['pin']:
        amount = int(input("Enter the amount to withdraw : "))
        if amount <= utils.transactions[account_no]['balance']:
            utils.transactions[account_no]['withdrawal_history'].append(amount)
            utils.transactions[account_no]['balance'] -= amount
            print("Amount withdrawn successfully. Your new balance is: ", utils.transactions[account_no]['balance'])
        else:
            print("Insufficient balance.")
    else:
        print("Invalid account number or pin.")