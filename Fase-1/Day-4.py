# Dictionary
# dictionary menyimpan data dalam bentuk key:value-- seperti kamus, yang dimana kamu cari data berdasarkan kata kunci

# mahasiswa = {
#     "nama": "chisa",
#     "nim": 24091096089,
#     "kelas": "B24"
# }

# print(mahasiswa["nama"])
# print(mahasiswa["nim"])

# # operasi pada dictionary
# mahasiswa["ipk"] = 3.9  #tambah data 
# mahasiswa["kelas"] = "rebbel"  #ubah data
# del mahasiswa["nim"]  #hapus data

# print(mahasiswa.keys())  #print semua key
# print(mahasiswa.values())  #print semua value
# print(mahasiswa.items())  #print semua pasangan key:value


# # loopiung di dictionary
# for key, value in mahasiswa.items():
#     print(key, ":", value)


# # set
# # set itu seperti list, tapi tidak ada duplikat dan tidak berurutan
# hobi = {"gaming", "musik", "gaming", "coding"}
# print(hobi) #gaming hanya akan tercetak sekali 

# # kegunaan paling umum -- hapus duplikat dari list
# nilai = [80, 90, 80, 20, 70, 20]
# unik = set(nilai)
# print(unik)

# # operasi dasar pada list
# a = {1, 2, 3, 4}
# b = {2, 3, 4, 5, 6}

# print(a|b)  #gabungan -> 1, 2, 3, 4 , 5, 6
# print(a & b)  # irisan -> 2, 3, 4
# print(a - b)  #selisih -> 1

# ============================================================================
# latiah 1
biodata_diri = {
    "Nama" : "Chisa",
    "Umur" : 19,
    "Jurusan" : "Informatika",
    "Hobi" : "Mendengar Musik"
}

print("Sebelum Update")
for key, value in biodata_diri.items():
    print(key, ":", value)

biodata_diri["kota"] = "Startoch Academy"

print("")
print("Sebelum Update")
for key, value in biodata_diri.items():
    print(key, ":", value)

# latihan 2
nilai = [85, 90, 85, 78, 90, 92, 78, 85, 100]

unik = set(nilai)
print("Hapus duplikat: ", unik)
print("Berapa banyak niali dalam unik: ", len(unik))

konversi = list(unik)
print("Unik setelah konversi: ", konversi)

pengurutan = sorted(konversi)
print("Pengurutan nilai: ", pengurutan)