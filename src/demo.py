import globals

print("Hello", globals.arr)
a = 1
print("a value is " + str(a) )


def calc():
    for i in range(10):
        if i == 6 :
            continue
        print(i , end = " ")

    print()

    w = 0
    while w <= 10 :
        print(w, end =" ")
        w = w+1

calc()

