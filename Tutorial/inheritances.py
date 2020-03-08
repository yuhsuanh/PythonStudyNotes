#!/usr/bin/python3
# coding=utf-8
'''
	Python Inheritance
	Parent class: is the class being inherited from, also called base class.
	Child class: is the class that inherits from another class, also called derived class.
'''

# Create Parent Class
class Person:
	def __init__(self, fname, lname):
		self.fname = fname
		self.lname = lname

	def printname(self):
		print(self.fname, self.lname)

# Use Parent class to create an object
x = Person('Yu-Hsuan', 'Huang')
x.printname()


# Create Child Class
class Student(Person):
	def __init__(self, fname, lname, birth):
		super().__init__(fname, lname)
		self.birth = birth

	def welcome(self):
		print('Welcome', self.fname, self.lname)

	def printname(self):
		print(self.fname, self.lname, self.birth)

# Use Child class to create an object
y = Student('Winnie', 'Lai', '0331')
y.printname()
y.welcome()