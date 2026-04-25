import utils
def statement():
    print(" ================== Mini Statement =================")

    print("Recent transactions:")
    access, account_no = utils.access_account()
    if access:
        print("Current balance: ", utils.transactions[account_no]['balance'])
        for amount in utils.transactions[account_no]['deposited_history'][::-1]:
            print("Deposited: ", amount)
        for amount in utils.transactions[account_no]['withdrawal_history'][::-1]:
            print("Withdrawn: ", amount)
    else:
        print("Invalid account number or pin.")