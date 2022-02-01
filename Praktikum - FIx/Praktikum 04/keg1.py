# Test case 1:
# Input:
# R1 = n: 2 p: 3 -> arti dari berikut ini adalah nilai input n dan p masing-masing untuk R1, sehingga n**p = 2**3 = 8
# R2 = n: 4 p: 3 -> arti dari berikut ini adalah nilai input n dan p masing-masing untuk R2, sehingga n**p = 4**3 = 64, begitu seterusnya
# T2 = n: 3 p: 2
#Output: T1square = 1.125

# Test case 2:
# Input:
# R1 = n: "Ups" p: 3
# R2 = n: 4 p: "Wow"
# T2 = n: "Ups" p: "Wow"
#Output: ERROR

# Test case 3:
# Input:
# R1 = n: 3 p: 3
# R2 = n: 3 p: 0
# T2 = n: 0 p: 0
#Output: T1square = 27

bil = {
    "R1": {
        "n": 'Ups',
        "p": 3
    },
    "R2": {
        "n": 4,
        "p": "wow"
    },
    "T2": {
        "n": 'ops',
        "p": 'wow'
    }
}
'''
def showinput():
    try:
      for i in bil:
        print(i," | Input Number Only")
        bil[i]["n"] = int(input("   n: "))
        bil[i]["p"] = int(input("   p: "))
    except:
      print('An exception occurred | Number Only')
''' 

def power(n, p):
    
    def inner_power(n, p):
        # Disini isikan error handling jika user memasukkan inputan selain angka
        
        if not isinstance(n,int) or not isinstance(p,int):
            print("Inputan Bukan Angka")
            exit()
        # Masukkan kalkulasi perpangkatan disini
        if p == 0:
            return 1
        if p >= 1:
            return n * inner_power(n, p-1)
    return inner_power(n, p)


def kepler():
    # Disini masukkan perhitungan T1 kuadrat sesuai dengan rumus hukum 3 kepler diatas.
    #T1square = power(2,3)*(power(3,2)/power(4,3))
      T1square = power(bil["R1"]["n"], bil["R1"]["p"])*(power(bil["T2"]["n"], bil["T2"]["p"])/power(bil["R2"]["n"], bil["R2"]["p"]))
      return T1square
    
#showinput()
print(kepler())




