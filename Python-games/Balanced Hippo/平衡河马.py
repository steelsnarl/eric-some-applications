while True:
    hippo = 1
    while hippo < 10:
        print(hippo,'hippo')
        a1 = input('add another hippo(y\\n)\nEnter: ')
        if a1 == 'n':
            break
        else:
            hippo += 1
    else:
        print('Crash!!!')
    
