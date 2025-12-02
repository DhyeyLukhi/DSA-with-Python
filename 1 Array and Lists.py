from array import *
import numpy as np

a1 = array('i', [1, 2, 3, 4, 5])
print(a1)

for i in a1:
    print(i)


a1.append(6)
print(a1)
print("Count of 3:", a1.count(3))
print("Index of 4:", a1.index(4))
a1.pop()
print(a1)
a1.remove(2)
print("Remove 2", a1)
a1.insert(2, 10)
print("Insert 10 at index 2:", a1)

a = np.array([1, 2, 3, 4, 5])  # 1D array
print(a)
b = np.array([[1, 2, 3], [4, 5, 6]])  # 2D array
print(b)
c = np.array([[1, 2, 3], [10, 13]])  # 1D array with 2 elements, and both elements are lists
print(c)