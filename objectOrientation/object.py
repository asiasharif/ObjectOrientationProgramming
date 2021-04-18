#object orientation work

# def hello():
#     print("hello")
#
# x = 1
# print(type(hello))

class Dog(object):
    pass


class Dog:
    def __init__(self, name, age):
        self.name = name #created an attribute of the class dog which is name - attriube is inside the dog class
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age



# dogs_name = ["Tim", "Bill"] #this way is a pain especially if we had other attributes associated to the dog that we wants to access
# dogs_age = [24, 34]

# d = Dog("Tim", 24)  #it passed this to the name parameter
# d.set_age(23)
# print(d.get_age())



    # def add_one(self, x):
    #     return x + 1
    #
    # def bark(self): #method goes inside of a class
    #     print("bark")

#assign variable to a class dog


# d2 = Dog("Bill", 23)
# print(d2.get_age())
# d.bark()
# print(d.add_one(5))
# print(type(d))