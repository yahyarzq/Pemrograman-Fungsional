def hof_product(multiplier):
    return lambda x: x * multiplier

mult6 = hof_product(6)
print(mult6(6)) # 36


# Python program to demonstrate
# lambda functions
 

asd ="GeeksforGeeks"
 
# lambda gets pass to print
(lambda gh : print(gh))(asd)

increment = lambda a: a+1
decrement = lambda a: a-1
print(increment(100))
print(decrement(200))


# Double all numbers using map and lambda
  
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(result)




print("==================================================================================")
import json

def readdatajson():
    path = "C:/Users/PC/Documents/Praktikum Pemrograman Fungsional/Praktikum 02/data.json"
    return json.load(open(path))

def printcostum(data):
    print("#####################################")
    print("  Id Barang = ", data['id'])
    print("  Nama Barang =  ", data["data"]["nama_barang"])
    print("  Jumlah Barang = ", data["data"]["jumlah_barang"])
    print("#####################################")

print_barang = lambda a: list(map(printcostum, a))

print_barang(readdatajson()["stok_barang"])
print(x(readdatajson()["stok_barang"]))