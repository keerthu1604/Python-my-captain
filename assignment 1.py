# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 22:46:17 2021

@author: keekee
"""

mylist=["one","two","three"]
print(mylist)
print(mylist[0])
mylist[2]="five"
print(mylist)
mylist.remove("five")
print(mylist)

mytuple=("apple","bat","cat")
print(mytuple)
print(mytuple[2])
mytuple=("apple","bat","cat")
mytuple1=list(mytuple)
mytuple1[1]="dog"
mytuple=tuple(mytuple1)
print(mytuple)

myset={"one","two","three"}
print(myset)
print("two" in myset)
myset.add("four")
print(myset)
myset.remove("two")
print(myset)

mydict={
        "one":"oneplus",
        "two":"iphone",
        "three":"vivo"
        }
print(mydict)
mydict["two"]
mydict["four"]="realme"
del mydict["two"]
print(mydict)

a = "Hello World"
print(len(a))
print(a[0])


 #Function to add two numbers 
def add(num1, num2):
    return num1 + num2
  
# Function to subtract two numbers 
def subtract(num1, num2):
    return num1 - num2
  
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
  
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
  
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
  
  
# Take input from the user 
select = int(input("Select operations form 1, 2, 3, 4 :"))
  
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
  
if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))
  
elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))
  
elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))
  
elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")