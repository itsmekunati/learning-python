# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
	return text.upper()

def create_adder(x, y):
    return x + y

def whisper(text):
	return text.lower()

def calc(func):
    num = func(15, 10)
    return num
    
def greet(func):
	# storing the function in a variable
	greeting = func("""Hi, I am created by a function
					passed as an argument.""")
	print(greeting)

greet(shout)
greet(whisper)
print(calc(create_adder))
