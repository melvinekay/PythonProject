class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def study(self):
        print("Student is studying")

#Creating an object
student1 = Person("Mel",20, "Male")
print(student1.name, student1.age, student1.gender)
student2 = Person("Cardia", 19, "Female")
print(student2.name, student2.age, student2.gender)
student3 = Person("Danyl", 21, "Male")
print(student3.name, student3.age, student3.gender)
