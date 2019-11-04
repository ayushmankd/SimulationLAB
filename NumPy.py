import numpy as np
# 1-D Array Initialization
a = np.array([1, 2, 3], dtype="int16") # np.array() -> takes list as argument e.g [1, 2, 3], dtype = "Type of Data"
# 2-D Array Initialization
a = np.array([[1, 2, 4], [4, 5, 6]]) # takes a list of lists as argument
# get dimensions
a.ndim
# get shape
a.shape
# get type of data
a.dtype
# get specific element
a[row, col]
# get specific row
a[row, :]
# get specific col
a[:, col]
# initialize all zeros
a = np.zeros(shape)
# initailze all ones
a = np.ones(shape)
# any other num
a = np.full(shape, number)
# identity matrix
a = np.identity(n)
# copy array
a = np.array([1, 2, 3])
b = a.copy()
# adding n to every element
a = np.array([1, 2, 3])
a + n
# Matrix Mul of a and b
np.matmul(a, b)
# determinant of a
np.linalg.det(a)
# min max
np.min(a)
np.max(a, axis=1) #col wise
# Load data from file
a = np.genfromtxt('data.txt', delimiter=",")
