#the statements we make in method are called behaviours things u do within the method
#a function within a class is called a method
class Animal():
    name = ""
    color = ""
    weight = ""
    owner = ""

    def sound(self):
        print("i bark")

dog= Animal()
dog.sound()

