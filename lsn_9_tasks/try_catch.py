# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def func():
    raise IndexError


def func1():
    try:
        func()
    except:
        print('Index error happened')


def a_b(a, b):
    try:
        a,b = int(a), int(b)
        return (a * a) / b
    except :
        return 'Wrong format dude'

print(a_b(input(), input()))