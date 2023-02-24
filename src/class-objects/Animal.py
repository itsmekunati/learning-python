import logging;

logging.basicConfig(filename='example.log', level=logging.INFO)

class Animal(object):
    
    def __init__(self, name, breed, category):
         self.name = name
         self.category = category
         self.breed = breed
        
    def Show(self):
        print("Name is :" , self.name)
        print("Breed is :", self.breed)
        print("Category is :", self.category)
        
animal = Animal("Dog","BullDog","Mammal")
logging.info("Printing the Animal Details :")
animal.Show()