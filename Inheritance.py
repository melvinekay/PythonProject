class Animal:
    def move(self):
        print("Animal is walking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

a = Animal()
b = Dog()
b.move()
b.bark()