
######
## 3

def cToF(c):
    return (c * 9/5) + 32

def cToK(c):
    return c + 273.15

def cToR(c):
    return (9/5)*c

def fToC(f):
    return (f - 32) * 5/9 
def kToC(k):
    return k - 273,15

### Fahrenheit to ? 
def fahrenheittocelcius(func):
    def inner():
        arr = func()
        data = list(map(fToC,arr))
        return data
    print("Fahrenheit To Celcius : ",inner())
    return inner
def kelvinttocelcius(func):
    def inner():
        arr = func()
        data = list(map(kToC,arr))
        return data
    print("Kelvin To Celcius : ",inner())
    return inner

### Celcius to ?
def celciustofahrenheit(func):
    def inner():
        arr = func()
        data = list(map(cToF,arr))
        return data
    print("Celcius To Fahrenheit : ",inner())
    return inner

def celciustokelvin(func):
    def inner():
        arr = func()
        data = list(map(cToK,arr))
        return data
    print("Celcius To Kelvin : ",inner())
    return inner


def celciustoreamur(func):
    def inner():
        arr = func()
        data = list(map(cToR,arr))
        return data
    print("Celcius To Reamur : ",inner())
    return inner

@fahrenheittocelcius
@celciustofahrenheit
def arraydata():
    arrd = [23,24,24,55,22,88,11,55,33,1,31,20]
    return arrd
@kelvinttocelcius
@celciustokelvin
def arraydata2():
    arrd = [23,24,24,55,22,88,11,55,33,1,31,20]
    return arrd
@celciustoreamur
def arraydata3():
    arrd = [23,24,24,55,22,88,11,55,33,1,31,20]
    return arrd
