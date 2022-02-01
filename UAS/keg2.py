
def first_decorator(func):
    def inner_decorator():
        books_collection = func()
        for i in books_collection:
            print("\n\nBook Title : {} ".format(i))
        return books_collection
    return inner_decorator



@first_decorator
def Cari():
    books_collection = ["Android Books","Java Books","Python Books"]
    return books_collection

Cari()

perkalian  = 0

def printmultiplicationof10(number):
    def wrapper():
        global perkalian
        perkalian = 10
        resullt = number * perkalian
        print("Hasil Perkalian {} * 10 Adalah {}".format(number,resullt))
    return wrapper()

printmultiplicationof10(10)