#Variables
a = 10
b = 20
c = a + b
print(c)

#Type casting
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

#Type of variables

x = 5
y = "John"
print(type(x))
print(type(y))


# # Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType

# Numeric Types:	int, float, complex
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# # Text Type:	str
x = "Hello World"
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) #multiline string

#String slicing
x = "Hello World"
print(x[2:5])

#Modify strings
a = "Hello, World!"
print(a.upper())    #HELLO, WORLD!
print(a.lower())    #hello, world!  
print(a.strip())    #Hello, World!
print(a.replace("H", "J"))  #Jello, World!
print(a.split(","))  #['Hello', ' World!']

#Format strings
x = 5
y = 10
print("The value of x is {} and y is {}".format(x, y))

#Boolean Type:	bool
print(10 > 9)   #True
print(10 == 9)  #False
print(10 < 9)   #False

#List
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "blackcurrant"
print(thislist)
for x in thislist:
  print(x)

#Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
for x in thistuple:
  print(x)

#Set
thisset = {"apple", "banana", "cherry"}
print(thisset)
for x in thisset:
  print(x)

#Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
for x in thisdict:
  print(x)
for x in thisdict.values():
  print(x)
for x, y in thisdict.items():
  print(x, y)

#Python operator
# Python divides the operators in the following groups:

# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators
# Python Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# Operator	Name	
# +	Addition	x + y	
# -	Subtraction	x - y	
# *	Multiplication	x * y	
# /	Division	x / y	
# %	Modulus	x % y	
# **	Exponentiation	x ** y	
# //	Floor division	x // y	
# Python Assignment Operators
# Assignment operators are used to assign values to variables:

# Operator
# =	x = 5	x = 5	
# +=	x += 3	x = x + 3	
# -=	x -= 3	x = x - 3	
# *=	x *= 3	x = x * 3	
# /=	x /= 3	x = x / 3	
# %=	x %= 3	x = x % 3	
# //=	x //= 3	x = x // 3	
# **=	x **= 3	x = x ** 3	
# &=	x &= 3	x = x & 3	
# |=	x |= 3	x = x | 3	
# ^=	x ^= 3	x = x ^ 3	
# >>=	x >>= 3	x = x >> 3	
# <<=	x <<= 3	x = x << 3	
# :=	print(x := 3)	x = 3
# print(x)	
# Python Comparison Operators
# Comparison operators are used to compare two values:

# Operator	
# ==	Equal	x == y	
# !=	Not equal	x != y	
# >	Greater than	x > y	
# <	Less than	x < y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to	x <= y	
# Python Logical Operators
# Logical operators are used to combine conditional statements:

# Operator
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	
# Python Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

# Operator 
# is 	Returns True if both variables are the same object	x is y	
# is not	Returns True if both variables are not the same object	x is not y	
# Python Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# Operator	
# in 	Returns True if a sequence with the specified value is present in the object	x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y	
# Python Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:

# Operator 
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2	
# Operator Precedence
# Operator precedence describes the order in which operations are performed.

# Example
# Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

# print((6 + 3) - (6 + 3))
# Example
# Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions:

# print(100 + 5 * 3)
# The precedence order is described in the table below, starting with the highest precedence at the top:

# Operator
# ()	Parentheses	
# **	Exponentiation	
# +x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
# *  /  //  %	Multiplication, division, floor division, and modulus	
# +  -	Addition and subtraction	
# <<  >>	Bitwise left and right shifts	
# &	Bitwise AND	
# ^	Bitwise XOR	
# |	Bitwise OR	
# ==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
# not	Logical NOT	
# and	AND	
# or	OR

