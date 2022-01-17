## NO 1
## A
def penambahan(a,b):
    return a+b
##

## B
arrr = [1,2,3,4,5,6,7]
def multiplyarray(a):
    multiply = lambda a : a * 2
    return list(map(multiply,a))
print(multiplyarray(arrr))
##

## C
def pangkat(n, p):
    def inner_pangkat(n, p):
        if not isinstance(n,int) or not isinstance(p,int):
            print("Inputan Bukan Angka")
            exit()
        else:
            if p == 0:
                return 1
            if p >= 1:
                return n * inner_pangkat(n, p-1)
    return inner_pangkat(n, p)
print(pangkat(2,5))
##

## D
def celciustoFahrenheit(a):
    return (a * 9/5) + 32
print(celciustoFahrenheit(55))

## E
data = [i for i in range(0,30) if i % 3 != 0  ]
print(data)
##





