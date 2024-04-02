import time
from random import randint
code = randint(1000,9999)
print('Your passcode to your credit card is ',code)
print('Welcome to starbucks.')
print('''Menu
Name           price
cappuccino      10
Ice American    5
caramel latte   7
Frappuccino     15
Hot chocolate   8
''')
for i in range(1,2):
    def make_coffee(coffee):
        print('Making',coffee)
        time.sleep(1)
        print('Your',coffee,'is done')
        print('Enjoy')
    coffee = str(input('What would you like.\nEnter: '))
    if coffee == 'cappuccino':
        print('That would be 10 dollers.')
        enter = int(input('Please enter your passcode\nEnter: '))
        if enter == code:
            make_coffee('cappuccino')
        else:
            print('Sorry the code you entered is not right.')
    elif coffee == 'Ice American':
        print('That would be 5 dollers.')
        enter = int(input('Please enter your passcode\nEnter: '))
        if enter == code:
            make_coffee('Ice American')
        else:
            print('Sorry the code you entered is not right.')
    elif coffee == 'caramel latte':
        print('That would be 7 dollers.')
        enter = int(input('Please enter your passcode\nEnter: '))
        if enter == code:
            make_coffee('caramel latte')
        else:
            print('Sorry the code you entered is not right.')
    elif coffee == 'Frappuccino':
            print('That would be 15 dollers.')
            enter = int(input('Please enter your passcode\nEnter: '))
            if enter == code:
                make_coffee('Frappuccino')
            else:
                print('Sorry the code you entered is not right.')
    elif coffee == 'Hot chocolate':
        print('That would be 8 dollers.')
        enter = int(input('Please enter your passcode\nEnter: '))
        if enter == code:
            make_coffee('Hot chocolate')
        else:
            print('Sorry the code you entered is not right.')
    else:
        print('Sorry that is not a choice.')
        quit()
