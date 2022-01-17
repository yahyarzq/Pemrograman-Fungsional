
import json

#file_data = open("C:/Users/PC/Documents/Praktikum Pemrograman Fungsional/Praktikum 02/data.json").read()
#user_data = json.loads(file_data)
##datajson = json_parser_from_dict(json.loads(file_data))

id_user_login = int
role_user_login = int
index_user_login = int

fileutama = '{"userdata":[{"id":1,"data":{"role_id":1,"role_status":"Penjual","nama":"Budi","username":"admin","password":"admin"}},{"id":2,"data":{"role_id":1,"role_status":"Penjual","nama":"Denis","username":"denis","password":"denis"}},{"id":3,"data":{"role_id":2,"role_status":"Pembeli","nama":"Sopo","username":"sopo","password":"sopo","barang":[{"id":10,"data":{"nama_barang":"Helm","jumlah_barang":3}},{"id":1,"data":{"nama_barang":"Oreo","jumlah_barang":2}},{"id":1,"data":{"nama_barang":"Oreo","jumlah_barang":1}}]}}],"stok_barang":[{"id":1,"data":{"nama_barang":"Oreo","jumlah_barang":91}},{"id":2,"data":{"nama_barang":"Minyak Goreng","jumlah_barang":99}},{"id":3,"data":{"nama_barang":"Tepung Terigu","jumlah_barang":100}}]}'

def readdatajson():
    path = "data.json"
    return json.load(open(path))


def writedatajson(data):
    path = "data.json"
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

#"role_status": "Penjual",
#"nama": "Budi",
#"username": "admin",
#"password": "admin"
#############################
#"role_status": "Pembeli",
#"nama": "Sopo",
#"username": "sopo",
#"password": "sopo",

def menutampilan():
    print("======== Selamat Datang Di ==========")
    print("========== Toko Kelontong ==========")
    print("======== Silahkan Pilih Menu ========")
    print('1 = Login')
    print('Pilih Menu : ')
    menu = input()
    if menu == 1 or menu == '1':
        login()
    else:
        print('!!!!! Pilihan Tidak Tersedia !!!!!!')
        menutampilan()


def login():
    print("=========== Toko Kelontong ==========")
    print("============= Menu Login ============")
    print('Masukkan Username: ')
    username = input()
    print('Masukkan Password: ')
    password = input()
    if getlogin(username, password, readdatajson()["userdata"]) is True:
        menulogin()
    else:
        print('!!!! Username / Password Salah !!!')
        login()


def simpanlogindetails(i, data):  # simpan data login ke variable global
    global id_user_login
    id_user_login = i["id"]
    global index_user_login
    index_user_login = data.index(i)
    global role_user_login
    role_user_login = i["data"]["role_id"]
    # print(id_user_login)
    # print(index_user_login)


def getlogin(username, password, data):  # cek login detail dalam array
    for i in data:
        if i["data"]["username"] == username:
            if i["data"]["password"] == password:
                simpanlogindetails(i, data)
                return True
    return False


def menulogin():
    print("======== Selamat Datang Di ==========")
    print("========== Toko Kelontong ==========")
    print("============= ", id_user_login, " =============")
    print("======== Silahkan Pilih Menu ========")
    print("=====================================")
    if role_user_login == 1:  # Penjual
        print(" 1 = Create Barang")
        print(" 2 = Lihat Semua Barang")
        print(" 3 = Update Jumlah Barang")
        print(" 4 = Delete Barang")
    if role_user_login == 2:  # Pembeli
        print(" 1 = Beli Barang")
        print(" 2 = Barang Yang Dibeli")
    print(" 0 = Logout")
    print('Pilih Menu :')
    menu = input()
    if (menu == 1 or menu == '1') and role_user_login == 1:
        createBarang()
    elif (menu == 2 or menu == '2') and role_user_login == 1:
        lihatBarang()
    elif (menu == 3 or menu == '3') and role_user_login == 1:
        updateBarang()
    elif (menu == 4 or menu == '4') and role_user_login == 1:
        deleteBarang()
    elif (menu == 1 or menu == '1') and role_user_login == 2:
        beliBarang()
    elif (menu == 2 or menu == '2') and role_user_login == 2:
        barangDibeli()
    elif menu == 0 or menu == '0':
        logout()
    else:
        print('!!!!! Pilihan Tidak Tersedia !!!!!!')
        menulogin()


def createBarang():
    print("======== Selamat Datang Di ==========")
    print("========= Toko Kelontong ==========")
    print("========== Create Barang ==========")
    print("=====================================")

    for i in readdatajson()["stok_barang"]:
        print("#####################################")
        print("  Id Barang = ", i['id'])
        print("  Nama Barang =  ", i["data"]["nama_barang"])
        print("  Jumlah Barang = ", i["data"]["jumlah_barang"])
        print("#####################################")

    print('Ketik 1 Input Barang')
    print('Ketik 0 Untuk Kembali')
    try:
        var = input()
    except SyntaxError:
        print('Inputan Salah')
    else:
        if var == 0 or var == '0':
            menulogin()
        else:
            print("Masukkan Id Barang")
            input3 = input()
            print("Masukkan Nama Barang")
            input1 = input()
            print("Masukkan Jumlah Barang")
            input2 = input()
            data = readdatajson()
            total_barang = data["stok_barang"]
            data["stok_barang"].append(
                {
                    "id": int(input3),
                    "data": {
                        "nama_barang": str(input1),
                        "jumlah_barang": int(input2)
                    }
                }
            )
            writedatajson(data)
            createBarang()


def lihatBarang():
    print("======== Selamat Datang Di ==========")
    print("========= Toko Kelontong ==========")
    print("========== Lihat Barang ==========")
    print("=====================================")

    for i in readdatajson()["stok_barang"]:
        print("#####################################")
        print("  Id Barang = ", i['id'])
        print("  Nama Barang =  ", i["data"]["nama_barang"])
        print("  Jumlah Barang = ", i["data"]["jumlah_barang"])
        print("#####################################")

    print('Ketik 0 Untuk Kembali')
    try:
        var = input()
    except SyntaxError:
        print('Inputan Salah')
    else:
        if var == 0 or var == '0':
            menulogin()
        else:
            print('Input Salah')


def updateBarang():
    print("======== Selamat Datang Di ==========")
    print("========= Toko Kelontong ==========")
    print("========== Update Barang ==========")
    print("=====================================")

    for i in readdatajson()["stok_barang"]:
        print("#####################################")
        print("  Id Barang = ", i['id'])
        print("  Nama Barang =  ", i["data"]["nama_barang"])
        print("  Jumlah Barang = ", i["data"]["jumlah_barang"])
        print("#####################################")

    print('Ketik 1 Update Barang')
    print('Ketik 0 Untuk Kembali')
    try:
        var = input()
    except SyntaxError:
        print('Inputan Salah')
    else:
        if var == 0 or var == '0':
            menulogin()
        else:
            print("Masukkan Id Barang")
            var1 = input()
            data = readdatajson()
            for i in range(len(data["stok_barang"])):
                if data["stok_barang"][i]["id"] == int(var1):
                    print("Ditemukan, Nama Barang :",
                          data["stok_barang"][i]["data"]["nama_barang"])
                    print("Update Jumlah Barang")
                    var2 = input()
                    data["stok_barang"][i]["data"]["jumlah_barang"] = int(var2)
                    writedatajson(data)
                    updateBarang()
            else:
                print("====Barang Tidak Ada====")
                updateBarang()


def deleteBarang():
    print("======== Selamat Datang Di ==========")
    print("========= Toko Kelontong ==========")
    print("========== Delete Barang ==========")
    print("=====================================")

    for i in readdatajson()["stok_barang"]:
        print("#####################################")
        print("  Id Barang = ", i['id'])
        print("  Nama Barang =  ", i["data"]["nama_barang"])
        print("  Jumlah Barang = ", i["data"]["jumlah_barang"])
        print("#####################################")

    print('Ketik 1 Delete Barang')
    print('Ketik 0 Untuk Kembali')
    try:
        var = input()
    except SyntaxError:
        print('Inputan Salah')
    else:
        if var == 0 or var == '0':
            menulogin()
        else:
            print("Masukkan Id Barang")
            var1 = input()
            data = readdatajson()
            for i in range(len(data["stok_barang"])):
                if data["stok_barang"][i]["id"] == int(var1):
                    print("Ditemukan, Nama Barang :",
                          data["stok_barang"][i]["data"]["nama_barang"], "Berhasil Dihapus")
                    data["stok_barang"].pop(i)
                    writedatajson(data)
                    deleteBarang()
            else:
                print("====Barang Tidak Ada====")
                deleteBarang()


def beliBarang():
    print("======== Selamat Datang Di ==========")
    print("========= Toko Kelontong ===========")
    print("========== Beli Barang =============")
    print("=====================================")

    for i in readdatajson()["stok_barang"]:
        print("#####################################")
        print("  Id Barang = ", i['id'])
        print("  Nama Barang =  ", i["data"]["nama_barang"])
        print("  Jumlah Barang = ", i["data"]["jumlah_barang"])
        print("#####################################")

    print('Ketik 1 Beli Barang')
    print('Ketik 0 Untuk Kembali')
    try:
        var = input()
    except SyntaxError:
        print('Inputan Salah')
    else:
        if var == 0 or var == '0':
            menulogin()
        else:
            print("Masukkan Id Barang")
            var1 = input()
            data = readdatajson()
            for i in range(len(data["stok_barang"])):
                if data["stok_barang"][i]["id"] == int(var1):
                    print("Nama Barang :", data["stok_barang"]
                          [i]["data"]["nama_barang"], "Telah Dibeli")
                    data["stok_barang"][i]["data"]["jumlah_barang"] = data["stok_barang"][i]["data"]["jumlah_barang"] - 1
                    # print(data["userdata"][index_user_login]["data"]["barang"])
                    if len(data["userdata"][index_user_login]["data"]["barang"]) == 0:
                        data["userdata"][index_user_login]["data"]["barang"].append({
                                "id": data["stok_barang"][i]["id"],
                                "data": {
                                    "nama_barang": data["stok_barang"][i]["data"]["nama_barang"],
                                    "jumlah_barang": 1
                                }
                            })
                    else:
                        for y in range(len(data["userdata"][index_user_login]["data"]["barang"])):
                            if data["userdata"][index_user_login]["data"]["barang"][y]["id"] == int(var1):
                                data["userdata"][index_user_login]["data"]["barang"][y]["data"]["jumlah_barang"] += 1
                            if data["userdata"][index_user_login]["data"]["barang"][y]["id"] != int(var1):
                                data["userdata"][index_user_login]["data"]["barang"].append({
                                    "id": data["stok_barang"][i]["id"],
                                    "data": {
                                        "nama_barang": data["stok_barang"][i]["data"]["nama_barang"],
                                        "jumlah_barang": 1
                                    }
                                })
                            else:
                                pass
                else:
                    pass
            writedatajson(data)
            beliBarang()

def barangDibeli():
    print("======== Selamat Datang Di ==========")
    print("========= Toko Kelontong ==========")
    print("========== Lihat Barang ==========")
    print("=====================================")

    for i in readdatajson()["userdata"][index_user_login]["data"]["barang"]:
        print("#####################################")
        print("  Id Barang = ", i['id'])
        print("  Nama Barang =  ", i["data"]["nama_barang"])
        print("  Jumlah Barang = ", i["data"]["jumlah_barang"])
        print("#####################################")

    print('Ketik 0 Untuk Kembali')
    try:
        var = input()
    except SyntaxError:
        print('Inputan Salah')
    else:
        if var == 0 or var == '0':
            menulogin()
        else:
            print('Input Salah')


def logout():
    global id_user_login
    id_user_login = 0
    global role_user_login
    role_user_login = 0
    global index_user_login
    index_user_login = 0
    menutampilan()

def fileted(data,das):
    return  filter(data, das) 

def increment(data1):
    return lambda data1: data1+1
def main():
    menutampilan()


if __name__ == "__main__":
    main()
