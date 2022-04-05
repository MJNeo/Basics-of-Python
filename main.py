#Python Syntax
print("Hello, World!")

#Python Indentation
if 5>3:
    print("Five is greater than the number")
else:
    print("Five is less than the number")

#Python Variables
x=5
y = "Hello, World!"

#Creating a comment
#Single line comment
print("Hello, this is Leo") #This is also a comment
#Multi line comments
#This is a comment
#Written in
#more than one line

"""
This is a comment
written in
more than one line
"""

#Creating variables
x=5
y = "John"
print(x)
print(y)

#Example:1
x=4 #x is of type int
x = "Sally" #x is now of type str
print(x)

#Casting
x=str(3)
y=int(3)
z=float(3)
print(x)
print(y)
print(z)

#Get the type
x=5
y="John"
print(type(x))
print(type(y))

#Single & double quotes
x="John"
y='John'
print(x)
print(y)

#Case sensitive
a=4
A="Sally"
print(a)
print(A)

#Variable Names
myvar="John"
my_var="John"
_my_var="John"
myVar="John"
MYVAR="John"
myvar2="John"
print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)

#Illegal variable Names
#2myvar="John"
#my-var="John"
#my var="John"

#Camel case
myVariableName="John"

#Pascal case
MyVariableName="John"

#Snake case
my_variable_name="John"

#Python Variables - assign multiple values
x, y, z = "orange", "Banana", "apple"
print(x)
print(y)
print(z)

#One value to multiple variables
x=y=z="orange"
print(x)
print(y)
print(z)

#Unpack a collection
#Unpack a list
fruits = ["apple", "banana", "mango"]
x,y,z=fruits
print(x)
print(y)
print(z)

#Python output variables
x="python is easy"
print(x)

x= "python"
y= "is"
z= "easy"
print(x)
print(y)
print(z)

x= "python "
y= "is "
z= "easy"
print(x + y + z)

x=5
y=10
print(x+y)

x=5
y= "John"
#print(x+y)

x=5
y="John"
print(x, y)

#Python Global variables
x = "simple"
def myfunc():
    print("Python is " + x)
myfunc()

x = "jesse"
def myfun():
    print("My name is " + x)
myfun()

x = "simple"
def myfunc():
  x = "easy to learn"
  print("Python is " + x)
myfunc()
print("Python is " + x)

def myfunc():
    global x
    x = "very easy programming language"
myfunc()
print("python is " + x)
