import json
import os

FILE_KARAKTER = "karakter.json"

karakter_list = [
    {
        "nama" : "Kei Tendou",
        "status" : "Online",
        "pesan_terakhir" : "Umm... selamat pagi senseii",
        "file_chat" : "kei.json",
        "gaya" : "Tsundere dan sedikit pemalu"
    },
    {
        "nama" : "Hayase Yuuka",
        "status" : "Offline",
        "pesan_terakhir" : "Sensei, jangan lupa periksa jadwal hari ini yaa",
        "file_chat" : "yuuka.json",
        "gaya" : "Tegas dan tsundere"
    },
    {
        "nama" : "Sorasaki Hina",
        "status" : "Offline",
        "pesan_terakhir" : "Ah sensei, apa kamu sudah sarapan? Aku sudah menyiapkan sarapan untukmu",
        "file_chat" : "hina.json",
        "gaya" : "Perhattian dan pemalu"
    }
]

FOLDER_CHAT ="chats"

def tampilkan_daftar_karakter():
    print("\n" + "=" * 40)
    print("      Kivotos Messenger")
    print("=" * 40)

    for nomor, karakter in enumerate(karakter_list, start=1):
        print(f"\n{nomor}, {karakter['nama']} | {karakter['status']}")
        # print(f"Pesan terakhir: {karakter['pesan_terakhir']}")
        preview = potong_preview(karakter["pesan_terakhir"])
        print(f'    "{preview}"')

def jawaban_dummy(karakter, pesan_user):
    nama = karakter["nama"]
    gaya = karakter["gaya"]
    pesan_user = pesan_user.lower()

    if nama == "Kei Tendou":
        if "halo" in pesan_user or "hai" in pesan_user:
            return "Uh sensei... ummm halo juga"
        elif "belajar" in pesan_user:
            return "Umm sensei bisa bantu aku belajar? Ah ini bukan berarti aku mau belajar sama sensei berdua yaa..."
        else:
            return "Umm... aku belum tahu harus membalas apa untuk pesan ini, sensei"
    elif nama == "Hayase Yuuka":
        if "halo" in pesan_user or "hai" in pesan_user:
            return "Halo sensei, ada yang bisa aku bantu?"
        elif "jadwal" in pesan_user:
            return "Jadwal hari ini sudah aku periksa, sensei. Tidak ada jadwal penting hari ini. Jadi mau jalan bareng gak sensei? Ahh bukan itu maksudku, aku cuma mau bilang kalau jadwal hari ini aman, sensei."
        else:
            return "Maaf sensei, aku belum tahu bagaimana membalas pesan ini."
    elif nama == "Sorasaki Hina":
        if "halo" in pesan_user or "hai" in pesan_user:
            return "Halo sensei, apa kabar hari ini?"
        elif "sarapan" in pesan_user:
            return "Ah sensei, aku sudah menyiapkan sarapan untukmu. Silakan makan sebelum berangkat."
        else:
            return "Maaf sensei, aku belum tahu bagaimana membalas pesan ini."

    if "halo" in pesan_user or "hai" in pesan_user:
                return "Uh ummm halo juga"
    elif "belajar" in pesan_user:
        return "Ya, kita bisa belajar"
    else:
        return "Umm... aku belum tahu harus membalas apa untuk pesan ini"
    

def buat_folder_chat():
    if not os.path.exists(FOLDER_CHAT):
        os.makedirs(FOLDER_CHAT)

def ambil_path_chat(karakter):
    return os.path.join(FOLDER_CHAT, karakter["file_chat"])

def load_chat_karakter(karakter):
    buat_folder_chat()
    path_file = ambil_path_chat(karakter)

    try:
        with open(path_file, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print(f"Terjadi kesalahan saat memuat riwayat chat dari {path_file}. File mungkin rusak.")
        return []

def simpan_chat_karakter(karakter, history):
    buat_folder_chat()
    path_file = ambil_path_chat(karakter)

    try:
        with open(path_file, "w", encoding="utf-8") as file:
            json.dump(history, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan riwayat chat ke {path_file}: {e}")

def simpan_data_karakter():
    try:
        with open(FILE_KARAKTER, "w", encoding="utf-8") as file:
            json.dump(karakter_list, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data karakter ke {FILE_KARAKTER}: {e}")

def load_data_karakter():
    global karakter_list

    try:
        with open(FILE_KARAKTER, "r", encoding="utf-8") as file:
            karakter_list = json.load(file)
    except FileNotFoundError:
        simpan_data_karakter()
    except json.JSONDecodeError:
        print("Terjadi kesalahan saat memuat riwayat chat dari. File mungkin rusak.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data karakter ke {FILE_KARAKTER}: {e}")

def potong_preview(teks, batas=50):
    if len(teks) > batas:
        return teks[:batas] + "....."
    return teks

def buat_nama_file(nama):
    nama = nama.lower()
    nama = nama.replace("", "_")
    return nama + ".json"

def tambah_karakter():
    print("\n--- TAMBAH KARAKTER ---")

    nama = input("Nama karakter: ").strip()

    if not nama:
        print("Nama tidak boleh kosong...")
        return

    for karakter in karakter_list:
        if karakter["nama"].lower() == nama.lower():
            print("Nama karakter sudah ada...")
            return

    status = input("Status (Online/Offline): ").strip()

    if status.lower() == "online":
        status = "Online"
    else:
        status = "Offline"

    pesan_awal = input("Pesan awal: ").strip()

    if not pesan_awal:
        pesan_awal = "Belum ada pesan..."

    gaya = input("Gaya karakter: ").strip()

    if not gaya:
        gaya = "ramah"

    karakter_baru = {
        "nama" : nama,
        "status" : status,
        "pesan_terakhir" : pesan_awal,
        "file_chat" : buat_nama_file(nama),
        "gaya" : gaya
    }

    karakter_list.append(karakter_baru)
    simpan_data_karakter()

    print(f"Karakter {nama} berhasil ditambahkan")

def edit_karakter(nomor):
    if nomor < 1 or nomor > len(karakter_list):
        print("Nomor karakter tidak tersedia di daftar...")
        return
    karakter = karakter_list[nomor - 1]

    print("\n--- EDIT KARAKTER ---")
    print(f"Nama sekarang                 : {karakter['nama']}")
    print(f"Status sekarang               : {karakter['status']}")
    print(f"Gaya sekarang                 : {karakter['gaya']}")
    print(f"Pesan terakhir sekarang       : {karakter['pesan_terakhir']}")
    print("\nKosongkan input jika tidak ingin mengubah bagian tersebut.")

    nama_baru = input("Nama baru: ").strip()
    status_baru = input("Status baru (Online/Offline): ").strip()
    gaya_baru = input("Gaya baru: ").strip()
    pesan_baru = input("Pesan baru: ").strip()

    if nama_baru:
        for data in karakter_list:
            if data["nama"].lower() == nama_baru.lower() and data != karakter:
                print("Nama tersebut sudah digunakan pada karakter lain.")
                return
        file_lama = karakter["file_chat"]
        file_baru = buat_nama_file(nama_baru)
        path_lama = os.path.join("chats", file_lama)
        path_baru = os.path.join("chats", file_baru)

        if os.path.exists(path_lama):
            os.rename(path_lama, path_baru)

        karakter["nama"] = nama_baru
        karakter["file_chat"] = file_baru

    if status_baru:
        if status_baru.lower() == "online":
            karakter["status"] = "Online"
        elif status_baru.lower() == "offline":
            karakter["status"] = "Offline"
        else:
            print("Status tidak valid. Status lama tetap dipakai...")

    if gaya_baru:
        karakter["gaya"] = gaya_baru

    if pesan_baru:
        karakter["pesan_terakhir"] = pesan_baru

    simpan_data_karakter()
    print(f"Data karakter {karakter['nama']} berhasil diperbarui")

def hapus_karakter(nomor):
    if nomor < 1 or nomor > len(karakter_list):
            print("Nomor karakter tidak tersedia di daftar...")
            return
    karakter = karakter_list[nomor - 1]

    print("\n--- HAPUS KARAKTER ---")
    print(f"Nama karakter   : {karakter['nama']}")
    print(f"File chat       : {karakter['file_chat']}")

    konfirmasi = input(f'Ketik "hapus" untuk menghapus {karakter["nama"]}: ').strip().lower()

    if konfirmasi != "hapus":
        print("Prose dibatalkan...")
        return

    path_chat = os.path.join("chats", karakter["file_chat"])

    try:
        if os.path.exists(path_chat):
            os.remove(path_chat)
            print("File chat berhasil dihapus...")
        else:
            print("File chat tidak ditemukan, tetapi data karakter tetap dihapus")

        karakter_list.pop(nomor - 1)
        simpan_data_karakter()
        print(f"Karakter {karakter['nama']} berhasil dihapus...")
    except Exception as e:
        print("Gagal menghapus karakter:", e)

load_data_karakter()

while True:
    tampilkan_daftar_karakter()
    pilihan = input("\nPilih nomor karakter atau ketik /exit untuk keluar, /add untuk tambah karakter: ").strip()

    if pilihan.lower() == "/exit":
        print("Arigatou sensei, sampai jumpa lagi!")
        break
    elif pilihan.lower() == "/add":
        tambah_karakter()
        continue
    elif pilihan.lower().startswith("/edit"):
        bagian_perintah = pilihan.split()

        if len(bagian_perintah) != 2:
            print("Format salah. Contoh penggunaan: /edit 4")
            continue

        if not bagian_perintah[1].isdigit():
            print("Nomor karakter harus berupa angka...")
            continue

        nomor_edit = int(bagian_perintah[1])
        edit_karakter(nomor_edit)
        continue
    elif pilihan.lower().startswith("/delete"):
        bagian_perintah = pilihan.split()

        if len(bagian_perintah) != 2:
            print("Format salah. Contoh penggunaan: /edit 4")
            continue
        
        if not bagian_perintah[1].isdigit():
            print("Nomor karakter harus berupa angka...")
            continue

        nomor_hapus = int(bagian_perintah[1])
        hapus_karakter(nomor_hapus)
        continue

    if not pilihan.isdigit():
        print("Pilihan tidak valid. Silakan masukkan nomor karakter atau /exit atau /add.")
        continue

    pilihan = int(pilihan)
    if pilihan < 1 or pilihan > len(karakter_list):
        print("Pilihan tidak valid. Silakan pilih nomor karakter yang tersedia.")
        continue

    karakter_dipilih = karakter_list[pilihan - 1]
    history_chat = load_chat_karakter(karakter_dipilih)
    print(f"\n" + "-" * 40)
    print(f"Chat dengan {karakter_dipilih['nama']}")
    print(f"Status: {karakter_dipilih['status']}")
    print("Commadn: /back, /history, /clear")
    print("-" * 40)

    if history_chat:
        print("\n--- Riwayat Chat ---")

        for chat in history_chat:
            print(f"Kamu: {chat['user']}")
            print(f"{karakter_dipilih['nama']}: {chat['assistant']}")
            print("-" * 25)
    else:
        print("\nBelum ada riwayat chat dengan karakter ini.")

    while True:
        pesan_user = input("\nKamu: ").strip()
        if pesan_user.lower() == "/back":
            break
        elif pesan_user.lower() == "/history":
            if not history_chat:
                print("Belum ada riwayat chat dengan karakter ini.")
            else:
                print("\n--- RIWAYAT CHAT---")

                for chat in history_chat:
                    print(f"Kamu: {chat['user']}")
                    print(f"{karakter_dipilih['nama']}: {chat['assistant']}")
                    print("-" * 25)
            continue
        elif pesan_user.lower() == "/clear":
            history_chat.clear()
            simpan_chat_karakter(karakter_dipilih, history_chat)

            karakter_dipilih["pesan_terakhir"] = "Belum ada pesan..."
            simpan_data_karakter()

            print("Riwayat chat dengan karakter ini berhasil dihapus")
            continue


        if not pesan_user:
            print("Pesan tidak boleh kosong. Silakan masukkan pesan.")
            continue

        jawaban = jawaban_dummy(karakter_dipilih, pesan_user)

        history_chat.append({
            "user" : pesan_user,
            "assistant" : jawaban
        })

        karakter_dipilih["pesan_terakhir"] = jawaban
        simpan_data_karakter()

        simpan_chat_karakter(karakter_dipilih, history_chat)
        print(f"{karakter_dipilih['nama']}: {jawaban}")