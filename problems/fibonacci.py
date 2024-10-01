import sys


def fibonacci(a, b, num):
    if (b > num):
        return
    else:
        print(a)
        fibonacci(b, a + b, num)

def fibonacci_generator(num):
    a, b = 0, 1
    while a <= num:
        yield a
        a, b = b, a + b


def fibonacci_sequence(num):
    a = 0
    b = 1
    while b <= num:
        print(b)
        a, b = b, a + b

