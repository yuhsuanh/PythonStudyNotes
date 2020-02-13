#!/usy/bin/python3
# coding=utf-8

'''
	Python Operators
	Operators are used to perform operations on variables and values.

	Arithmetic operators
	Assignment operators
	Comparison operators
	Logical operators
	Identity operators
	Membership operators
	Bitwise operators
'''

'''
	Arithmetic Operators
	+	Addition
	-	Subtraction
	*	Multiplication
	/	Division
	%	Modulus
	**	Exponentiation
	//	Floor division
'''
x = 2 ** 4
y = 256 / 3
z = 256 // 3
print(x, 'Exponentiation')
print(y, 'Division')
print(z, 'Floor division', end='\n\n')

'''
	Assignment Operators
	=	Equal to
	+= 	example: a += 1 is equal to a = a + 1
	-=	
	*=
	/=
	%=
	//=
	**=
	&=
	|=
	^=
	>>=
	<<=
'''
# Decimal '4' is binary '100'
x = 4
# Left shift is  binary '1' is decimal '1'
x >>= 2
print(x)

# Decimal '4' is binary '100'
x = 4
# Right shift is  binary '10000' is decimal '16'
x <<= 2
print(x, end='\n\n')

'''
	Comparison Operators
	==	Equal
	!=	Not equal
	>	Greater than
	<	Less than
	>=	Greater than or equal to
	<=	Less than or equal to
'''

'''
	Logical Operators
	and 
	or 	
	not 
'''
x = 3
print(x<5 and x>10)
print(x<5 or x>10)
print(not(x<5 and x>10), end='\n\n')

'''
	Identity Operators
	is		Returns true if both variables are the same object 
	is not 	Returns true if both variables are not the same object
'''
x = 'Hsuan'
y = 'Huang'
print(x is y)
print(x is not y)

'''
	Membership Operators
	in 		Returns True if a sequence with the specified value is present in the object
	not in 	Returns True if a sequence with the specified value is not present in the object
'''
x = 'Hsuan'
y = 'su'
print(y in x)
print(y not in x)

'''
	Bitwise Operators
	& 	AND
	|	OR
	 ^	XOR
	~ 	NOT
	<<	Zero fill left shift
	>>	Signed right shift