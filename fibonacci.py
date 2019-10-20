def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)

def dusinMachine():
    if 12 == 12:
        i = 1
        while i < 12:
            i += 1
    else:
        print('Too bad')

def nest():
    if True:
        if 'AND' == 'True':
            if True:
                True
        else:
            False

def whileForever():
    while i < 1:
        while j < 2:
            while w < 3:
                print('maybe')
