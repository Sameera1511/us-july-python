# Print "Hello World" 50000 times.

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# Above solution is not right.
#------------------------------------------------------

# Print "Hello World" 5 times using while loop:

# count = 0
# while count < 5:   #True  0 1 2 3 4
#     print(f"Hello World")
#     count+=1

#-----------------------------

# Write a program to print all even numbers in between 0 to 10

# start = 1

# while start <= 10:   # 1
#     if start % 2 == 0:
#         print(start)
#     start+=1
#------------------------------------

# Write a table of 2

# start = 1

# while start <=10:
#     print(f"28 * {start} = {28*start}")
#     start +=1

#--------------------------------------
# Write a program to print all numbers from 1 to 100
# which are divisible by 5 as well 3

# start = 1
# while start <=100:
#     if start % 5 == 0 and start % 3 == 0:
#         print(start)
#     start +=1

#------------------------------
# Write a program to print fibonacci series upto user 
# asks for.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

# num_of_nums = int(input("How many numbers do you want from fibonacci series: "))

# start = 0
# end = 1

# count = 0
# print(start)
# print(end)

# while count < num_of_nums-2:   # 5-2 =3
#     new_num = start + end
#     print(new_num)
#     start = end
#     end = new_num
#     count+=1

#--------------------------------------------

# Write a program to print all consonents from
# str1

# str1 = "Ajain"   # jn


# print(len(str1))

# index = 0
# while index < len(str1):
#     if str1[index] not in "AEIOUaeiou":
#         print(str1[index])
#     index+=1

#------------------------------------

# Write a program to print all Special charecters 
# from str2

# str2 = "In$01Gh&k!"  # $&!
# index = 0
# while index < len(str2):
#     if not(str2[index].isalnum()):
#         print(str2[index])
#     index+=1

#------------------------------

# Write a program to print armstrong numbers in between 100 and 1000.
# 153 => 1**3 + 5**3 + 3**3
#     => 1 + 125 + 27
    # => 153

# 9474 => 9**4 + 4**4 + 7**4 + 4**4

# number = 100
# while number <= 1000:
#     power = len(str(number))
#     count = 0
#     total = 0
#     while count < len(str(number)): #3
#         total += int(str(number)[count]) ** power
#         count+=1
#     if total == number:
#         print(number)
#     number+=1
