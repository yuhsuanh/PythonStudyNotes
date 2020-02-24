#!/usr/bin/python3
# coding=utf-8

'''
	Python Classes and Objects
		Python is an object oriented programming language.
		Almost everything in Python is an object, with its properties and methods.
		A Class is like an object constructor, or a "blueprint" for creating objects.
'''

# Create a Class
class MyClass:
	x = 5

c1 = MyClass()
print(c1)
print(type(c1))
print(c1.x)


# The __init__() Function
class Person:
	def __init__(self, name, age) :
		self.name = name
		self.age = age

c1 = Person("Yu-Hsuan", 20)
print(c1.name)
print(c1.age)


# Object Methods
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def myfunc(person):
		print('Hello my name is ' + person.name)

c1 = Person("Yu-Hsuan", 20)
c1.myfunc()

# Modity Object Properties
c1.age = 50
print(c1.age)

# Delete object properties
del c1.age
# Delete object
del p1