class Pet: #general class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")



#to allow cat and dog class to use above functionality simply add(pet)
class Cat(Pet): #specific class

    def speak(self):
        print("meow")


class Dog(Pet):

    def speak(self):
        print("Bark")

p = Pet("Asia", 23)
p.show()
c = Cat("Chinobi", 34)
c.speak()
d = Dog("Bobbi", 10)
d.speak()


