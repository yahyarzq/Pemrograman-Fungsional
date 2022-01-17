''' Program to transpose a matrix using list comprehension'''

X = [[12, 7],
     [4, 5],
     [3, 8]]

result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
    print(r)


Y = [12, 4, 3]

result = list(Y[0] for i in range(len(Y)))

print(result)


def matrixX():
    matrixX = [6, 1, 2, 3]
    # Diasumsikan matrixX = |6  1|
    # |2  3|
    return matrixX


def ddgd(function):
    mattrex = []
    for i in range(len(function)):
        mattrex.append([i])
    return mattrex


import numpy 
matrix=[3, 2, 4, 5]
print(matrix)
print("\n")
print(numpy.transpose(matrix))


# You need to install numpy in order to import it
import numpy as np
matrix = np.array([3, 2, 4, 5])
print(matrix)
print("\n")
print(matrix.T)
print(matrix.T.tolist())


[3, 2, 4, 5]

[3, 2, 4, 5]
3, 4, 2, 5

matrixfg =[6, 1, 2, 3]
print(matrixfg)
matrixfg.insert(2,matrixfg.pop(1))
print(matrixfg)

