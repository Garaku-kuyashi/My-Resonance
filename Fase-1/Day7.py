class Mahasiswa:
    def __init__(self, nama, nim,):
        self.nama = nama
        self.nim = nim
        self.list_nilai = []

    def tambah_nilai(self, nilai):
        self.list_nilai.append(nilai)

    def hitung_statistik(self):
        if not self.list_nilai:
            return 0, 0, 0
        tertinggi = max(self.list_nilai)
        terendah = min(self.list_nilai)
        rata_rata =  sum(self.list_nilai) / len(self.list_nilai)
        return tertinggi, terendah, rata_rata
    
    def status_kelulusan(self):
        _, _, rata_rata = self.hitung_statistik()
        if rata_rata >= 80:
            return "Cumlaude"
        elif rata_rata >= 70:
            return "Lulus"
        else:
            return "Tidak Lulus"
        
def tampilkan_laporan(mahasiswa):
    tertinggi, terendah, rata_rata = mahasiswa.hitung_statistik()
    print(f"Nama : {mahasiswa.nama}")
    print(f"NIm : {mahasiswa.nim}")
    print(f"Nilai : {mahasiswa.list_nilai}")
    print(f"Tertinggi : {tertinggi}")
    print(f"Terendah : {terendah}")
    print(f"Rata-rata : {rata_rata:.2f}")
    print(f"Status : {mahasiswa.status_kelulusan()}")
    print("========================================")

mhs1 = Mahasiswa("Chisa", 2409106089)
mhs1.tambah_nilai(90)
mhs1.tambah_nilai(100)
mhs1.tambah_nilai(97)

mhs2 = Mahasiswa("Mafuyu", 240915678)
mhs2.tambah_nilai(98)
mhs2.tambah_nilai(85)
mhs2.tambah_nilai(80)

mhs3 = Mahasiswa("Miku", 23465829898)
mhs3.tambah_nilai(40)
mhs3.tambah_nilai(82)
mhs3.tambah_nilai(78)

daftar_list = [mhs1, mhs2, mhs3]

print("========================================")
print("LAPORAN MAHASISWA.")
print("========================================")
for mhs in daftar_list:
    tampilkan_laporan(mhs)


