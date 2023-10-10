import Account

class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return 'Hello {}, you have £{} in your savings accout!'.format(self.name, self.balance)
