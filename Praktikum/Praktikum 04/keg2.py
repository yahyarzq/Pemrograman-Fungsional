
def transpose(function):
    def wrapper():
        # Funtion tranpose berisikan fungsi transpose suatu matrix.
        # Function ini akan mengembalikan matrix tranpose dari matrix yang terdapat pada parameter di function ini.
        result = function()
        result.insert(2,result.pop(1)) # ini digunkan untuk mentraspose array eg. [6, 1, 2, 3] mjd [6, 2, 1, 3]
        return result
    return wrapper

def matrixaddition(function1, function2):
    # Function ini digunakan untuk menjumlahkan matrix X dan Y. Praktikan dilarang mendeklarasikan matrix X dan Y pada function ini.
    # Nantinya matrix X dan matrix Y dipanggil sesuai pada parameter function di function ini yaitu secara berturut-turut function1 dan function2.
    # Function ini akan mengembalikan list yang berupa matrix dari hasil penjumlahan matrix X dan Y.
    # Nilai dari penjumlahan tersebut disimpan dalam variabel XaddY.
    XaddY = list(function1[i] + function2[i] for i in range(len(function1)))
    return XaddY


def matrixZmultiplyA(function):
    def wrapper():
        #Nantinya variabel ini digunakan untuk menyimpan matrix Z.
        matrixZ = function()
        matrixA = [4, 1, 5, 2]
        # Diasumsikan matrixA = |4  1|
        #                       |5  2|
        # Function ini digunakan untuk mengalikan matrix Z * A.
        # Function ini akan mengembalikan hasil kali dari matrix Z dan matrix A.
        def slicer(arr) -> list: # Fungsi ini digunkan untuk memotong array diubah menjadi  2 dimenesi eg [1,2,3,4] menjadi [[1,2],[3,4]]
            result = [arr[slice(0,2)],arr[slice(2,4)]]
            return result
        
        slicedmatrixZ = slicer(matrixZ)
        slicedmatrixA = slicer(matrixA)
        res = [[0,0],[0,0]]
        for i in range(len(slicedmatrixZ)):
            for j in range(len(slicedmatrixA[0])):
                for k in range(len(slicedmatrixA)):
                    res[i][j] += slicedmatrixZ[i][k] * slicedmatrixA[k][j]
        result = [x for z in res for x in z]
        # result = list( ((matrixZ[i] * matrixA[i]) + (matrixZ[i] * matrixA[x])) for i in x for x in matrixA )
        return result
    return wrapper


# Isikan decoration untuk men-transpose-kan matrix X
@transpose
def matrixX():
    matrixX = [6, 1, 2, 3]
    # Diasumsikan matrixX = |6  1|
                          # |2  3|
    return matrixX

# Isikan decoration untuk men-transpose-kan matrix Y
@transpose
def matrixY():
    matrixY = [3, 2, 4, 5]
    # Diasumsikan matrixY = |3  2|
    # |4  5|
    return matrixY

# Isikan decoration untuk mengalikan matrix Z dengan matrix A, lalu transpose hasil kali tersebut
@transpose
@matrixZmultiplyA
def resultmatrix():
    # Panggil function matrixaddition untuk menjumlahkan matrix X dan matrix Y, sesuaikan parameternya.
    matrixadd = matrixaddition(matrixX(), matrixY())
    return matrixadd


print(resultmatrix())
