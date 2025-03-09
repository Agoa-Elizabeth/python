
class Fruits:
    def __init__(lisa, name, color, size, taste, price):
        lisa.name = name 
        lisa.color = color
        lisa.size = size
        lisa.size = taste
        lisa.size = price

orange = Fruits("orange", "orange", "medium", "juicy", "2000")
mango = Fruits("mango","yellow", "big", "yummy", "2500")


class Animal:
    def __init__(self, name, color, breed, weight, age):
        self.name = name
        self.breed = color
        self.breed = breed
        self.weight = weight
        self.age = age

    def dispalydetails(self):
     print(f"animalname:{self.name}\n animalbreed:{self.breed}\n animalcolor:{self.color}\n animalweight:{self.weight}\n animalage:{self.age}\n")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog = Dog("press", "grey", "germanysherpad", "32.8", "8")
dog.details()



    