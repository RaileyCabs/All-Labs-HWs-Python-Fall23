#HW1.py
# Author: James Railey Cabrera

# Question 1:
# Print Hello World like we did in class

# Question 2:
# Print the following:
# Your name

# Your age

# Your favorite color

# Your favorite animal

# Question 3:
# Create a variable called "myName" and set it equal to your name

# Create a variable called "myAge" and set it equal to your age

# Create a variable called "myColor" and set it equal to your favorite color

# Create a variable called "myAnimal" and set it equal to your favorite animal

# Print the following:
# Hello, my name is <myName>
# I am <myAge> years old
# My favorite color is <myColor>
# My favorite animal is <myAnimal>


# Question 4:
# Calculate the following and print the result:
# 2 + 2

# 3 * 4

# 5 - 6

# 8 / 2

# Question 5:
# Create a variable called "num1" and set it equal to 2

# Create a variable called "num2" and set it equal to 3

# Create a variable called "num3" and set it equal to 4

# Create a variable called "num4" and set it equal to 5

# Calculate the following and print the result:
# num1 + num2

# num3 * num4

# num4 - num1

# num2 / num1

# Question 6: Write a program that asks the user for their name and then prints the following:

# Hello, <name>. Please enter three numbers.

# The program should then ask the user for three numbers (floats) and print the following:


# 1. The sum of the three numbers is <sum>

# 2. The product of the three numbers is <product>

# 3. round the three numbers to the nearest integer and print the sum of the three rounded numbers divided by 3 

# 4. The average of the three numbers is <average>

# Question 7: Ask the user for an input of a symbol (in the example its *)     
# Print a diamond of the symbol that looks like the following. Include the spaces and the | character. 
# Hint: the print("symbol", end="") with \t and \n characters will be useful here.

#    *     |
#   ***    |
#  *****   |
# *******  |
#  *****   |
#   ***    |
#    *     |


print("Hello World")
print("Railey Cabrera")
print('18')
print("blue")
print("dog")
myName = "Railey Cabrera"
myAge = '18'
myColor = "blue"
myAnimal = "dog"
print("Hello, my name is " + myName + " I am " + myAge + " years old. My favorite color is " + myColor + " and my favorite animal is " + myAnimal + ". ")

add = 2 + 2
print(add)
multiply = 3 * 4
print(multiply)
subtract = 5 - 6
print(subtract)
divide = 8 / 2
print(divide)

num1 = 2
num2 = 3
num3 = 4
num4 = 5

num1 + num2
print(num1 + num2)
num3 * num4
print(num3 * num4)  
num4 - num1
print(num4 - num1)
num2 / num1 
print(num2 / num1)

name = input("What is your name? ")
print("Hello, " + name + ". Please enter three numbers.")

nom1 = float(input("Enter first number: "))
nom2 = float(input("Enter second number: "))
nom3 = float(input("Enter third number: "))

print("The sum of the three numbers is " + str(nom1 + nom2 + nom3))
print("The product of the three numbers is " + str(nom1* nom2 *nom3))
print("The average of the three numbers is " + str((nom1 + nom2 + nom3) / 3))
round(nom1)
round(nom2)
round(nom3) 
print("The sum of the three rounded numbers divided by 3 is " + str((nom1 + nom2 + nom3) / 3))
print("The average of the three numbers is " + str((nom1 + nom2 + nom3) /3))

symbol = input("Enter a symbol: ")
print(" " + " " + " " + symbol + "    |")
print(" " + " " + symbol * 3 + "   |")
print(" " + symbol * 5 + "  |")
print(symbol * 7 + " |")
print(" " + symbol * 5 + "  |")
print(" " + " " + symbol * 3 + "   |")
print(" " + " " + " " + symbol + "    |")