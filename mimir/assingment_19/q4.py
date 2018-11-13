class Account:
    def __init__(self,amount):
        self.amount = amount
    def __str__(self):
        return "Balance: {:.2f}".format(self.amount)
class DebitAccount(Account):
    rate = (0.02)
    def update_balance(self):
        self.amount = self.amount * (1 + DebitAccount.rate)
class SavingsAccount(Account):
    rate_bonus = (0.1)
    rate = (0.05)
    def update_balance(self):
        self.amount =  self.amount * (1 + SavingsAccount.rate + SavingsAccount.rate_bonus)
def print_accounts(Accounts):
    for x in Accounts:
        print(x)
def update_accounts(Accounts):
    new_account = []
    for account in Accounts:
        new_account.append(account.update_balance())