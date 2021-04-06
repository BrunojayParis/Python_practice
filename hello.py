#Libraries
from math import *

print ("hello")
print(10%3)
mynum = 5
anothernum = -5
print (str(mynum))
print (abs(anothernum))
print (ceil(3.8))
print (sqrt(36))

#inputs with python

#name = input("enter your name: ")
#age = input("enter your age: ")
#print ("hello "+ name +" you are "+ age)

#functions

def say_hi ():
    print("hello user!")

say_hi()

#if declaration

is_male = False
is_tall = True

if is_male and is_tall:
    print("it is definetly a male and tall")
else:
    print("not a male nor tall")

if is_male or is_tall:
    print("it is definetly a male or tall or both")
else:
    print("not a male nor tall")

#If statements and comparisson.

def max_num(num1,num2,num3):
    if num1 >= num2 and num1>=num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(300, 450, 2))


#Dictionaries
monthConversions ={
    "jan": "january",
    "feb": "february",
    "Mar": "March"
}
print(monthConversions["Mar"])

#while loop
i = 1
while i<= 10:
    print (i)
    i += 1

