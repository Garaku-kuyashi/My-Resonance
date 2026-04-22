# variabel dan tipe data
# nama = "chisa"  # string
# umur = 19 # int
# ipk = 3.9 # float
# mahasiswa = True # boolean

# print(f"nama kamu adalah: {nama} untuk umur kamu adalah: {umur} ipk kamu adalah: {ipk} dan kamu adalah mahasiswa: {mahasiswa}")

# input dan output
# namaKamu = input("siapa kamu: ")
# print(namaKamu)

# perkondisian
# if else
# nilai = int(input("berapa nilai kamu: "))
# print(nilai)

# if nilai > 70:
#     print("kamu dapat A")
# elif nilai > 60:
#     print("kamu dapat B")
# else:
#     print("kamu dapat c")

# operasi dasar
# matematika
# print (3+8) # [penjumlahan]
# print (8-3) # [pengurangan]
# print (3*8) # [perkalian]
# print (10/2) # [pembagian][hasil jadi float]
# print (10//2) # [modulus]
# print (3**8) # [pangkat]

# perbandingan [hasilnya true/flase]
# print(12>8) # true
# print(12==8) # false
# print(12 != 8) # true

# ========================================================================================================

# latihan 1
nama = input("masukkan nama kamu: ")
print(nama)
umur = int(input("masukkan umur kamu: "))

if umur < 17:
    print("kamu belum dewasa")
elif umur >= 17 and umur <= 25:
    print("kamu usia mahasiswa")
else:
    print("kamu sudah dewasa")

# latihan 2
a = int(input("masukkan nilai 1: "))
operator = input("masukkan oprator = +,-,*,/: ")
b = int(input("masukkan nilai 2: "))


if operator == "+":
    print(a+b)
elif operator == "-":
    print(a-b)
elif operator == "*":
    print(a*b)
elif operator == "/":
    print(a/b)
else:
    print("masukkan yang benar")





    