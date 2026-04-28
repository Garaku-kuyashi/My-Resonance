# function
# function adalah kode yang bisa dipanggil berkali-kali tanpa harus menulis ulang kode

# def sapa():
#     print("halo, semua")

# sapa()
# sapa()

# # function dengan parameter
# # parameter itu data yang kamu kirim ke dalam function

# def sapa(nama):
#     print("halo, ", nama)

# sapa("chisa")

# def perkenalan(iniial, umur):
#     print(f"Nama saya {iniial}, dan umur saya adalah {umur}")

# perkenalan("chisa", 19)

# # function dengan return
# # function bisa mengembalikan nilai untuk dipakai di luar

# def tambah(a, b):
#     return a+b

# hasil = tambah(5, 4)
# print("hasil: ", hasil)  

# # default parameter 
# # parameter bisa mempunyai nilai default kalau tidak diisi

# def sapaan(siapa, salam="halo"):
#     print(salam + ",", siapa)

# sapaan("chisa")
# sapaan("chisa", "hai")

# ==========================================================================

# latihan 1
def hitung_nilai(list_nilai):
    nilai_max = max(list_nilai)
    nilai_min= min(list_nilai)
    nilai_rata = sum(list_nilai) / len(list_nilai)
    return nilai_max, nilai_min, nilai_rata

data_nilai = [100, 89, 45, 23, 90]
hasil1 = hitung_nilai(data_nilai)
print("hasil adalah: ", hasil1)


# latihan 2
def cek_genap_ganjil(angka):
    if angka % 2 == 0:
        return "genap"
    else:
        return "ganjil"
    
list_angka = [1, 2, 3, 4, 6, 8, 10, 20]

for i in list_angka:
    hasil = cek_genap_ganjil(i)
    print(i, "adalah: ", hasil)

