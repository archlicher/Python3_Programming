class Account:

    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print('You have reached your min balance')

    def statement(self):
        print('Account balance: £{}'.format(self.balance))


class Current(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return 'Hello {}, you have £{} in your bank accout!'.format(self.name, self.balance)


class Savings(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return 'Hello {}, you have £{} in your savings accout!'.format(self.name, self.balance)


x = Current('Chris', 500)
print(x.statement())
x.deposit(300)
print(x.statement())
x.withdraw(400)
print(x.statement())
x.withdraw(1700)
print(x.statement())
print(x)

s = Savings('Chris', 1500)
print(s)
s.withdraw(1500)
print(s.statement())
s.withdraw(1)
