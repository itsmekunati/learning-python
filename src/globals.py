arr = [10, 20, 30]


def fun():
	global arr
	arr = [20, 30, 40]
	for i in range(len(arr)):
		arr[i] += 10
	print("'arr' inside method before executing fun():", arr)

def add():
	global x
	x = 15
	def change():
		global x
		x = 20
	print("Before making changing: ", x)
	print("Making change")
	change()
	print("After making change: ", x)

print("'arr' list before executing fun():", arr)
fun()
print("'arr' list after executing fun():", arr)
add()
print("value of x is :", x)
