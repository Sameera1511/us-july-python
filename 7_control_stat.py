# For Loop:-

# Print "Hello World" 5 times using for loop.

# for i in range(0, 5):
#     print("Hello world")


# Write a program to print table of 5 using for loop

# for i in range(1, 11):
#     print(i * 5)


# Write a program to print all numbers which are even 
# from list1

# list1 = [34, 89, 0, 12, 67, 5, 4, 8, 88, 22, 1]

# for i in range(0, len(list1)): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#     if list1[i] % 2 == 0:
#         print(list1[i])

# Write a program to print all odd numbers from 
# list2

# list2 = [34, 5, 67, 8, 90, 1, 23, 99, 4, 2]

# for i in range(0, len(list2)):
#     if list2[i] % 2 != 0:
#         print(list2[i])

# for i in list2:
#     if i % 2 != 0:
#         print(i)


# Write a program to print all even numbers from 
# list3

list3 = [1, 4, "A", True, 50, "7", "14", 7, 99, 34, 3, "Apple", 7.8]

# for i in list3:
#     if type(i) == int:
#         if i % 2 == 0:
#             print(i)

# for i in list3:
#     if str(i).isdigit():
#         if int(i) % 2 == 0:
#             print(i)


# Write a program to print all vowels which are capital
# from bellow string 

str1 = "YtEjoLaUHM"   # EU

# for i in str1:
#     if i in "AEIOU":
#         print(i)



# Write a program to print bellow list 
# in reverse oder

l1 = [5, 2, 4, 9, 1, 6]   # [6, 1, 9, 4, 2, 5]

# print(l1[::-1])
# l2 = []
# for i in range(-1, -len(l1)-1, -1):
#     l2.append(l1[i])
# print(l2)


# for i in range(len(l1)-1, -1, -1):
#     print(i)

#-----------------------------------------

# Write a program to print fibonacci series upto
# 20 numbers.


# start = 0
# end = 1

# print(start)
# print(end)

# for i in range(2, 20):
#     new = start + end
#     print(new)
#     start, end = end, new

#-----------------------------------------
