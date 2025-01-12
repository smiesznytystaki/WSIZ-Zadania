import numpy as np

array1 = np.zeros((3, 3), dtype=int)
array1[2, :] = 1
print(array1)

array2 = np.zeros((3, 3), dtype=int)
array2[1, 1] = 1
array2[2, 1] = 1
print(array2)

array3 = np.zeros((3, 3), dtype=int)
array3[1, :] = 1
array3[2, :] = 1
print(array3)

array4 = np.zeros((3, 3), dtype=int)
array4[0, 0] = 1
array4[1, 0] = 1
array4[0, 2] = 1
array4[1, 2] = 1
print(array4)

array5 = np.zeros((3, 3), dtype=int)
array5[2, 1] = 1
array5[2, 2] = 1
array5[1, 1] = 1
array5[1, 2] = 1
print(array5)
