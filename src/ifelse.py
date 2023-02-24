# No exception Exception raised in try block

val1 = int(input("Enter your value: "))
print(val1)
val2 = int(input("Enter your value: "))
print(val2)

def calculate(a, b) :
    """ handles zero division exception """
    try:
        k = a//b # raises divide by zero exception.
        print(k)
    # handles zerodivision exception
    except ZeroDivisionError:
        print("Can't divide by zero")

    finally:
        # this block is always executed
        # regardless of exception generation.
        print('This is always executed')

# assert Keyword
# using assert to check for 0


print ("The value of ", val1, "/", val2, "is :")
print(calculate.__doc__)
calculate(val1,  val2)
