#declaring a class under encapsulation
class Animal:
#a constructor is used to initialize or giving value to a 0bject
# the word self is used to identify properties in a class
#animal name is the property
    def __init__ (self, name, weight, color, owner):
        self.animalname = name
        self.animalweight = weight
        self.animalcolor = color
        self.animalowner = owner

cat = Animal("cat", "small", "black")
dog = Animal("dog", "name", "size", "color")
