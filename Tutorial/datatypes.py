#!/usr/bin/python3
# coding=utf-8

'''
	Python Data Types
	Text: str
	Numeric: int float, complex
	Sequence: list, tuple, range
	Mapping: dict
	Set: set, frozenset
	Boolean: bool
	Binary: bytes, btyearray, memoryview
'''


# Get Data Type
# You can get the data type of any object by using the type() function
x = 5
print(x, type(x), end='\n\n') # <class 'int'>


# Setting Data Type Sample
x = "Hello World"
x = str("Hello World") # Specific Data Type
print(x)

x = 20
x = int(20) # Specific Data Type
print(x)

x = 20.5
x = float(20.5) # Specific Data Type
print(x)

x = 1j
x = complex(1j) # Specific Data Type
print(x)

x = ["apple", "banana", "cherry"]
x = list(("apple", "banana", "cherry")) # Specific Data Type
print(x)

x = ("apple", "banana", "cherry")
x = tuple(("apple", "banana", "cherry")) # Specific Data Type
print(x)

x = range(6)
x = range(6) # Specific Data Type
print(x)

x = {"name" : "John", "age" : 36}
x = dict(name="John", age=36) # Specific Data Type
print(x)

x = {"apple", "banana", "cherry"}
x = set(("apple", "banana", "cherry")) # Specific Data Type
print(x)

x = frozenset({"apple", "banana", "cherry"})
x = frozenset(("apple", "banana", "cherry")) # Specific Data Type
print(x)

x = True
x = bool(5) # Specific Data Type
print(x)

x = b"Hello"
x = bytes(5) # Specific Data Type
print(x)

x = bytearray(5)
x = bytearray(5) # Specific Data Type
print(x)

x = memoryview(bytes(5))
x = memoryview(bytes(5)) # Specific Data Type
print(x)
