import logging

logging.basicConfig(filename='example.log',level=logging.INFO)

def hello_calc(func):
    def logger(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return return_value
    return logger

def both_calc(func):
    def both():
        return a * b
    return both

@both_calc
def multi():
    print("Inside Function - Multiplication")

@hello_calc
def add(a, b):
    print("Inside Function - Addition")
    return a + b

def sub(a, b):
    print('Inside Function - Substraction')
    return a - b

a, b = 1, 2
print("Addition = ",add(a, b))
print("Substraction = ",sub(a, b))
print("Multiplication = ",multi())




