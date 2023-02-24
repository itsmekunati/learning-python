try:
    a = 2
    b = a / 0
    print("b is :", b)
    if ( b > 2):
        raise ValueError("B is greater than 2")
except ZeroDivisionError:
    print(" Not able to devide by Zero")
except ValueError as e:
    print(e)
else:
    print("No Error")
finally:
    print("Completed")