from data_manager import (
    load_chat_karakter,
    simpan_chat_karakter,
    simpan_data_karakter
)
from datetime import datetime

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

def tampilkan_history(karakter, history_chat):
     if not history_chat:
          print("Belum ada riwayat chat dengan karakter ini...")
          return
     print("\n--- RIWAYAT CHAT ---")
     for chat in history_chat:
        waktu = chat.get("waktu", "waktu tidak tersedia")
        print(f"[{waktu}] Kamu: {chat['user']}")
        print(f"{karakter['nama']}: {chat['assistant']}")
        print("-" * 35)

def buka_chat(karakter, karakater_list):
    history_chat = load_chat_karakter(karakter)

    print("\n" + "=" * 40)
    print(f"CHAT DENGAN {karakter['nama'].upper()}")
    print("=" * 40)
    print("Command: /back, /history, /clear")

    while True:
        pesan_user = input("\nKamu: ").strip()

        if pesan_user.lower() == "/back":
            break
        elif pesan_user.lower() == "/history":
            tampilkan_history(karakter, history_chat)
            continue
        elif pesan_user.lower() == "/clear":
            konfirmasi = input('Ketik "hapus" untuk menghapus seluruh history chat ini: ').strip().lower()

            if konfirmasi == "hapus":
                history_chat.clear()
                simpan_chat_karakter(karakter, history_chat)

                karakter["pesan_terakhir"] = "Belum ada pesan..."
                simpan_data_karakter(karakater_list)
                print("Riwayat chat berhasil dihapus...")
            else:
                print("Proses dibatalkan...")
            continue

        if not pesan_user:
            print("Pesan tidak boleh kosong")
            continue

        jawaban = jawaban_dummy(karakter, pesan_user)


        waktu_sekarang = datetime.now().strftime("%Y-%m-%d %H:%M")
        history_chat.append({
            "user" : pesan_user,
            "assistant" : jawaban,
            "waktu" : waktu_sekarang
        })

        karakter["pesan_terakhir"] = jawaban

        simpan_chat_karakter(karakter, history_chat)
        simpan_data_karakter(karakater_list)

        print(f"{karakter['nama']}: {jawaban}")
     