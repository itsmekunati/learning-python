class Base(object):
    def __init__(self,name):
        self.name = name
        self._other = "private"
    def getName(self):
        return self.name
    def getOther(self):
        return self._other

class Child(Base):
    def __init__(self, name, age):
        Base.__init__(self,name)
        self.age = age
        self._other="local-private"
    def getAge(self):
        return self.age

chi = Child("Abhishek",39)
print("Name is : ", chi.getName())
print("Age is : ", chi.getAge())
print("Inner Other is : ", chi._other)

ba = Base("Abhishek")
print("Name is : ", ba.getName())
print("Outer Other is : ", ba._other)