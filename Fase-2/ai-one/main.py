

history =  []
mode = "Browser Pembantu Penjelasan Teori"

def tampilkan_bantuan():
    print(""" Command yang tersedia:
          /help - akan menampilkan bantuan
          /mode - akan mengganti mode assistant
          /history - akan menampilkan history chat
          /clear - akan menghapus semua history chat
          /exit - akan keluar dari program
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
            print("== History Chat ==")
            for chat in history:
                print(f"Kamu: {chat['user']}")
                print(f"AI Assistant: {chat['assistant']}")
                print("-" * 25)
    else:
        jawaban_ai = jawaban_dummy(user_input)
        history.append({"user": user_input, "assistant": jawaban_ai})
        print(f" AI: {jawaban_ai}")