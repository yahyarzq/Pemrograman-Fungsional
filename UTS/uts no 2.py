############
# NO 2
## A
def pritn():
    data = [i for i in range(1,33)]
    print(data)
    
##  B
def celciustoFahrenheit(a):
    return (a * 9/5) + 32
def arrayMapMultiplication(a):
    return list(map(celciustoFahrenheit),range(1.50))

## C
def arayyzip():
    return [i+j for i ,j in zip(range(1,10),range(11,20))]

## D
import json
def writedatajson(data):
    path = "/data.json"
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
##  E
gem = map(lambda s : s**3, range(1,30))
##
