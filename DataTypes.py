number = 67 #integer
second = 45.98 #Float
text = "Hello World" #String
value = "True" #Boolean
letter = "b" #Character
print(number)
print(second)
print(text)
print(value)
print(letter)


#Data Structures - Multiple values stored in one variable
#Lists
cars = ["Toyota","Mercedes","BMW"] #Ordered and Changeable
print(cars)
#Tuples
fruits = ("Apple","Watermelon","Peaches") #Ordered buh Unchangeable
print(fruits)
#Sets
countries = {"USA","Spain","Australia"} #Unordered and Unchangeable
print(countries)
#Dictionaries: Key-Value Pairs
student = {
    "firstname" : "Mel",
    "age" : 20,
    "course" : "Software Development",
    "gender" : "Male"
}
print(student)
print(student["firstname"])

#Determining a datatype
print(type(countries))
print(type(fruits))
print(type(student))

#Typecasting - Conversion from one datatype to another
print(float(number))
print(int(second))
