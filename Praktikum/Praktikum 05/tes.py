import copy
def new_matrix(a, i):  # FUNCTION TO FIND THE NEW MATRIX
    arr = copy.deepcopy(a)
    if len(arr) == 2:

        return arr
    else:
        arr.pop(0)
        for j in arr:
            j.pop(i)
        print(arr)
        return arr


def determinant(a):  # FUNCTION TO FIND THE DETERMINANT OF A MATRIX
    if len(a) == 1:
        pro = a[0]
        return pro


    elif len(a) == 2:
        pro = a[0][0]*a[1][1] - a[1][0]*a[0][1]
        return pro

    else:
        pro = 0
        for i in range(len(a[0])):
            pro += ((-1)**i)*a[0][i]*determinant(new_matrix(a,i))    
        return pro         
            
A = [2]
B = [[1,2,4],[3,4,7],[5,6,7]]
C = [[1,2,3,4],[4,3,5,6],[8,4,2,1],[3,2,4,1]]
D = [[1,3,5,7,9],[4,6,3,7,5],[5,10,8,3,1],[1,5,3,7,6],[8,1,7,5,8]]
E = [[1,3,1],
     [1,1,2],
     [2,3,4]]
print("The determinant of A --> ",determinant(A))
print("The determinant of B --> ",determinant(B))
print("The determinant of C --> ",determinant(C))
print("The determinant of D --> ",determinant(D))
print("The determinant of E --> ",determinant(E))
