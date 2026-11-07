import numpy as np

matrix = np.array([[80,90],[70,60],[95,85],[60,70]])
print(matrix)
print(matrix.shape)


print("3rd student, it mean 2nd index")
print(matrix[2,:])
print("Get everyone test2_score")
print(matrix[:,1])
print("Particular value")
print(matrix[0,1])


A = np.array([[2,0],[1,3]])
B = np.array([[4,1],[2,5]])
print(A @ B)

M = np.array([[10,20,30],[40,50,60]])
print(M[1,:])


P = np.array([[1,2],
     [3,4]])
Q = np.array([[2,0],
     [1,2]])

print(P @ Q)
