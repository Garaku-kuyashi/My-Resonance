# list dan tuple
# list

# buah = ["apel", "mangga", "jeruk"]

# print(buah[0])
# print(buah[1])
# print(buah[2])

# # operasi tambahan pada list
# buah.append("langsat")  #tambah data pada list
# buah.insert(1, "pisang") #tambah pada index tertentu
# buah.remove("apel") #hapus data pada list buah
# buah.pop(0) #hapus berdasarkan index
# print(len(buah)) #jumlah item dalam list
# print(buah)


# # loop pada list
# for item in buah:
#     print(item)

# tuple
# smaa seperti list tapi tidak bisa diubah setelah dibuat

# koordinat = (10, 20)
# print(koordinat[0])
# print(koordinat[1])


# list + loop
# nilai = [85, 90, 78, 92, 88]

# total = 0
# for n in nilai:
#     total += n

# rata = total / len(nilai)

# print("rata-rata: ", rata)

# =================================================================================
# latihan 1
nama_teman = ["chisa", "shiroko", "frostnova", "mafuyu", "galbrena"]

for i in nama_teman:
    print(i)

print("")
print("nama ketika diubah")
nama_teman.pop(0)
print(nama_teman)


# latihan 2
nilai_ujian = [90, 89, 23, 45, 100]
print(max(nilai_ujian))
print(min(nilai_ujian))
print(sum(nilai_ujian) / len(nilai_ujian))
