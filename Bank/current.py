import Account

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return 'Hello {}, you have £{} in your bank accout!'.format(self.name, self.balance)
