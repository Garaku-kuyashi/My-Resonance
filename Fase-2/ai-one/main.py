import json


# =========== fase 2 -day 01 ============
history =  []
file_aktif = None
mode = "Browser Pembantu Penjelasan Teori"
NAMA_FILE = "history_chat.json"

def tampilkan_bantuan():
    print(""" Command yang tersedia:
          /help - akan menampilkan bantuan
          /mode - akan mengganti mode assistant
          /history - akan menampilkan history chat
          /clear - akan menghapus semua history chat
          /exit - akan keluar dari program
          /save - akan menyimpan history chat ke file json
          /load - akan memuat history chat dari file json
        """)

def pilih_mode():
    global mode 
    print("Pilih mode assistant:")
    print("1. Tutorial Python")
    print("2. Tutorial c++")
    print("3. Tutorial Matematika Diskrit")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        mode = "Tutorial Python"
    elif pilihan == "2":
        mode = "Tutorial c++"
    elif pilihan == "3":
        mode = "Tutorial Matematika Diskrit"
    else:
        print("Pilihan Tidak Ada")
        return

    print(f"Mode Assistant Sekarang Adalah: {mode}")
    nama_file = ambil_nama_file()
    load_history(nama_file)


def jawaban_dummy(pesan):
    pesan = pesan.lower()
    if mode == "Tutorial Python":
        if "list" in pesan:
            return "List adalah tipe data yang digunakan untuk menyimpan beberapa item dalam satu variabel. List dibuat dengan menggunakan tanda kurung siku [] dan item dipisahkan dengan koma. contoh: my_list = [1, 2, 3, 'empat']"
        elif "loop" in pesan:
            return "Loop adalah struktur kontrol yang digunakan untuk mengulangi blok kode tertentu. Ada dua jenis loop utama dalam Python: for loop dan while loop. For loop digunakan untuk iterasi melalui elemen dalam suatu koleksi, sedangkan while loop digunakan untuk mengulangi blok kode selama kondisi tertentu terpenuhi."
        else:
            return "Maaf saya tidak mengerti pertanyaan anda, Kemungkinan pertanyaan anda diluar topik pembahasan atau belum ada dalam data saya, silahkan bertanya tentang topik yang sudah saya jelaskan"
    elif mode == "Tutorial c++":
        if "pointer" in pesan:
            return "Pointer adalah variabel yang menyimpan alamat memori dari variabel lain. Pointer digunakan untuk mengakses dan memanipulasi data yang disimpan di alamat memori tersebut. Contoh: int* ptr = &var;"
        elif "class" in pesan:
            return "Class adalah blueprint atau template untuk membuat objek dalam pemrograman berorientasi objek. Class mendefinisikan atribut (data) dan metode (fungsi) yang dimiliki oleh objek yang dibuat dari class tersebut. Contoh: class MyClass { public: int myVariable; void myMethod() { } };"
        else:
            return "Maaf saya tidak mengerti pertanyaan anda, Kemungkinan pertanyaan anda diluar topik pembahasan atau belum ada dalam data saya, silahkan bertanya tentang topik yang sudah saya jelaskan"
    elif mode == "Tutorial Matematika Diskrit":
        if "graph" in pesan:
            return "Graph adalah struktur data yang terdiri dari simpul (vertices) dan sisi (edges) yang menghubungkan simpul-simpul tersebut. Graph digunakan untuk merepresentasikan hubungan antara objek-objek dalam berbagai bidang, seperti jaringan komputer, algoritma pencarian, dan teori graf."
        elif "set" in pesan:
            return "Set adalah kumpulan elemen unik yang tidak memiliki urutan tertentu. Set digunakan untuk menyimpan elemen-elemen yang berbeda dan mendukung operasi seperti union, intersection, dan difference. Contoh: A = {1, 2, 3} dan B = {2, 3, 4}."
        else:
            return "Maaf saya tidak mengerti pertanyaan anda, Kemungkinan pertanyaan anda diluar topik pembahasan atau belum ada dalam data saya, silahkan bertanya tentang topik yang sudah saya jelaskan"

# ================= fase 2 -day 02 ============
def simpan_history(nama_file):
    global file_aktif
    try:
        nama_file = nama_file + ".json"
        with open(nama_file, "w", encoding="utf-8") as file:
            json.dump(history, file, ensure_ascii=False, indent=4)
            file_aktif = nama_file
            print(f"HItory berhasil disimpan ke file {nama_file}")
    except Exception as e:
        print(f"Proses gagal: {e}")

def load_history(nama_file):
    global history, file_aktif
    try:
        nama_file = nama_file + ".json"
        with open(nama_file, "r", encoding="utf-8") as file:
            history = json.load(file)
            file_aktif = nama_file
            print(f"History berhasil diload dari file {nama_file}")
    except FileNotFoundError:
        history = []
        file_aktif = nama_file
        print(f"File {nama_file} tidak ditemukan. History dikosongkan.")
    except json.JSONDecodeError:
        print("File json tidak valid.")
    except Exception as e:
        print(f"Proses gagal: {e}")

def ambil_nama_file():
    if mode == "Tutorial Python":
        return "python"
    elif mode == "Tutorial c++":
        return "cpp"
    elif mode == "Tutorial Matematika Diskrit":
        return "matdis"
    

print("=" *40)
print("Selamat datang di AI Assistant!")
print("=" *40)
print("Silahkan ketik /help untuk melihat command yang tersedia")
print(f"Mode Assistant Sekarang Adalah: {mode}")

while True:
    user_input = input("\nKamu: ").strip()

    if not user_input:
        print("Input tidak boleh kosong, silahkan masukkan pertanyaan atau command.")
        continue

    if user_input.lower() == "/exit":
        print("Terima kasih telah menggunakan AI Assistant. Sampai jumpa!")
        break
    elif user_input.lower() == "/help":
        tampilkan_bantuan()
    elif user_input.lower() == "/mode":
        pilih_mode()
    elif user_input.lower() == "/clear":
        history.clear()
        print("History chat telah dihapus.")
    elif user_input.lower() == "/history":
        if not history:
            print("History masih kosong.")
        else:
            print(f"== History Chat ({file_aktif}) ==")
            for chat in history:
                print(f"Kamu: {chat['user']}")
                print(f"AI Assistant: {chat['assistant']}")
                print("-" * 25)
    # ================= fase 2 -day 02 ============
    elif user_input.lower().startswith("/save"):
        bagian_input = user_input.split()

        if len(bagian_input) < 2:
            print("Nama file tidak boleh kosong. Tolong gunakan format yang benar /save nama file (/save python)")
        else:
            nama_file = bagian_input[1]
            simpan_history(nama_file)
    elif user_input.lower().startswith("/load"):
        bagian_input = user_input.split()

        if len(bagian_input) < 2:
            print("Nama file tidak boleh kosong. Tolong gunakan format yang benar /load nama file (/load python)")
        else:
            nama_file = bagian_input[1]
            load_history(nama_file)
    else:
        jawaban_ai = jawaban_dummy(user_input)
        history.append({"user": user_input, "assistant": jawaban_ai})
        print(f" AI: {jawaban_ai}")

# penjelasan kode:
# 1. Program ini adalah sebuah AI Assistant sederhana yang dapat memberikan jawaban berdasarkan mode yang dipilih oleh pengguna.
# 2. Program memiliki beberapa command seperti /help, /mode, /history, /clear, dan /exit untuk membantu pengguna dalam berinteraksi dengan AI Assistant.

# history = [] adalah list yang digunakan untuk menyimpan riwayat percakapan antara pengguna dan AI Assistant. Setiap kali pengguna mengajukan pertanyaan, jawaban dari AI Assistant akan disimpan dalam history sebagai sebuah dictionary dengan kunci "user" untuk pertanyaan pengguna dan "assistant" untuk jawaban AI.

# global adalah keyword yang digunakan untuk mengakses variabel mode yang dideklarasikan di luar fungsi pilih_mode(). Dengan menggunakan global, kita dapat mengubah nilai variabel mode di dalam fungsi tersebut sehingga perubahan tersebut akan terlihat di seluruh program. Jika kita tidak menggunakan global, maka variabel mode yang dideklarasikan di dalam fungsi akan menjadi variabel lokal yang hanya berlaku di dalam fungsi tersebut, dan perubahan nilai mode tidak akan mempengaruhi variabel mode di luar fungsi.

# strip() adalah metode string yang digunakan untuk menghapus spasi di awal dan akhir string. Dalam konteks program ini, user_input.strip() digunakan untuk memastikan bahwa input yang diberikan oleh pengguna tidak memiliki spasi yang tidak diinginkan di awal atau akhir, sehingga memudahkan dalam memproses perintah atau pertanyaan yang diberikan oleh pengguna.

# lower() adalah metode string yang digunakan untuk mengubah semua karakter dalam string menjadi huruf kecil. Dalam program ini, user_input.lower() digunakan untuk memastikan bahwa perintah yang diberikan oleh pengguna dapat dikenali tanpa memperhatikan kapitalisasi huruf. Misalnya, jika pengguna mengetik "/HELP" atau "/help", kedua input tersebut akan dianggap sama karena keduanya akan diubah menjadi "/help" sebelum diproses.

# ================= fase 2 -day 02 ============
# Fungsi simpan_history() digunakan untuk menyimpan riwayat percakapan yang tersimpan dalam list history ke dalam sebuah file JSON dengan nama yang ditentukan oleh variabel NAMA_FILE. Fungsi ini menggunakan modul json untuk melakukan serialisasi data history menjadi format JSON dan menyimpannya ke dalam file. Jika proses penyimpanan berhasil, akan muncul pesan konfirmasi, namun jika terjadi kesalahan selama proses penyimpanan, akan muncul pesan error yang menjelaskan penyebab kegagalan.

# Fungsi load_history() digunakan untuk memuat riwayat percakapan dari sebuah file JSON dengan nama yang ditentukan oleh variabel NAMA_FILE ke dalam list history. Fungsi ini menggunakan modul json untuk melakukan deserialisasi data dari file JSON dan menyimpannya ke dalam list history. Jika proses pemuatan berhasil, akan muncul pesan konfirmasi, namun jika terjadi kesalahan seperti file tidak ditemukan atau file JSON tidak valid, akan muncul pesan error yang menjelaskan penyebab kegagalan.

# with open(NAMA_FILE, "w", encoding="utf-8") as file: adalah sebuah pernyataan yang digunakan untuk membuka file dengan nama yang ditentukan oleh variabel NAMA_FILE dalam mode penulisan ("w") dan dengan encoding UTF-8. Pernyataan ini menggunakan konteks manager with untuk memastikan bahwa file akan ditutup secara otomatis setelah blok kode di dalamnya selesai dieksekusi, bahkan jika terjadi kesalahan selama proses penulisan ke file. Dengan menggunakan with, kita tidak perlu secara eksplisit menutup file dengan file.close(), karena konteks manager akan menangani hal tersebut secara otomatis.

# json.dump(history, file, ensure_ascii=False, indent=4) adalah sebuah fungsi dari modul json yang digunakan untuk menulis data history ke dalam file dalam format JSON. Fungsi ini mengambil tiga argumen: data yang akan ditulis (history), objek file tempat data akan ditulis (file), dan dua parameter opsional yaitu ensure_ascii=False yang memastikan bahwa karakter non-ASCII akan disimpan dengan benar dalam file JSON, dan indent=4 yang memberikan format indentasi agar file JSON lebih mudah dibaca oleh manusia. Dengan menggunakan json.dump(), data history akan diserialisasi menjadi format JSON dan disimpan ke dalam file yang telah dibuka sebelumnya.

# try except adalah sebuah konstruksi dalam bahasa pemrograman Python yang digunakan untuk menangani kesalahan atau exception yang mungkin terjadi selama eksekusi program. Blok try berisi kode yang mungkin menghasilkan kesalahan, sedangkan blok except berisi kode yang akan dijalankan jika terjadi kesalahan. Dalam konteks program ini, try except digunakan untuk menangani kemungkinan kesalahan yang dapat terjadi saat menyimpan atau memuat riwayat percakapan ke atau dari file JSON, seperti file tidak ditemukan, file JSON tidak valid, atau kesalahan lainnya. Dengan menggunakan try except, program dapat memberikan pesan error yang informatif kepada pengguna jika terjadi kesalahan selama proses penyimpanan atau pemuatan data.

# exception adalah sebuah objek yang mewakili kesalahan atau error yang terjadi selama eksekusi program. Dalam blok except, kita dapat menangkap exception yang terjadi dan memberikan penanganan yang sesuai, seperti menampilkan pesan error kepada pengguna. Dalam konteks program ini, exception digunakan untuk menangkap kesalahan yang mungkin terjadi saat menyimpan atau memuat riwayat percakapan ke atau dari file JSON, sehingga program dapat memberikan informasi yang jelas tentang penyebab kegagalan proses tersebut.

# fileNotFoundError adalah sebuah jenis exception yang terjadi ketika program mencoba untuk membuka file yang tidak ada atau tidak ditemukan di lokasi yang ditentukan. Dalam konteks program ini, FileNotFoundError digunakan untuk menangani kasus ketika pengguna mencoba memuat riwayat percakapan dari file JSON yang tidak ada, sehingga program dapat memberikan pesan error yang informatif kepada pengguna tentang masalah tersebut.

# json.jsonDecodeError adalah sebuah jenis exception yang terjadi ketika program mencoba untuk memuat data dari file JSON yang tidak valid atau tidak sesuai dengan format JSON yang benar. Dalam konteks program ini, json.JSONDecodeError digunakan untuk menangani kasus ketika pengguna mencoba memuat riwayat percakapan dari file JSON yang tidak valid, sehingga program dapat memberikan pesan error yang informatif kepada pengguna tentang masalah tersebut.

# startwith() adalah sebuah metode string yang digunakan untuk memeriksa apakah string dimulai dengan substring tertentu. Dalam konteks program ini, user_input.lower().startswith("/save") digunakan untuk memeriksa apakah input pengguna dimulai dengan perintah "/save", sehingga program dapat mengeksekusi fungsi simpan_history() jika perintah tersebut diberikan oleh pengguna. Metode ini membantu dalam mengenali perintah yang diberikan oleh pengguna tanpa memperhatikan kapitalisasi huruf.

# file_aktif adalah sebuah variabel global yang digunakan untuk menyimpan nama file JSON yang saat ini aktif atau sedang digunakan untuk menyimpan atau memuat riwayat percakapan. Variabel ini diperbarui setiap kali pengguna menyimpan atau memuat riwayat percakapan dari file JSON tertentu, sehingga program dapat menampilkan informasi tentang file yang sedang digunakan kepada pengguna.

# import adalah sebuah pernyataan yang digunakan untuk mengimpor modul atau pustaka eksternal ke dalam program Python. Dalam konteks program ini, import json digunakan untuk mengimpor modul json yang menyediakan fungsi-fungsi untuk bekerja dengan data dalam format JSON, seperti menyimpan dan memuat riwayat percakapan ke atau dari file JSON. Dengan mengimpor modul json, program dapat menggunakan fungsi-fungsi yang disediakan oleh modul tersebut untuk melakukan operasi terkait JSON.
