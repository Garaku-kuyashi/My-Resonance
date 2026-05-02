# soal 1
# belanja = [
#     ("Apel", 5000, 3),
#     ("Susu", 15000, 2),
#     ("Roti", 12000, 1),
#     ("Telur", 25000, 2),
#     ("Mie", 3000, 5)
# ]

# total = 0

# print(f"{'Nama':<10} | {'Harga':<8} | {'Jumlah':<3} | {'Subtotal'}")

# for nama, harga, jumlah, in belanja:
#     subtotal = harga*jumlah
#     total += subtotal
#     print(f"{nama:<10} | {harga:<8} | {jumlah:<6} | {subtotal:>8}")

# print("")
# print(f"Total Dari Semua Belanja Adalah: Rp {total}")

# ==============================================================
# soal 2
data = {
    "Chisa": [90, 85, 92, 88],
    "Mafuyu": [78, 82, 75, 80],
    "Miku": [65, 70, 68, 72],
    "Hoshino": [95, 98, 92, 97],
    "Shiroko": [55, 60, 58, 62]
}

rata_rata_mhs= {}

for nama, daftar_nilai in data.items():
    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    rata_rata_mhs[nama] = rata_rata
    print(f"{nama:<10}: {rata_rata:2f}")

nama_tinggi = max(rata_rata_mhs, key=rata_rata_mhs.get)
nama_rendah = min(rata_rata_mhs, key=rata_rata_mhs.get)


print(f"Rata-rata Tertinggi: {nama_tinggi} ({rata_rata_mhs[nama_tinggi]:.2f})")
print(f"Rata-rata Terendah: {nama_rendah} ({rata_rata_mhs[nama_rendah]:.2f})")