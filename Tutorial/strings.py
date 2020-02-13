#!/usr/bin/python3
# coding=utf-8

'''
	Python String
'''

# Single quotation marks or double quotation marks
print('Hello')
print("Hello", end='\n\n')

# Use three single quotation/double quotes for multiple lines
a = """My name is
Yu-Hsuan Huang
How are you?"""
print(a, end='\n\n')

# String are Arrays
# Strings in Python are arrays of bytes representing unicode characters.
a = 'Hello Yu-Hsuan'
print(a[9])


# Slicing 
# You can return a range of characters by using the slice syntax.
a = 'Hello Yu-Hsuan'
print(a[6:9])

# Negative Indexing
# Get the characters from position 5 to position 1, starting the count from the end of the string
a = 'Hello Yu-Hsuan'
print(a[-5:-2])

# String Length
a = 'Hello Yu-Hsuan'
print(len(a), end='\n\n')

#Other String Methods
# strip() removes any whitespace from beginning or the end
a = ' Hello Yu-Hsuan   '
print(a.strip())
# lower() return the string in lower case
print(a.lower())
# upper() return the string in upper case
print(a.upper())
# replace() replace a string with another string
print(a.replace(' ', '|'))
# split() splits the into substrings if it finds instances of the separator
print(a.split(' '), end='\n\n')


# Check String
# use 'in' or 'not in' to check if a certain phrase or character is present in a string
a = 'Hello Yu-Hsuan'
x = 'uan' in a
y = 'uan' not in a
print(x)
print(y, end='\n\n')

# String Concatennation
# Use the + operator
a = 'Hello'
b = 'Yu-Hsuan'
c = a + b
print(c)

# we cannot combine string s and numbers like this
# age = 20
# a = "I am " + age + " years old"
# print(a)

# But we can combine strings and numbers by using the format() method!
age = 20
a = 'I am {} years old'
print(a.format(age))

# Multiple arguments
fname = 'Yu-Hsuan'
lname = 'Huang'
age = 20
a = 'My name is {} {}. I am {} years old'
print(a.format(fname, lname, age))

# Or you can assign the index number for each {}
fname = 'Yu-Hsuan'
lname = 'Huang'
age = 20
a = 'My name is {1} {2}. I am {0} years old'
print(a.format(age, fname, lname), end='\n\n')


# Escape Character
'''
	\'		Single Quote	
	\\		Backslash	
	\n		New Line	
	\r		Carriage Return	
	\t		Tab	
	\b		Backspace	
	\f		Form Feed	
	___		Octal value	
	___		Hex value
'''
# Octal value
txt = '\110\145\154\154\157'
print(txt)
# Hex value
txt = '\x48\x65\x6c\x6c\x6f'
print(txt)


'''
	Method	Description
	capitalize()	Converts the first character to upper case
	casefold()	Converts string into lower case
	center()	Returns a centered string
	count()	Returns the number of times a specified value occurs in a string
	encode()	Returns an encoded version of the string
	endswith()	Returns true if the string ends with the specified value
	expandtabs()	Sets the tab size of the string
	find()	Searches the string for a specified value and returns the position of where it was found
	format()	Formats specified values in a string
	format_map()	Formats specified values in a string
	index()	Searches the string for a specified value and returns the position of where it was found
	isalnum()	Returns True if all characters in the string are alphanumeric
	isalpha()	Returns True if all characters in the string are in the alphabet
	isdecimal()	Returns True if all characters in the string are decimals
	isdigit()	Returns True if all characters in the string are digits
	isidentifier()	Returns True if the string is an identifier
	islower()	Returns True if all characters in the string are lower case
	isnumeric()	Returns True if all characters in the string are numeric
	isprintable()	Returns True if all characters in the string are printable
	isspace()	Returns True if all characters in the string are whitespaces
	istitle()	Returns True if the string follows the rules of a title
	isupper()	Returns True if all characters in the string are upper case
	join()	Joins the elements of an iterable to the end of the string
	ljust()	Returns a left justified version of the string
	lower()	Converts a string into lower case
	lstrip()	Returns a left trim version of the string
	maketrans()	Returns a translation table to be used in translations
	partition()	Returns a tuple where the string is parted into three parts
	replace()	Returns a string where a specified value is replaced with a specified value
	rfind()	Searches the string for a specified value and returns the last position of where it was found
	rindex()	Searches the string for a specified value and returns the last position of where it was found
	rjust()	Returns a right justified version of the string
	rpartition()	Returns a tuple where the string is parted into three parts
	rsplit()	Splits the string at the specified separator, and returns a list
	rstrip()	Returns a right trim version of the string
	split()	Splits the string at the specified separator, and returns a list
	splitlines()	Splits the string at line breaks and returns a list
	startswith()	Returns true if the string starts with the specified value
	strip()	Returns a trimmed version of the string
	swapcase()	Swaps cases, lower case becomes upper case and vice versa
	title()	Converts the first character of each word to upper case
	translate()	Returns a translated string
	upper()	Converts a string into upper case
	zfill()	Fills the string with a specified number of 0 values at the beginning
'''