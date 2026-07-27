# Error and Exception:

    # Types of Errors:
        # Type Error
        # ZeroDivisionError
        # ValueError
        # IndentationError
        # SyntaxError
        # NameError
        # IndexError
        # KeyError

#-----------------------------------------

# Write a program to divide 7 by any number:

# denominator = eval(input("Enter a denominator: "))
# print(7/denominator)

# try:  # Actual Operation Responsibility
#     denominator = eval(input("Enter a denominator: "))
#     division = (7/denominator)

# except ZeroDivisionError: # If ZeroDivisionError Occurs then this block activates
#     print("Dividing by 0 is invalid.")

# else: # if try block doesnt throw an error then it executes.
#     print(division)

# finally: # At the End wether error or output this block will execute
#     print("Program executed successfully..!")

#------------------------------------------

# Write a program which prints element from bellow
# list, using index number. Ask user what 'index number' number
# want.


# l1 = [121, 232, 343, 454, 565, 676]

# try:
#     indx = int(input("Enter Index Number: "))
#     element = l1[indx]

# except IndexError:
#     print("Provided Index is out of range.")

# except ValueError:
#     print("Provided incorrect Input.")

# else:
#     print(element)

# finally:
#     print("Program executed successfully.")

#-----------------------------------------

# Write a program to print values from bellow
# dictionary

d1 = {
    "Fruits":["Apple", "Banana", "Grapes", "Avocado"],
    "Sports": ["Cricket", "Kabbadi", "Football", "Hockey"],
    "Cars": ["Tata", "Mahindra", "Tesla", "Nissan", "Suzuki"]
}
# print(d1["Flowers"])   

# print(d1.get("Fruits"))
# print(d1["Fruits"])

# try:
#     key = input("Enter key: ")
#     val = d1[key]

# except KeyError:
#     print("Provided Key is not Valid.")

# else:
#     print(val)

# finally:
#     print("Program executed successfully..!")



#--------------------------------------

# Write a program to print the eligibility of 
# a person to get a VoterCard.
# if person age >= 18 => Eligibile
# if person age 1 >< 18  => Not Eligible
# User can enter -Ve Age ==> NegativeAgeError

class NegativeAgeError(Exception):
    pass

# try:
#     age = int(input("Enter your age: "))
#     result = None
#     if age > 0 and age < 18:
#         result = "Not Eligible"
#     elif age >= 18:
#         result = "Eligible"
#     else:
#         raise NegativeAgeError()

# except NegativeAgeError:
#     print("Age can not be negative")

# else:
#     print(result)

# finally:
#     print("Bye Bye..!")

#---------------------------------------------

# age = int(input("Enter your age: "))

# if age < 0:
#     raise NegativeAgeError("-ve age is not allowed")
# elif age > 0 and age < 18:
#     print("Not Eligible")
# else:
#     print("Eligible")
