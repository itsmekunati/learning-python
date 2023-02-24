with open("info.txt", 'r') as file :
    data = file.read()
    print(len(data))
    file.close()
    
L = [ "Variables. \n", "Objects. \n" ]
with open("info.txt", 'a') as app:
    app.writelines(L)
    
"""

with open(r"/Users/Abhishek.Kunati/Documents/GitHub/learning-python/example.log", 'r') as f:
    print(f.read())
"""