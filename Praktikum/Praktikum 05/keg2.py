

def multiply(na, ma) -> list:
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # iterate through rows of X
    for i in range(len(na)):
        # iterate through columns of Y
        for j in range(len(ma[0])):
            # iterate through rows of Y
            for k in range(len(ma)):
                result[i][j] += na[i][k] * ma[k][j]
    return result


# Testing
def minorMatrix(arr, i, j):
    minor = [row[:j] + row[j+1:] for row in (arr[:i] + arr[i+1:])]
    return minor


# Testing
def determinantMatrix(n):
    if len(n) == 2:
        return (n[0][0]*n[1][1]-n[0][1]*n[1][0])*1.0
    determinant = 0
    for c in range(len(n)):
        determinant += ((-1)**c)*n[0][c] * \
            determinantMatrix(minorMatrix(n, 0, c))
    return determinant


def determinant(n):
    DE = n[0][0]*((n[1][1]*n[2][2])-(n[1][2]*n[2][1])) \
        - n[0][1]*((n[1][0]*n[2][2])-(n[1][2]*n[2][0])) \
        + n[0][2]*((n[1][0]*n[2][1])-(n[1][1]*n[2][0]))
    return DE


def cofactor(n):
    cofactorsMatrix = []
    for r in range(len(n)):
        cofactor = []
        for c in range(len(n)):
            minor = minorMatrix(n, r, c)
            cofactor.append(((-1)**(r+c)) * determinantMatrix(minor))
        cofactorsMatrix.append(cofactor)
    return cofactorsMatrix


def transpose(n):
    A = list([j[i] for j in n] for i in range(len(n[0])))
    return A


def invers(n, determinant):
    for r in range(len(n)):
        for c in range(len(n)):
            n[r][c] = n[r][c]/determinant
    return n


def power(n, p):
    b = n

    def inner_power(n, p):
        if p == 0:
            return n
        if p >= 1:
            return inner_power(inner_multiply(n, b), p-1)

    def inner_multiply(na, ma):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        # iterate through rows of X
        for i in range(len(na)):
            # iterate through columns of Y
            for j in range(len(ma[0])):
                # iterate through rows of Y
                for k in range(len(ma)):
                    result[i][j] += na[i][k] * ma[k][j]
        return result
    return inner_power(n, p)

def result(function):
  def wrapper():
    HA = function()
    HE = f"Hasil Akhir Adalah\n{HA[0]}\n{HA[1]}\n{HA[2]}"
    return HE 
  return wrapper

#Testing
def matrixA():
    return [[4, 2, 8], [2, 1, 5], [3, 2, 4]]
def matrixB():
    return [[2, 0, 0], [0, 5, 0], [0, 0, 4]],
def matrixAinvers():
    return [[4, 2, 8], [2, 1, 5], [3, 2, 4]]

@result
def matrixABA():
    X1 = [[4, 2, 8], [2, 1, 5], [3, 2, 4]]
    X2 = [[2, 0, 0], [0, 5, 0], [0, 0, 4]]
    XS = invers(transpose(cofactor(X1)), determinantMatrix(X1))
    XA = multiply(XS, multiply(X1, power(X2, 2)))
    #XZ = matrixA()*matrixB()*matrixAinvers()
    return XA
    
print(matrixABA())
