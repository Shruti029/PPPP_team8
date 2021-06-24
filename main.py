# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 20:36:53 2021

@author: chawane
"""

from addition import addition
from multiplication import multiplication
from subtraction import subtraction
from division import division


def startApp():
    return "Welcome to Matrix calculator!"


startApp()

row1 = int(input("Enter number of numbers in arrays:"))


array1 = []
array2 = []

for i in range(row1):
    array1.append(int(input("Enter element of Array 1:")))

for i in range(row1):
    array2.append(int(input("Enter element of Array 2:")))


operation = str(input("Choose operation (+, -, *, /):"))

if operation == "+":
    print("Answer:", addition(array1, array2))


if operation == "-":
    print("Answer:", subtraction(array1, array2))


if operation == "*":
    print("Answer:", multiplication(array1, array2))
    

if operation == "/":
    print("Answer:", division(array1, array2))


def endApp():
    return "Thank you for using Matrix calculator!"


endApp()
