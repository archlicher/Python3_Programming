import Account
import Current
import Savings

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