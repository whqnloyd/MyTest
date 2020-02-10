import numpy as np

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
data2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

array1 = np.array(data1)
array2 = np.array(data2)

# print(np.shape(array1))
# print(np.shape(array2))

# print(array1[2])
# print(array2[2, 2])
# print(array2[0:1])
#
# array3 = np.reshape(array1, (3, 3))
# print(np.shape(array3))

# #add
# array4 = array1 + 1
# print(array4)
# array5 = array4 + array1
# print(array5)

# #subtract
# array4 = array1 - 1
# print(array4)
# array5 = array1 - array4
# print(array5)

# # multiply
# array4 = array1 * 2
# print(array4)
# array5 = array3 * array2
# print(array5)

# # transport
# array4 = array2.transpose()
# print(array4)

# # inverse
# #array4 = np.array([[1, -1], [1, 1]])
# array4 = np.mat('1 -1; 1 1')
# print(array4)
# inverse = np.linalg.inv(array4)
# print(inverse)

# # spe for y=xw+b
# w = np.mat('-1 2; -2 1')
# b = np.mat('1 -1')
# x = np.mat('5 -5')
# print(np.shape(w))
# print(np.shape(b))
# print(np.shape(x))
# y = x * w + b
# print(np.shape(y))
# print(y)
