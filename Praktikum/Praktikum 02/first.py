# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = json_parser_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Type, cast, Callable


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


@dataclass
class StokBarangData:
    nama_barang: str
    jumlah_barang: int

    @staticmethod
    def from_dict(obj: Any) -> 'StokBarangData':
        assert isinstance(obj, dict)
        nama_barang = from_str(obj.get("nama_barang"))
        jumlah_barang = from_int(obj.get("jumlah_barang"))
        return StokBarangData(nama_barang, jumlah_barang)

    def to_dict(self) -> dict:
        result: dict = {}
        result["nama_barang"] = from_str(self.nama_barang)
        result["jumlah_barang"] = from_int(self.jumlah_barang)
        return result


@dataclass
class Barang:
    id: int
    data: StokBarangData

    @staticmethod
    def from_dict(obj: Any) -> 'Barang':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        data = StokBarangData.from_dict(obj.get("data"))
        return Barang(id, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["data"] = to_class(StokBarangData, self.data)
        return result


@dataclass
class UserdatumData:
    role_id: int
    role_status: str
    nama: str
    username: str
    password: str
    barang: Optional[List[Barang]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserdatumData':
        assert isinstance(obj, dict)
        role_id = from_int(obj.get("role_id"))
        role_status = from_str(obj.get("role_status"))
        nama = from_str(obj.get("nama"))
        username = from_str(obj.get("username"))
        password = from_str(obj.get("password"))
        barang = from_union([lambda x: from_list(Barang.from_dict, x), from_none], obj.get("barang"))
        return UserdatumData(role_id, role_status, nama, username, password, barang)

    def to_dict(self) -> dict:
        result: dict = {}
        result["role_id"] = from_int(self.role_id)
        result["role_status"] = from_str(self.role_status)
        result["nama"] = from_str(self.nama)
        result["username"] = from_str(self.username)
        result["password"] = from_str(self.password)
        result["barang"] = from_union([lambda x: from_list(lambda x: to_class(Barang, x), x), from_none], self.barang)
        return result


@dataclass
class Userdatum:
    id: int
    data: UserdatumData

    @staticmethod
    def from_dict(obj: Any) -> 'Userdatum':
        assert isinstance(obj, dict)
        id = from_int(obj.get("id"))
        data = UserdatumData.from_dict(obj.get("data"))
        return Userdatum(id, data)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_int(self.id)
        result["data"] = to_class(UserdatumData, self.data)
        return result


@dataclass
class JSONParser:
    userdata: List[Userdatum]
    stok_barang: List[Barang]

    @staticmethod
    def from_dict(obj: Any) -> 'JSONParser':
        assert isinstance(obj, dict)
        userdata = from_list(Userdatum.from_dict, obj.get("userdata"))
        stok_barang = from_list(Barang.from_dict, obj.get("stok_barang"))
        return JSONParser(userdata, stok_barang)

    def to_dict(self) -> dict:
        result: dict = {}
        result["userdata"] = from_list(lambda x: to_class(Userdatum, x), self.userdata)
        result["stok_barang"] = from_list(lambda x: to_class(Barang, x), self.stok_barang)
        return result


def json_parser_from_dict(s: Any) -> JSONParser:
    return JSONParser.from_dict(s)


def json_parser_to_dict(x: JSONParser) -> Any:
    return to_class(JSONParser, x)




######################################################################

import json

#file_data = open("C:/Users/PC/Documents/Praktikum Pemrograman Fungsional/Praktikum 02/data.json").read()
#user_data = json.loads(file_data)
##datajson = json_parser_from_dict(json.loads(file_data))

id_user_login = int
role_user_login = int
index_user_login = int


def readdatajson():
    path = "C:/Users/PC/Documents/Praktikum Pemrograman Fungsional/Praktikum 02/data.json"
    return json_parser_from_dict(json.loads(open(path).read()))

def writedatajson(data):
    path = "C:/Users/PC/Documents/Praktikum Pemrograman Fungsional/Praktikum 02/data.json"
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

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
    if getlogin(username, password, readdatajson().userdata) is True:
        menulogin()
    else:
        print('!!!! Username / Password Salah !!!')
        login()

def simpanlogindetails(i, data): ## simpan data login ke variable global
    global id_user_login
    id_user_login = i.id
    global index_user_login
    index_user_login = data.index(i)
    global role_user_login
    role_user_login = i.data.role_id
    #print(id_user_login)
    #print(index_user_login)


def getlogin(username, password, data): ## cek login detail dalam array
    for i in data:
        if i.data.username == username:
            if i.data.password == password:
                simpanlogindetails(i,data)
                return True
    return False



def menulogin():
    print("======== Selamat Datang Di ==========")
    print("========== Toko Kelontong ==========")
    print("======== Silahkan Pilih Menu ========")
    print("=====================================")
    if role_user_login == 1: # Penjual
        print(" 1 = Create Barang")
        print(" 2 = Lihat Semua Barang")
        print(" 3 = Update Jumlah Barang")
        print(" 4 = Delete Barang")
    if role_user_login == 2: # Pembeli
        print(" 1 = Beli Barang")
        print(" 2 = Barang Yang Dibeli")




def createBarang():
    print("======== Selamat Datang Di ==========")
    print("========= Toko Kelontong ==========")
    print("========== Create Barang ==========")
    print("=====================================")
    
    for i in readdatajson().stok_barang:
        print("#####################################")
        print("  Id Barang = ", i.id)
        print("  Nama Barang =  ",i.data.nama_barang)
        print("  Jumlah Barang = ",i.data.jumlah_barang)
        print("#####################################")
    
    print('Ketik 1 Input Barang')
    print('Ketik 0 Untuk Kembali')
    try:
        var = input()
    except SyntaxError:
        print('Inputan Salah')
    else:
        
        if var == 0 or var == '0':
            pass
        if var == 1 or var == '1':
            path = "C:/Users/PC/Documents/Praktikum Pemrograman Fungsional/Praktikum 02/data.json"
            data = json_parser_to_dict(json.loads(open(path).write()))


        else:
            print(' Tidak Ada Di List')


def lihatBarang():
    pass

def updateBarang():
    pass

def deleteBarang():
    pass

def beliBarang():
    pass

def barangDibeli():
    pass



def main():
    menutampilan()

if __name__ == "__main__":
    main()