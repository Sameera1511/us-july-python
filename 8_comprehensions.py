# Comprehensions:
    # Single line code.
    # code inside collection

# l1 = [1, 2, 3, 4, 5]
# l2 = [i for i in range(1, 6)]
# print(l1)
# print(l2)

    # Types of Comprehensions:
        # 1) List Comprehension []
        # 2) Tuple Comprehension ()
        # 3) Set Comprehension {}
        # 4) Dict Comprehension {}

# List Comprehension:
    # Using LC we can create a list of elements
    # upto required length

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# l2 = []

# for i in range(1, 10000):
#     l2.append(i)

# print(l2)

# l3 = [i for i in range(1, 11)]
# print(l3)

#-------------------------------------------

# Create a list comprehension of all even numbers from
# 23 to 40 

# l4 = [i for i in range(23, 40) if i % 2 == 0]
# print(l4)

# Write a list comprehension to have all
# Capital letters from str1

# str1 = "Ag6%KlopQ"

# l1 = [char for char in str1 if char.isalpha() and char.isupper()]
# print(l1)

#  Write a comprehenion for all the numbers from 
# list bellow which are divisible by 5

# list1 = ["A", "O", "0", 67, 20, 75, 1, True, "Grape", 5.5]

# list2 = [i for i in list1 if type(i) == int and i % 5 == 0]
# print(list2)


#-------------------------------------
# Tuple Comprehension:

# Write a TC to print table of 9

# table_of_9 = (num*9 for num in range(1, 11))
# print(table_of_9)   #<generator object <genexpr> at 0x00000242CEF89490>

# for i in table_of_9:
#     print(i, end=" ")


# RAM => 16 GB
# HDD => 512GB  ()

#---------------------------

# Set Comprehension 

# Write a set comprehension
# where all the +ve numbers will be there
# and no dumplicates.

# l1 = [-3, 4, 6, 7, -4, 9, 0, -4, 2, 8, 8, 8, -5]
# set1 = {num for num in l1 if num> 0}
# print(set1)

# Dict Comprehension:

# Write a dict comprehension to create a 
# dictionary of number and its square
# refer l1

# l1 = [4, 2, 7, 9, 5, 1]

# dict1 = {num:num**2 for num in l1}
# print(dict1)

