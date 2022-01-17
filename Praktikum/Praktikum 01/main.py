
datakendaraan = ["Kijang", "Inova", "Toyota", "Yaris", "Pickep"]
userdata = [
    {
        "username": "admin",
        "password": "admin",
        "data": []
    },
    {
        "username": "budi",
        "password": "budi",
        "data": ["revo"]
    },
]
userditemukan = False
useryanglogin = ''
userloginindex = 999  # Dummy Value


def menutampilan():
    print("======== Penyewaaan Kendaraan ========")
    print('1 = Login')
    print('Pilih Menu : ')
    menu = input()
    if menu == 1 or menu == '1':
        login()
    else:
        print('!!!!! Pilihan Tidak Tersedia !!!!!!')
        menutampilan()


def login():
    print('Masukkan Username: ')
    username = input()
    print('Masukkan Password: ')
    password = input()
    global userditemukan
    userditemukan = getlogin(username, password)
    print('User is Logedin', userditemukan)
    if userditemukan is False:
        print('!!!! Username / Password Salah !!!')
        login()
    else:
        global useryanglogin
        useryanglogin = username
        menulogin(username)


def getlogin(username, password):
    for i in userdata:
        if i["username"] == username:
            print('username adalah ' + i["username"])
            if i["password"] == password:
                print('password adalah ' + i["password"])
                global userloginindex
                userloginindex = userdata.index(i)
                return True
    return False

def menu_input_kendaraan():
    print("============= Masukkan Kendaraan =============")
    print('==Kendaraan Sekarang==')
    for a in datakendaraan:
        print(a, '\n')
    print('==Kendaraan Sekarang==')
    print('Masukkan Kendaraan: ')
    print('Ketik 0 Untuk Kembali')
    try:
        var = input()
    except EOFError:
        print('Inputan Salah')
        menu_input_kendaraan()
    else:
        if var == 0 or var == '0':
            menulogin(useryanglogin)
        
        datakendaraan.append(var)
        menu_input_kendaraan()


def menu_sewa_kendaraan():
    print("============= Menu Sewa Kendaraan =============")
    print('== Kendaraan Ynag Ada ==')
    for a in datakendaraan:
        print(a, '\n')
    print('== Kendaraan Ynag Ada ==')
    print('Masukkan Kendaraan Yang Ingin Disewa: ')
    print('Ketik 0 Untuk Kembali')
    try:
        var = input()
    except SyntaxError:
        print('Inputan Salah')
    else:
        if var == 0 or var == '0':
            menulogin(useryanglogin)
        if var in datakendaraan:
            userdata[userloginindex]["data"].append(var)

            valindex = datakendaraan.index(var)
            datakendaraan.pop(valindex)
            menu_sewa_kendaraan()
        else:
            print('Kendaraan Tidak Ada Di List')
            menu_sewa_kendaraan()


def menu_pengembalian_kendaraan():
    print("============= Menu Pengembalian Kendaraan =============")
    print('== Kendaraan Ynag Di Sewa ==')
    for a in userdata[userloginindex]["data"]:
        print(a, '\n')
    print('== Kendaraan Ynag Disewa ==')
    print('Masukkan Kendaraan Yang Ingin Dikembalikan: ')
    print('Ketik 0 Untuk Kembali')
    try:
        var = input()
    except SyntaxError:
        print('Inputan Salah')

    else:
        if var == 0 or var == '0':
            menulogin(useryanglogin)
        if var in userdata[userloginindex]["data"]:
            #print(var)
            datakendaraan.append(var)
            valindex = userdata[userloginindex]["data"].index(var)
            userdata[userloginindex]["data"].pop(valindex)
            menu_pengembalian_kendaraan()
        else:
            print('Kendaraan Tidak Ada Di List')
            menu_pengembalian_kendaraan()


def menulogin(user):
    print("============= Penyewaaan Kendaraan ============")
    print('=== Selamat Datang', useryanglogin, '====')
    print('== Kendaraan Yang Dipinjam ==')
    for a in userdata[userloginindex]["data"]:
        print(a, '\n')
    print('== Kendaraan Yang Dipinjam ==')
    print('1 = Sewa Kendaraan')
    print('2 = Pengembalian Kendaraan')
    if user == 'admin':
        print('3 = Input Kendaraan')
    print('0 = Log out')
    print('Pilih Menu :')
    menu = input()
    if menu == 1 or menu == '1':
        menu_sewa_kendaraan()
    elif menu == 2 or menu == '2':
        menu_pengembalian_kendaraan()
    elif (menu == 3 or menu == '3') and user == 'admin':
        menu_input_kendaraan()
    elif menu == 0 or menu == '0':
        logout()
    else:
        print('!!!!! Pilihan Tidak Tersedia !!!!!!')
        menulogin(user)

def logout():
  
  print(userditemukan)
  print(useryanglogin)
  print(userloginindex)
  login()

menutampilan()
