# Lambda:
    # It is anonymous function
    # A nameless function
    # A function without name
    # Lambda's are single line codes

# What is Function ?
    # A Function is a reusable block of code.


# Create a lambda function to add two numbers.

# total = lambda num1, num2: num1 + num2

# print(total(7, 9))     #16
# print(total(123, 677)) #800
# print(total(343, 908)) #1251


# Write a lambda which takes number as input and 
# returns wether number is even or odd.

# result = lambda number: "Even" if number % 2 == 0 else "Odd"
# print(result(7))
# print(result(123))
# print(result(68))

#------------------------------------------

# Write a lambda function which will reverse a string

# reverse_string = lambda string:string[::-1]
# print(reverse_string("APPLE"))

#--------------------------------------------------

# Write a program to check a datatype of 
# provided input parameter

# check_dtype = lambda data: type(data)

# print(check_dtype(5))
# print(check_dtype("Hello"))
# print(check_dtype([1,2,3,4]))

#------------------------------------------

# Write a lambda to check wheter entered alphabetic
# charecter is Capital of Small

# check_char_case = lambda char: "Capital" if char.isupper() else "Lower"

# print(check_char_case("A"))
# print(check_char_case("s"))



# map()  
    # It is used in conjuction with lambda function
    # it will take two inputs 
            # lambda func
            # collection
l1 = [1, 2, 3, 4, 5, 6, 7]   # 28
# use lambda with map and get the squares of l1 numbers.

# result = list(map(lambda num: num**2, l1))
# print(result)  #[1, 4, 9, 16, 25, 36, 49]


# filter()
    # It is used in conjuction with lambda function
    # it will take two inputs 
            # lambda func
            # collection
# create a list of even numbers from l1 
# using filter with lmbda .
# evens = list(filter(lambda num: num if num%2==0 else None, l1))
# print(evens)

# reduce()
    # It is used in conjuction with lambda function
    # it will take two inputs 
            # lambda func
            # collection

# Get the sum of l1 numbers using reduce

from functools import reduce

# total = reduce(lambda num1, num2: num1+num2, l1)
# print(total)

# #----------------------------
# l1 = [1, 2, 3, 4, 5, 6, 7]   # [1, 4, 9, 16, 25, 36, 49]


# Get the square of each number

# square = lambda num: num * num
# print(square(5))

#----------------------------------------------

# str1 = "Hakunamatata"
# # Using lambda i want to get all consonents

# consonents = list(filter(lambda char: char if char.upper() not in "AEIOU" else None, str1))
# print(consonents)

#----------------------------------------------

# Write a program using lambda to get the highest number 
# from str1
# str1 = "736592"

# highest = reduce(lambda num1, num2: num1 if int(num1) > int(num2) else num2, str1)
# print(highest)

#--------------------------------------------------------

# Write a program to get the all special charecters
# from tup1
# tup1 = ("A", 3, 1.1, False, "&", ".", " ", "E")

# result = list(filter(lambda x: (x if not(x.isalnum()) else None) if type(x) == str else None, tup1))
# print(result)

# result = list(filter(lambda x: x if type(x) == str and not(x.isalnum()) else None, tup1))
# print(result)

