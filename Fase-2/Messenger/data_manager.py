import json
import os

FILE_KARAKTER = "karakter.json"
FOLDER_CHAT ="chats"

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

def simpan_data_karakter(karakter_list):
    try:
        with open(FILE_KARAKTER, "w", encoding="utf-8") as file:
            json.dump(karakter_list, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data karakter ke {FILE_KARAKTER}: {e}")

def load_data_karakter(karakter_list):
    # global karakter_list

    try:
        with open(FILE_KARAKTER, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        simpan_data_karakter(karakter_list)
        return karakter_list
    except json.JSONDecodeError:
        print("Terjadi kesalahan saat memuat riwayat chat dari. File mungkin rusak.")
        return karakter_list
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan data karakter ke {FILE_KARAKTER}: {e}")
        return karakter_list