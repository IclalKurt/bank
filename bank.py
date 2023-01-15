#para çekme fonksiyonu 
def cashWithdrawal (account,amount):
    remainder = (account['remaining balance']) - amount 
    print(f'current balance {remainder}') 



#para yatırma fonksiyonu
def toDepositMoney (account,amount):
    newBalance = (account['remaining balance']) + amount
    print(f'current balance {newBalance}')

iclalAccount = {
    'name' : 'iclal kurt',
    'account no' : '65764797',
    'remaining balance' : 3000
}

mustafaAccount = {
    'name' : 'mustafa emir utku',
    'account no' : '164987',
    'remaining balance' : 2000
}


print('enter your name')
name = input()

if name == 'iclal kurt':
    account = iclalAccount
    print('select the operation.\na-cash withdrawal \nb-to deposit money')
    chooseOperation = input()
   
    print('enter amount.')
    amount = int(input())

    if chooseOperation == 'a':
        cashWithdrawal(account,amount)  
    else :
        toDepositMoney (account,amount)

    


elif name == 'mustafa emir utku':
    account = mustafaAccount
    print('select the operation.\na-cash withdrawal \nb-to deposit money')
    chooseOperation = input()
   
    print('enter amount.')
    amount = int(input())

    if chooseOperation == 'a':
        cashWithdrawal(account,amount)  
    else :
        toDepositMoney (account,amount)

else :
    print('user not found')

    
    