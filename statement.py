import utils
def statement():
    print(" ================== Mini Statement =================")

    print("Recent transactions:")
    account_no = int(input("Enter your account number : "))
    pin = int(input("Enter your pin : "))
    if account_no in utils.transactions and pin == utils.transactions[account_no]['pin']:
        print("Current balance: ", utils.transactions[account_no]['balance'])
        for amount in utils.transactions[account_no]['deposited_history'][::-1]:
            print("Deposited: ", amount)
        for amount in utils.transactions[account_no]['withdrawal_history'][::-1]:
            print("Withdrawn: ", amount)
    else:
        print("Invalid account number or pin.")