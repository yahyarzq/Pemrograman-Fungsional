
matrixx = [['x','x','x','x','x'],
           ['x','x','x','x','x'],
           ['x','x','x','x','x'],
           ['x','x','x','x','x'],
           ['x','0','x','x','x']]

def printMatrix(data):
    return list(map(lambda x : print(x),data))

def isBidak(bidak):
    return True if bidak == '0' else False
'''
def findIndexBidak(data):
    list(map(lambda x: map(lambda a: print(a),x), data))
'''
def findIndexBidakLooping(data):
    for i in data:
        for ib in i:
            if isBidak(ib) :
                return [data.index(i),i.index('0')] ## Nilai Kemblian Dalam Bentuk Array. ex [2,4]

def findIndexBidakRecursiveFuction(data):
    def xCoordinat(k):
        if k < len(data):
            def yCoordinat(j):
                if j < len(data[k]) :
                    if isBidak(data[k][j]):
                        global hasil
                        hasil = [data.index(data[k]),data[k].index(data[k][j])]
                    yCoordinat(j+1)
                else:
                    pass
            yCoordinat(0)
            xCoordinat(k+1)
        else:
            pass
    xCoordinat(0)
    return hasil ## Nilai Kemblian Dalam Bentuk Array. ex [2,4]

def moveBidak(x,y,data):
    #bidakCurrentLocation = findIndexBidakLooping(data)
    bidakCurrentLocation = findIndexBidakRecursiveFuction(data)
    a = bidakCurrentLocation[0]
    b = bidakCurrentLocation[1]
    if 0 <= (a+x) < len(data) and 0 <= (b+y) < len(data[0]): # Set Upper And Lower Bound
        global matrixx
        matrixx[a][b] = 'x'
        matrixx[a+x][b+y] ='0'
    else:
        print("============= Ilegal Move ===============")
    
def interFace():
    print("============ Bidak Matrix =============")
    printMatrix(matrixx)
    
    print('Ketik 1 Cek Posisi')
    print('Ketik 2 Geser Kanan')
    print('Ketik 3 Geser Kiri')
    print('Ketik 4 Geser Atas')
    print('Ketik 5 Geser Bawah')
    print('Ketik 6 Geser Timur Laut')
    print('Ketik 7 Geser Tenggara')
    print('Ketik 8 Geser Barat Daya')
    print('Ketik 9 Geser Barat Laut')
    print('Ketik 0 Keluar')
    print('Pilih Menu :')
    menu = input()
    if (menu == 1 or menu == '1'):
        print("Lokasi Bidak",findIndexBidakRecursiveFuction(matrixx))
        interFace()
    elif (menu == 2 or menu == '2') :
        moveBidak(0,1,matrixx)
        interFace()
    elif (menu == 3 or menu == '3') :
         moveBidak(0,-1,matrixx)
         interFace()
    elif (menu == 4 or menu == '4') :
         moveBidak(-1,0,matrixx)
         interFace()
    elif (menu == 5 or menu == '5') :
         moveBidak(1,0,matrixx)
         interFace()
    elif (menu == 6 or menu == '6') :
         moveBidak(-1,1,matrixx)
         interFace()
    elif (menu == 7 or menu == '7') :
         moveBidak(1,1,matrixx)
         interFace()
    elif (menu == 8 or menu == '8') :
         moveBidak(1,-1,matrixx)
         interFace()
    elif (menu == 9 or menu == '9') :
         moveBidak(-1,-1,matrixx)
         interFace()
    elif (menu == 0 or menu == '0') :
        exit()

def main():
    interFace()

if __name__ == "__main__":
    main()