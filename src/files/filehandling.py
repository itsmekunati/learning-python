file = open("info.txt", 'r')
print(file.read())
file.close()

file = open("info.txt", 'a')
file.write("\n")
file.write("this is the information about Python. \n")
file.write("its a easy to learn language campare to Java. \n")
file.close()
"""
for line in file :
   print(line)  

"""