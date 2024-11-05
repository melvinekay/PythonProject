#!/usr/bin/python3
#Area of a rectangle
length = int(input("Enter a length: "))
width = int(input("Enter a width: "))
area = length * width
print("The area of the square is", area, "square centimeters.")

#Area of a triangle
base = int(input("Enter a base: "))
height = int(input("Enter a height: "))
area = 0.5 * base * height
print("The area of the triangle is", area, "square centimeters.")

#Area of a circle
radius = int(input("Enter a radius: "))
area = radius * radius
print("The area of the circle is", area, "square centimeters.")

#Circumference
diameter = int(input("Enter a diameter: "))
pi = 3.14159
circumference = pi * diameter
print("The circumference of the circle is", circumference, "centimeters.")