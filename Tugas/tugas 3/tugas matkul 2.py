
my_list = [1,2,3,4,5]

def muul():
    sum = 0
    for x in my_list:
        sum = sum + ( x ** 2)
    print(sum)
        
muul()

def konversiCtoF(a):
    return (a * 9/5) + 32


def celciusToFahreneitArray():
    return list(map(lambda a: konversiCtoF(a), my_list))

idx = 0
result = []
#Perubahan yang saya tambah adalah penambahan fungsi "celciusToFahreneitArrayLoopingFunction",
# fungsi tersebut digunkan untuk mengalikan value di array "my_list" secara looping
# Masalah yang muncul bagimana cara agat output dari fungsi tersebut bisa tersimpan ke variable global "result"
# Karena variable tersebut tidak dapat diakses dari fungsi "loopingFunc"
# oleh karena itu saya menggunkan "global" agar memanggil variable "result" didalam  fungsi "loopingFunc"
#
#
def celciusToFahreneitArrayLoopingFunction():
    global result #digunakan agar bisa mamasukkan data ke dalam variable result, data berasal dari fungsi " loopingFunc(idx) "
    def loopingFunc(idx):
        if 0 <= idx < (len(my_list)):
            result.append(konversiCtoF(my_list[idx]))
            loopingFunc(idx+1)
        else:
            pass
    loopingFunc(0)
    return result
            

print(celciusToFahreneitArray())
celciusToFahreneitArrayLoopingFunction()
print(result)
