import utils 
def access_account():
    print(" ================== Access Account =================")
    account_no = int(input("Enter you account number : "))
    pin = int(input("Enter your pin : "))
    if account_no in utils.transactions and pin == utils.transactions[account_no]['pin']:
        return True ,account_no
    else:
        return False , account_no