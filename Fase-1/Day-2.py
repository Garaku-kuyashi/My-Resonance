# looping
# loop for
# for i in range(1, 6):
#     print(i)

# buah = ["apel", "mangga", "jeruk"]
# for item in buah:
#     print(item)
# print(buah)

# LOOP WHILE
# angka =1 
# while angka <=10:
#     print(angka)
#     angka += 1


# break dan continue
# break -> keluar dari loop
# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# for i in range(6):
#     if i == 3:
#         continue
#     print(i)

# ===================================================
# latihan 1
print("program angka genap")
print("")

for i in range(2, 20, 2):
    print(i)

# latihan 2
angka_rahasia = 8
percobaan =0


print("tebak angka dari 1-10")

while percobaan != angka_rahasia:
    tebakan = int(input("masukkan tebakan: "))
    percobaan += 1
    

    if tebakan > angka_rahasia:
        print("anda salah")
        
    elif tebakan < angka_rahasia:
        print("anda salah")
        
    else:
        print(f"anda benar dan anda menjawab sebanyak")
        print("anda menebak sebanyak ", percobaan, " kali")
        