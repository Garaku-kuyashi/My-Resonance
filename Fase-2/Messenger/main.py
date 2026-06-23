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
        print(f"Pesan terakhir: {karakter['pesan_terakhir']}")

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

while True:
    tampilkan_daftar_karakter()
    pilihan = input("\nPilih karakter (1-3) atau ketik /exit untuk keluar: ").strip()

    if pilihan.lower() == "/exit":
        print("Arigatou sensei, sampai jumpa lagi!")
        break

    if not pilihan.isdigit():
        print("Pilihan tidak valid. Silakan masukkan nomor karakter atau /exit.")
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
    print("Ketik /back untuk kembali ke daftar karakter.")
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

        if not pesan_user:
            print("Pesan tidak boleh kosong. Silakan masukkan pesan.")
            continue

        jawaban = jawaban_dummy(karakter_dipilih, pesan_user)

        history_chat.append({
            "user" : pesan_user,
            "assistant" : jawaban
        })

        karakter_dipilih["pesan_terakhir"] = jawaban

        simpan_chat_karakter(karakter_dipilih, history_chat)
        print(f"{karakter_dipilih['nama']}: {jawaban}")