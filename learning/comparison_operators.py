
#Comparison operators
# Logical operators
# Decision making
# loops(for loops, while loops, range, enumerator)
# min/max practice
# Random in python
# List comprehension


# review practice
# Append the value of current to the end of the list seconds Please use the list.append() method to do that.


# seconds = [1.23, 1.45, 1.02]
# current = 1.11
# print(seconds.append(current))
# print(seconds)
# # Remove item 1.45 from seconds.
# seconds = [1.23, 1.45, 1.02, 1.11]
# seconds.remove(1.45)
# print(seconds)

# # Remove items 1.45, 1.02, and 1.11 from seconds.
# seconds = [1.23, 1.45, 1.02, 1.11]

# seconds.remove(1.45)
# seconds.remove(1.02)
# seconds.remove(1.11)
# print(seconds)
################################comparison operators#########################
#remember....
# > greater
# < less
# >= greater or equal
# <= less or equal
# == equal
# != different or not equal to




# Comparison Operators Practice  1:
# Create two variables (num1 and num2) with the following values: 36 and 17. Check if num1 is greater than or equal to num2 and store the result of that comparison in a variable called my_bool

# num1= 35
# num2= 17

# if num1 >= num2:
#     my_boo= print(True)
# else:
#     print(False)


# Comparison Operators Practice  2:
# Create two variables (num1 and num2):
# Inside num1, store the result of the square root of 25
# Inside num2, store the number 5.
# Check if num1 is equal to num2 and store the result of that comparison in a variable called my_bool.

from math import*

# num1=sqrt(25)
# num2=5

# my_bool= num1==num2
# print(my_bool)

# Comparison Operators Practice #3:
# Create two variables (num1 and num2):
# Inside num1, store the result of 64 x 3
# Inside num2, store the result of 24 x 8
# Check if num1 is different from num2 and store the result of that comparison in a variable called my_bool.

# num1=64 * 3
# num2=24 * 8

# my_bool= num1 != num2
# print(my_bool)


#######################comparison operators challenge#####################
# Challenge: Compare two numbers entered by the user and check if they are equal or not.
# If they are not equal, print which one is greater.
num1=int(input('Enter a number:'))
num2=int(input('Enter another number:'))

if num1 == num2:
    print("they are equal")
elif num1> num2:
    print("Number 1 is greater than Number 2")
elif num1 < num2:
    print("Number 2 is greater than Number 1")
# Check for equality and greater number