# oop
# oop adalah cara mengorganisir kode dengan membuat blueprint (class) yang bisa di cetak jadi banyak object
# analogi = class itu seperti cetakn kue, objek itu kuenya. dari satu cetakan bisa bikin banyak kue dengan isi berbeda

# ==================================================================================
# class dan object
# class Mahasiswa:
#     def __init__(self, nama, umur, jurusan):
#         self.nama = nama
#         self.umur = umur
#         self.jurusan = jurusan

#     def perkenalan(self):
#         print(f"halo, saya {self.nama}, umur saya adalah {self.umur}, dan saya dari jurusan {self.jurusan}")

# mhs1 = Mahasiswa("chisa", 19, "rebbel")

# mhs1.perkenalan()

# penjelasan
# class -> keyword untuk membuat blueprint
# __init__  -> method yang ototmatis jalan saat objek dibuat
# self -> merujuk ke objek itu sendiri
# self.nama -> menyimpan data ke dalam objek

# =================================================
# mengakses dan mengubaj atribut

# print("")
# print(mhs1.nama)
# mhs1.umur = 20
# print(mhs1.umur)

# =================================================
# method
# method itu function yang ada di dalam class

# class Laptop:
#     def __init__(self, merk, harga):
#         self.merk = merk
#         self.harga = harga

#     def status_barang(self):
#         if self.harga <= 5000:
#             return "murah"
#         elif self.harga >= 6000:
#             return "mahal"
#         else:
#             return "tidak ada"
        

# lap1 = Laptop("acer", 9000)
# print(lap1.merk, ":", lap1.status_barang())

# ===================================================================================
# latihan 1
class Buku:
    def __init__(self, judul, penulis, harga):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga

    def info(self):
        print("===============================")
        print(f"JUDUL: {self.judul}")
        print(f"PENULIS: {self.penulis}")
        print(f"HARGA: RP {self.harga}")
        print("===============================")

    def diskon(self, persen):
        potongan = self.harga * (persen/100)
        harga_baru = self.harga - potongan
        print(f"Disko {persen}% -> HARGA BARU: RP {harga_baru}")

buku1 = Buku("Narnia", "C.S LEWIS", 100000)
buku2 = Buku("Boochi The Rock", "Aki Hamazi", 60000)

print("info buku")
buku1.info()
print("")
buku2.info()

print("")
print("harga diskon")
buku1.diskon(20)
print("")
buku2.diskon(20)

# latihan 2
class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo

    def setor(self, jumlah):
        self.saldo += jumlah
        print(f"setor RP{jumlah:,} -> saldo: RP{self.saldo}")

    def tarik(self, jumlah):
        if jumlah <= self.saldo:
            self.saldo -= jumlah
            print(f"tarik: {jumlah:,} -> saldo: RP{ self.saldo}")
        else:
            print(f"saldo tidak cukup, saldo anda: RP {self.saldo}")

    def cek_saldo(self):
        print(f"atas nama: {self.nama}, dengan saldo: RP {self.saldo}")

rek = RekeningBank("Chisa", 400000)
rek.setor(1000)
rek.tarik(39000)
rek.cek_saldo()