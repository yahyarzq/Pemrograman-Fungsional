import numpy as np

def manipulate_row(P, k, i, j):
  # Isi function ini digunakan untuk memproses kalkulasi manipulate_row (baris i + (k * baris j)) pada matrix P
  R1, R2 = P[i], P[j]
  T1 = [k * R2[i] for i in range(len(R2))]
  T2 = [R1[i] + T1[i] for i in range(len(R1))]
  P[i] = T2
  return P # Function ini akan me-return matrix yang sudah dilakukan proses kalkulasi manipulate_row


def manipulate_rowa(P, k, i, j):
  # Isi function ini digunakan untuk memproses kalkulasi manipulate_row (baris i + (k * baris j)) pada matrix P
  R1, R2 = P[i], P[j]
  matrik = []
  for x in range(len(R1)):
    e = R1[x]+(k*R2[x])
    matrik.append(e)
  P[i] = matrik
  return P

def scale_row(P, k, i):
 # Isi function ini digunakan untuk memproses kalkulasi scale_row (baris i * k) pada matrix P
 Q = P[i]
 matrix = P[:]
 R = []
 for x in range(len(Q)):
   scale = k * Q[x]
   scale = np.ceil(scale)
   R.append(scale)
 matrix[i] = R
 return matrix #Function ini akan me-return matrix yang sudah dilakukan proses kalkulasi scale_row


def switch_row(P, i, j):
  # Isi function ini digunakan untuk memproses kalkulasi switch_row ((baris i = baris j),(baris j = baris i)) pada matrix P
  matrix = P
  matrix[i],matrix[j] = matrix[j],matrix[i]
  return matrix #Function ini akan me-return matrix yang sudah dilakukan proses kalkulasi switch_row

def get_result(function):
  def wrapper():
    HA = function()
    # Isi fanction ini sebagai decorator untuk gauss_jordan
    HE = f"Nilai a,b,c masing masing adalah {HA[0][3]}, {HA[1][3]}, {HA[2][3]}"
    return HE #Function ini akan mereturn string a,b,c beserta masing" valuenya sebagaimana yang didapatkan dari kalkulasi gauss_jordan
  return wrapper

@get_result
def gauss_jordan():
  X = [[2,1,2,10],[1,2,1,8],[3,1,-1,2]]
  print("X",X)
  X1 = switch_row(X, 0, 1) #nanti akan menghasilkan matrix X1 = [[1, 2, 1, 8], [2, 1, 2, 10], [3, 1, -1, 2]]
  print("X1",X1)
  X2 = manipulate_row(X1, -2, 1, 0) #nanti akan menghasilkan matrix X2 = [[1.0, 2.0, 1.0, 8.0], [0.0, -3.0, 0.0, -6.0], [3.0, 1.0, -1.0, 2.0]]
  print("X2",X2)
  X3 = manipulate_row(X2, -3, 2, 0) #nanti akan menghasilkan matrix X3 = [[1, 2, 1, 8], [0, -3, 0, -6], [0, -5, -4, -22]]
  print("X3",X3)
  X4 = scale_row(X3,-0.333 , 1)     # x-3 nanti akan menghasilkan matrix X4 = [[1, 2, 1, 8], [0, 1, 0, 2], [0, -5, -4, -22]]
  print("X4",X4)
  X5 = manipulate_rowa(X4,-2,0,1)   #nanti akan menghasilkan matrix X5 = [[1, 0, 1, 4], [0, 1, 0, 2], [0, -5, -4, -22]]
  print("X5",X5)
  X6  = manipulate_row(X5,5,2,1)  # -5 nanti akan menghasilkan matrix X6 = [[1, 0, 1, 4], [0, 1, 0, 2], [0, 0, -4, -12]]
  print("X6",X6)
  X7 =  scale_row(X6,-0.25,2)   # x-4  nanti akan menghasilkan matrix X7 = [[1, 0, 1, 4], [0, 1, 0, 2], [0, 0, 1, 3]]
  print("X7",X7)
  X8  = manipulate_row(X7,-1,0,2)    #nanti akan menghasilkan matrix X8 [[1, 0, 0, 1], [0, 1, 0, 2], [0, 0, 1, 3]]
  print("X8",X8) 
  
  # Teruskan kalkulasi sehingga menghasilkan matrix akhir = [[1.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 2.0], [0.0, 0.0, 1.0, 3.0]]
  
  
  
  # Teruskan mencetak hasil matrix sehingga menghasilkan matrix akhir = [[1.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 2.0], [0.0, 0.0, 1.0, 3.0]]
  return  X8 #return matrix terakhir

print(gauss_jordan())




