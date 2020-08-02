#!/usr/bin/python3
#Created by Caleb Akinosho
from math import *
#Converts Fahrenheit into Celsius and vice versa
print("F is for Fahrenheit")
print("C is for Celsius")
temp = input("Choose your unit of temperature Celsius(C) or Fahrenheit(F):  ")

if temp == 'F':
    fahrenheit = float(input("What is the temperature in Fahrenheit: "))
    print(float((fahrenheit-32)/1.8))
elif temp == 'C':
    celsius = float(input("What is the temperature in Celsius: "))
    print(float((celsius*1.8)+32))
else:
    print("Invalid Input")
print("Goodbye!")