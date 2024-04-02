while True:
    def calculate(a,b,add,subtract,times,divide):
        if add:
            def add(a,b):
                print(int(a) + int(b))
            add(a,b)
        if subtract:
            def subtract(a,b):
                print(int(a) - int(b))
            subtract(a,b)
        if times:
            def times(a,b):
                print(int(a) + int(b))
            times(a,b)
        if divide:
            def divide(a,b):
                print(int(int(a) / int(b)))
            divide(a,b)
    first = input('Enter the first number\nEnter: ')
    Next = input('Enter the next number\nEnter: ')
    what = int(input('What do you want to do with those numbers(add is 1,subtract is 2,times is 3,divide is 4)\nEnter: '))
    if what == 1:
        calculate(first,Next,True,False,False,False)
    elif what == 2:
        calculate(first,Next,False,True,False,False)
    elif what == 3:
        calculate(first,Next,False,False,True,False)
    elif what == 4:
        calculate(first,Next,False,False,False,True)

    
