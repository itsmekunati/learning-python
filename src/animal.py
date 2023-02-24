class Animal:
    name = "Cany"
    iam = "Pet"

    def printNames(self) :
        print("My Name is ", self.name)
        print("I am a", self.iam)
    

dog  = Animal()
# print ("name is ", dog.name)
dog.printNames()