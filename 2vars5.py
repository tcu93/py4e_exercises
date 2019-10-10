"""
Exercise 5   Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit and print out the converted temperature.
"""

#!/usr/bin/env python
Celsius = int(input("Enter a temperature in Celsius: "))

Fahrenheit = 9.0/5.0 * Celsius + 32

print("Celcius is: ", Celsius, "and Farenheit is : ", Fahrenheit)
print('Celsius is {} and F is {}'.format(Celsius, Fahrenheit))
# WHICH IS BETTER?
