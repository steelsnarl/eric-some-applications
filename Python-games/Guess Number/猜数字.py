import random
print('Guess the number')
while True:
    num = random.randint(1,1000)
    guess = int(input('Enter a number 1 to 1000\nEnter: '))
    if (guess in range(1,1001)):
        if (guess == num):
            print('You guessed it right!!!')
            break
        elif (guess < num):
            print('You guessed it too small')
        elif (guess > num):
            print('You guessed it too big')
    else:
        print('Out of range\nTry again')
            
