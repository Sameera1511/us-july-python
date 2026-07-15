# Datatpes:
    # 1) Int => Integer
        # Integers are numbers without decimal point including 0
        # Integers can be +ve , -ve

# x = 6
# print(x)
# print(type(x))   #<class 'int'>

# y = 0
# print(y)
# print(type(y))

# z = 4.0
# print(z)
# print(type(z))


    # 2) Float => Float
        # A number with decimal point is float
        # float can be _ve, +ve

# a = 7.5
# print(a)
# print(type(a))

# b = 0.0000
# print(b)
# print(type(b))

    # 3) Complex => Complex
        # A combination of Real numbers and Imaginary numbers.
            # Real:
                # All Integers and Floats are real numbers.
            # Imaginary:
                # A number which comes with 'j' suffix

            # 5+5j => Complex
# p = 4-8j
# print(p)
# print(type(p))


    # 4) String
        # String is a sequence of charecters (alphabetic, numeric, special)
        # collection of charecters is enclosed by quotes.
        # Types of quotes used for string formation:
            # ''  => Single quotes
            # ""  => Double quotes
            # ''' ''' => Tripple single quotes
            # """ """ => Tripple double quotes

# Examples:
# str1 = 'Hello'
# print(str1, type(str1))   # str

# str2 = "Apple"
# print(str2, type(str2))

# str3 = "Kumar@123"
# print(str3, type(str3))

# str4 = '''This is a new car..!'''
# print(str4, type(str4))

# str5 = """My dear friend Mr. Bean."""
# print(str5, type(str5))

# Sara is the most 'Beatiful' women in the town.
# str6 = "Sara is the most 'Beatiful' women in the town."
# print(str6, type(str6))

# str7 = '''
# Hello brother stephan..!
# welcome to "church"..
# may "god" bless you with all the 'happiness' and 'welth'..
# '''
# print(str7, type(str7))

# Built in methods (functions)
# str100 = "Hello"
# str200 = "my dear friend"
# str300 = "INDIA IS MY COUNTRY"
# Case manipulation functions:
        # .upper()
# print(str100.upper())   #HELLO

        # .lower()
# print(str100.lower())   #hello

        # .capitalize()
# print(str200.capitalize()) #My dear friend
# print(str300.capitalize()) #India is my country

        # .title()
# print(str200.title())      #My Dear Friend
# print(str300.title())      #India Is My Country

        # .swapcase()
# str400 = "Nigeria IS NIce"
# print(str400.swapcase())   #nIGERIA is niCE

# Indexing:
    # Positive Indexing => starts from 0
    # Negative Indexing => starts from -1
str1 = "APPLE"

# print(str1)
# print(str1[0])
# print(str1[-5])

# print(str1[1])
# print(str1[-4])

# print(str1[4])
# print(str1[-1])

# -------------------------------
# SLICING:
# print(str1[0:3:1])
# print(str1[2::1])
# print(str1[0::2])
# print(str1[0:5:3])

# print(str1[-5::2])
# print(str1[-1::-2])

#--------------------------------
# str2 = '1234'
# str3 = 'amma@123'
# str4 = "     "

# print(str2, type(str2))

# is methods of string:
    # .isalpha()
# print(str2.isalpha())
# print(str1.isalpha())
# print(str3.isalpha())


    # .isdigit()
# print(str1.isdigit())
# print(str2.isdigit())
# print(str3.isdigit())

    # .isspace()
# print(str1.isspace())
# print(str4.isspace())

    # .isalnum()
# print(str1.isalnum())
# print(str2.isalnum())
# print(str3.isalnum())
# print(str4.isalnum())

# s1 = "app le"
# print(s1.isalpha())
# print(s1.isspace())
#----------------------------------------------------------------
    # 5) Boolean
        # It represents True or False.
        # Always True has numeric value 1
        # Always False has numeric value 0

# print(True + True + True)
# print(5 * False)
# print((True * True - True +False) * True + (False -True))


    # 6) List:
        # Collection Datatype
        # It is heterogenous  --> Allow all types of datatypes inside it.
        # It is mutable --> It can be Modified
        # Supports Indexing
        # Allow Duplicates
        # Intialized using []

# marks = [12, 34, 56, 32, 89, 55, 30, 90]
# print(marks, type(marks))

# students = ["Ajain", "Sharmishta", "Imran", "Amit", "Jay"]
# print(students, type(students))

# list1 = [12, 5.5, 4+6j, "Laxmi", True, [1, 2, 3, False]]
# print(list1, type(list1))

#--------------------------------------------------------
# Initializing list using literal / function 

# age = list([78, 56, 40, 89, 20])  #TypeError: list expected at most 1 argument, got 5
# names = list(("X", "Y", "A", "M"))
# numbers = list({1, 2.2, 4, 5.5})
# print(numbers, type(numbers))
# ---------------------------------------------------

# Indexing:
# l1 = [10, 222, 34, 54, 89, 100]
# 89, 34, 10  [0::2]  [-2::-2]
# 100, 54, 222  [-1:-5:-2]
# 10, 54 [0::3]

# print(l1[0])  # 10
# print(l1[-3])  # 54
# print(l1[-4])  # 34
# print(l1[7])   # Error  IndexError: list index out of range
# print(l1[-7])  # Error  IndexError: list index out of range

# Slicing:

# print(l1[-2::-2])
# print(l1[-1::-2])
# print(l1[0::3])

#-------------------------------
# List In Built Methods:
l2 = [12, 23, 34, 45]
# print(l2[0:1] + l2[2::])  # [12] + [34, 45]  Concatination

# print(l2[0] + l2[1])  # 12 + 23  # Addition


# insertion and deletion methods:
    # .append()  # adds single element at end 
    # .extend()  # adds multiple elements at end
    # .insert()  # to add element at particular index
l2 = [12, 23, 34, 45, 23]  
# l3 =[100, 200, 300]
# l2.insert(1, l3[0])
# l2.insert(2, l3[1])
# l2.insert(3, l3[2])

# l2.insert(1, l3)
# l2.append(l3)
# l2.extend(l3)
# print(l2)

# l2.append(60)  #[12, 23, 34, 45, 60]
# l2.extend([100, 200])
# l2.insert(2, 900)

    # Deletion methods:
        # .pop()   # deletes any last element
        # .remove()  # deletes element 
        # .clear()  # deletes all elements
# l2.pop()
# print(l2)
# l2.remove(23)
# print(l2)
# l2.clear()
# print(l2)
# del l2[0]
# print(l2)

    # Searching Elements from list:
        # .index()

# print(l2.index(23))
#-------------------------------------------------------


    # 7) Tuple:
        # Collection Datatype
        # It is Heterogeneous
        # It is Immutable
        # It is Ordered so allows indexing
        # It can be initialized using ()

# tup1 = ()
# print(tup1, type(tup1))

# tup2 = tuple()
# print(tup2, type(tup2))

# tup3 = (12, 3.4, True, "Sahil", [1, 2, 3], (10, 20, "A"))
# print(tup3, type(tup3))

#---------------------------------------------

# Indexing
t1 = (12, 23, 34, 45, 56)
# print(t1[2], t1[-3])
# print(t1[1], t1[-4])

# Slicing:
# 12, 23, 34
# print(t1[0:3:1])
# 56, 34, 12, 23
# t1 = (12, 23, 34, 45, 56)
# print(t1[-1:-4:-2] +t1[0:2:1])

# IN built Methods:
    # .index()
    # .count()

# t2 = (1, 23, 2, 4, 1, 5, 6, 1, 8, 4, 9, 3, 23)
# print(t2.index(1))
# print(t2.index(5))

# print(t2.count(1))
# print(t2.count(23))


    # 8) Set
        # It is collection datatype
        # It is partially Heterogeneous
        # It is mutable
        # It is unordered so doesnt support indexing
        # It doesnt alllow duplicates
        # Elements are randomly placed
        # Set is initialized using {}

# set1 = {1}
# print(set1, type(set1))

# set2 = set()
# print(set2, type(set2))

# set3 = {1, 2, 3, 4, 1, 2, 3, 4, 5}
# print(set3)

# set4 = {1, 3.4, 6+7j, False, (1, 2, 3), "Ajain"}
# print(set4)

# IN built methods:
set5 = {11, True, (1, 2, 3), "Sara", 4.5}
#     # .add()  it adds element in set
# set5.add(100)
# print(set5)

    # .pop()  # Randomly any element will e removed
# set5.pop()
# print(set5)

#     # .remove()   # takes specific element to remove
# set5.remove(100)
# print(set5)

    # .clear()
# set5.clear()
# print(set5)

    # some other set operations
    # Union |
    # Difference -
    # INtersection &
s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}

# UNion
# print(s1 | s2)

# Intersection
# print(s1 & s2)

# Difference
# print(s1 - s2)
# print(s2 - s1)


    # 9) Range

    # 10) Dict