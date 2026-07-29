# NUMPY:

    # It is a python library for working with linear algebra, 
    # fourier transformers and matrices.

    # Num + Py => Numeric Python

    # It is open source

# Why use numpy in analytics:

    # In python we have list that serves the purpose of array.

    # The problem with list is they are slow.

    # Thats the reason we developed Numpy which will create 
    # pythonic array, which is 50X faster.

    # Numpy aims to provide an array object that is also
    # called ndarray (N-Diamensional Array)

# Why numpy is faster than List ?
    # List stores data in discontinous manner in memory
    # which takes maximum tome to assemble scattered data
    # and process.

    # Numpy arrays are stored at one continuous place.

#--------------------------------------------------------------


import numpy as np

# First Numpy array using list
# arr1 = np.array([1, 2, 3, 4, 5])
# print(arr1)

# Second Numpy array using tuple
# arr2 = np.array((10, 20, 30, 40, 50))
# print(arr2)

# Check Version of numpy
# print(np.__version__)   #2.4.4

#------------------ Diamensions ----------------

# # 0-D Array
# arr3 = np.array(12)
# print(arr3)
# print(arr3.ndim)

# # 1-D Array
# arr4 = np.array([9, 4, 6, 1, 9])
# print(arr4)
# print(arr4.ndim)

# # 2-D Array
# arr5 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr5)
# print(arr5.ndim)


# # 3-D Array
# arr6 = np.array([
#     [
#         [1, 2],
#         [3, 4]
#     ],
#     [
#         [5, 6],
#         [7, 8]
#     ]
# ])

# print(arr6)
# print(arr6.ndim)
#---------------------------------------
# Array Indexing:

# arr7 = np.array([1, 2, 3, 4])
# print(arr7)
# print(arr7[0])
# print(arr7[3])
# print(arr7[-2])
# print(arr7[-4])

# arr8 = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ])

# print(arr8[0, 1])
# print(arr8[1, 2])

# arr9 = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ])

# print(arr9[-2, -1, -3])
# print(arr9[-1, -1, -2])
# print(arr9[0, 1, 2])
# print(arr9[1, 1, 1])
# print(arr9[1, 0, 2])

#----------------------------------------

# arr10 = np.array([1, 2, 3, 4, 5, 6, 7])

# # print(arr10[4::])
# # print(arr10[-2:2:-2])

# arr11 = np.array([
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10]
# ])

# # print(arr11[0, 2:])
# # print(arr11[1, 3:0:-2])

# print(arr11[0:2, 2])

#---------------------------------------------
# Datatypes in Numpy:
    # Strings
    # Float
    # Integer
    # Complex

# a1 = np.array([1, 2, 3, 4])
# print(a1)
# print(a1.ndim)
# print(a1.dtype)

# b1 = np.array(["A", "B", "C"], dtype='S')
# print(b1)
# print(b1.ndim)
# print(b1.dtype)

# c1 = np.array([1.1, 2.2, 3.3, 4.4])
# print(c1)
# print(c1.dtype)

#--------------------------

# Shape of an Array:

# aa1 = np.array([1, 2, 3, 4])
# print(aa1.shape)

# aa2 = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# print(aa2.shape)


# aa3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ndmin=1)

# print(aa3)
# print(aa3.ndim)
# print(aa3.dtype)
# print(aa3.shape)

# aa3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# aa4 = aa3.reshape(3, 4)
# aa5 = aa3.reshape(2, 6)
# print(aa5)

#-------------------------------------
# Iterating ndarray

# a1 = np.array([1, 2, 3, 4])

# for i in a1:
#     print(i)

# a2 = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# for i in a2:
#     for j in i:
#         print(j)

# a3 = np.array([
#     [
#         [1, 2, 3],
#         [4, 5, 6]
#     ],
#     [
#         [7, 8, 9],
#         [10, 11, 12]
#     ]
# ])

# for i in a3:
#     for j in i:
#         for k in j:
#             print(k)


#------------------ Concatinating -------------------

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

# a3 = np.concatenate((a1, a2))
# print(a3)

# [1, 2, 4, 5]
# a4 =np.concatenate((a1[0:2], a2[0:2]))
# print(a4)

#------------------------------------

# Split Arry:

import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# arr1 = arr.reshape(4, 2)

# new_arr1 = np.array_split(arr1, 4)
# print(new_arr1)

# newarr = np.array_split(arr, 3)
# print(newarr[0])
# print(newarr[1])
# print(newarr[2])


#--------------------------------------
# Array Search:

arr = np.array([1, 2, 3, 4, 5, 4, 4])

# x = np.where(arr==4)
# print(x)

# y = np.where(arr==2)
# print(y)

#---
# arr1 = np.array([10, 14, 93, 41, 8, 7])
# 2, 3, 5

# x = np.where(arr1%2 != 0)
# print(x)

# y = np.where(arr1 > 50)
# print(y)

# z = np.where(arr1%7 != 0)
# print(z)

#---------------------

# arr2 = np.array([6, 7, 9, 8])

# x = np.searchsorted(arr2, 7)
# print(x)

# y = np.searchsorted(arr2, 8)
# print(y)

#-----------------------
# arr3 = np.array([3, 2, 0, 1])

# print(np.sort(arr3))


arr4 = np.array(["banana", "cherry", "apple"])
# print(np.sort(arr4)[::-1])

# arr5 = sorted(np.sort(arr4), reverse=True)
# print(arr5)

#-----------------------------
# arr6 = np.array([True, False, True])
# print(np.sort(arr6))

#-----------------------------

# arr7 = np.array([
#     [3, 2, 4],
#     [5, 0, 1]
# ])

# print(np.sort(arr7))

#------------------------

# arr8 = np.array([41, 42, 43, 44])

# x = [True, False, True, False]

# newarr = arr8[x]
# print(newarr)


arr9 = np.array([41, 42, 43, 44])

# x = (arr9 > 42)
# print(arr9[x])

# x = np.array(list(filter(lambda val1: val1 if val1 > 42 else None, arr9)))
# print(x)

# arr10 = np.array([i for i in arr9 if i > 42])
# print(arr10)


# filter_arr = []

# for i in arr9:
#     if i > 42:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)

# newarr = arr9[filter_arr]
# print(newarr)

