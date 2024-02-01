# HW2.py
# Author: james railey cabrera


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:
age = int(input("What is your age?" " "))

if age < 13:
    print("You are a child.")
elif age in range(13,20):
        print("You are a teenager")
elif age >= 20:
     print("You are an adult")

    # If the age is less than 13, print "You are a child."
    # If the age is between 13 and 19, print "You are a teenager."
    # If the age is 20 or older, print "You are an adult."


#     # Question 2:
#     # Write some code to display the following pattern using a for or while loop:
#     # 1
#     # 12
#     # 123
#     # 1234
#     # 12345

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print("") 
    

    # Question 3:
    # Write a Python program that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

    # The highest number.
    # The lowest number.
    # The average of all the numbers.

for i in range (1,11):
    num = int(input("Enter a number: "))
    if i == 1:
        highest = num
        lowest = num
        total = num
    else:
        if num > highest:
            highest = num
        if num < lowest:
            lowest = num
        total += num
print("Highest number:", highest)
print("Lowest number:", lowest)
print("Average:", total/10)


    # Question 4:
    # Vowel Counter - Write some code that prompts the user to enter a string. 
    # The program should then display the number of vowels in the string. IE. If the user enters #"Hello World",
    #  the program should display 3.
    # the vowels are a, e, i, o, u
    # Hint: convert the string to lowercase and use a for loop with a counter 
    # variable and an if statement

word = input("Enter a word: ")
vowels = 0
word = word.lower()
for i in word:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1
print("Number of vowels are: ", vowels)

