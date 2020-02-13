#!/usr/bin/python3
# coding=utf-8

'''
	Python Dictionary
	A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
'''

thisdict = {
	'brand': 'Subaru',
	'model': 'XV Crosstrek',
	'year': 2013
}
print(thisdict)
print(type(thisdict))
print(len(thisdict))

# Access Item
x = thisdict['brand']
print(x)
x = thisdict.get('brand')
print(x)

# Change value
thisdict['year'] = 2019
print(thisdict)

# Add item
thisdict['color'] = 'black'
print(thisdict)

# Remove items
# The pop() method removes the item with the specified key name
thisdict.pop('model')
print(thisdict)
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
thisdict.popitem()
print(thisdict)
# del to delete the item
del thisdict['year']
print(thisdict)
# Celar the dictionary
thisdict.clear()
print(thisdict, end='\n\n')

# Loop through a Dictionary
thisdict = {
	'brand': 'Subaru',
	'model': 'XV Crosstrek',
	'year': 2013
}
for x in thisdict:
	print(x, thisdict[x])
# Get Values
for x in thisdict.values():
	print(x)
# Get Items
for x, y in thisdict.items():
	print(x, y)


# Check if this item exists in the dictionary
if 'model' in thisdict:
	print('model is one of the key in the thisdict dictionary', end='\n\n')

# Nested Dictionaries
myfamily = {
	"child1" : {
		"name" : "Emil",
    	"year" : 2004
  	},
  	"child2" : {
    	"name" : "Tobias",
    	"year" : 2007
	},
	"child3" : {
		"name" : "Linus",
		"year" : 2011
	}
}
print(myfamily)


# The dict() Constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)