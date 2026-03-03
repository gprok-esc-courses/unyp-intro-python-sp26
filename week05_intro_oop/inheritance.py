
class Animal:
    def __init__(self, name):
        self.name = name 
        self.sound = '...'
        self.type = "Animal"

    def __str__(self):
        return f"{self.type} {self.name} says {self.sound}"
    

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Dog"
        self.sound = "Woooof"

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.type = "Cat"
        self.sound = "Mieow"
    



# a = Animal("Bob")
# print(a)

# d = Dog("Pluto")
# print(d)

# c = Cat("Sylvester")
# print(c)

animals = [] 
animals.append(Animal("Bob"))
animals.append(Dog("Pluto"))
animals.append(Cat("Sylvester"))

for a in animals:
    print(a)