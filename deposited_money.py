import utils
def deposited_money():
    print(" ================== Deposit Money =================")

    account_no = int(input("Enter your account number : "))
    pin = int(input("Enter your pin : "))
    if account_no in utils.transactions and pin == utils.transactions[account_no]['pin']:
        amount = int(input("Enter the amount to deposit : "))
        utils.transactions[account_no]['deposited_history'].append(amount)
        utils.transactions[account_no]['balance'] += amount
        print("Amount deposited successfully. Your new balance is: ", utils.transactions[account_no]['balance'])
    else:
        print("Invalid account number or pin.")