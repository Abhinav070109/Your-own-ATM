import random

class Atm(object):
    def __init__(self,accountNo,pin):
        self.accountNo = input('Input your account no.')
        self.pin = input('Input your pin')
        
    def withdrawal(self):
        r = random.randint(1000,99999)
        print(r,' = current balance')
        a = input('Input Amount To Withdraw')
        print('Cash Withdrawed')
            
    def balance(self):
        r = random.randint(1000,99999)
        print(r)
        
    def deposit(self):
        r = random.randint(1000,99999)
        print(r,' = current balance')
        a = input('Input Amount To Deposit')
        print('Cash Deposited')
        
a = input('Input Account No.')
b = input('Input Pin')
atm = Atm(a,b)

c = input('What do you want to do:- Withdraw Money, Deposit Money, Check Balance. Please write all small.')

if c == 'withdraw money':
    print(atm.withdrawal())
    
if c == 'deposit money':
    print(atm.deposit())
    
if c == 'check balance':
    print(atm.balance())