class Dessert:
    def __init__(self, nama_dessert, stok_dessert, harga, varian_rasa, jenis_dessert):
        self.nama = nama_dessert
        self.stok = stok_dessert
        self.harga = harga
        self.varian_rasa = varian_rasa 
        self.jenis = jenis_dessert

class TokoDessert:
    def __init__(self, menu_dessert):
        self.desserts = {}
        for dessert_info in menu_dessert:
            self.tambah_dessert(Dessert(
                dessert_info['nama'],  # Nama dessert
                dessert_info['stok'],  # Stok dessert
                dessert_info['harga'],  # Harga dessert
                dessert_info.get('varian_rasa', []),  # Varian rasa dessert
                dessert_info.get('jenis', '')  # Jenis dessert
            ))

    def tambah_dessert(self, dessert):
        self.desserts[dessert.nama] = dessert
        print(f"{dessert.nama} berhasil ditambahkan ke menu dessert.")

    def hapus_dessert(self, nama_dessert):
        if nama_dessert in self.desserts:
            del self.desserts[nama_dessert]
            print(f"{nama_dessert} berhasil dihapus dari menu dessert.")
        else:
            print(f"{nama_dessert} tidak ditemukan dalam menu dessert.")

    def update_stok_dessert(self, nama_dessert, stok_baru):
        if nama_dessert in self.desserts:
            self.desserts[nama_dessert].stok = stok_baru
            print(f"Stok {nama_dessert} berhasil diperbarui menjadi {stok_baru}.")
        else:
            print(f"{nama_dessert} tidak ditemukan dalam menu dessert.")

    def tampilkan_menu_dessert(self):
        print("=== Menu Dessert ===")
        for dessert in self.desserts.values():
            print(f"Nama: {dessert.nama}")
            print(f"Stok: {dessert.stok}")
            print(f"Harga: {dessert.harga}")
            if dessert.varian_rasa:
                print(f"Varian Rasa: {', '.join(dessert.varian_rasa)}")
            if dessert.jenis:
                print(f"Jenis: {dessert.jenis}")
            print("--------------------")

    def lakukan_penjualan(self, nama_dessert, jumlah):
        if nama_dessert in self.desserts:
            if self.desserts[nama_dessert].stok >= jumlah:
                self.desserts[nama_dessert].stok -= jumlah
                total_harga = jumlah * self.desserts[nama_dessert].harga
                print(f"Pembelian {jumlah} {nama_dessert} berhasil. Total harga: Rp{total_harga}")
            else:
                print(f"Stok {nama_dessert} tidak mencukupi.")
        else:
            print(f"{nama_dessert} tidak ditemukan dalam menu dessert.")

    def kelola_menu(self):
        while True:
            print("\n=== Kelola Menu ===")
            print("1. Tambah Dessert")
            print("2. Hapus Dessert")
            print("3. Tampilkan Menu")
            print("4. Update Menu")
            print("5. Keluar")
            pilihan = input("Masukkan pilihan menu: ")
            if pilihan == "1":
                self.menambahkan_dessert()
            elif pilihan == "2":
                nama_dessert = input("Masukkan nama dessert yang akan dihapus: ")
                self.hapus_dessert(nama_dessert)
            elif pilihan == "3":
                self.tampilkan_menu_dessert()
            elif pilihan == "4":
                nama_dessert = input("Masukkan nama dessert yang akan diperbarui stoknya: ")
                stok_baru = int(input("Masukkan stok baru untuk dessert tersebut: "))
                self.update_stok_dessert(nama_dessert, stok_baru)  # Perbaikan: Panggil metode dengan argumen yang benar
            elif pilihan == "5":
                print("Terima kasih. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid.")
                continue

    def menambahkan_dessert(self):
        nama = input("Masukkan nama dessert: ")
        stok = int(input("Masukkan stok dessert: "))
        harga = float(input("Masukkan harga dessert: "))
        varian_rasa_input = input("Masukkan varian rasa dessert (pisahkan dengan koma): ")
        varian_rasa = varian_rasa_input.split(',') if varian_rasa_input else []
        jenis = input("Masukkan jenis dessert: ")
        dessert = Dessert(nama, stok, harga, varian_rasa, jenis)
        self.tambah_dessert(dessert)

menu_dessert = [
    {"nama": "pudding", "varian_rasa": ["coklat", "fla"], "jenis": "pudding", "stok": 20, "harga": 20000},
    {"nama": "cream pie", "varian_rasa": ["fruit pie"], "jenis": "pie", "stok": 15, "harga": 30000},
    {"nama": "frozen yogurth", "varian_rasa": ["strawberry", "vanilla"], "jenis": "froxen dessert", "stok": 15, "harga": 25000},
    {"nama": "chocolate chip cookies", "varian_rasa": ["coklat"], "jenis": "cookies", "stok": 25, "harga": 15000},
    {"nama": "peanut butter banana pie", "varian_rasa": ["peanut_banana"], "jenis": "pie", "stok": 20, "harga": 30000}
]

if __name__ == "__main__":
    toko = TokoDessert(menu_dessert)

    while True:
        print("\n=== Menu Utama ===")
        print("1. Lihat Menu")
        print("2. Pesan Dessert")
        print("3. Kelola Menu (Admin)")
        print("4. Keluar")
        pilihan = input("Pilih aksi: ")

        if pilihan == "1":
            toko.tampilkan_menu_dessert()
        elif pilihan == "2":
            nama_dessert = input("Masukkan nama dessert yang ingin dipesan: ")
            jumlah = int(input("Masukkan jumlah yang ingin dipesan: "))
            toko.lakukan_penjualan(nama_dessert, jumlah)
        elif pilihan == "3":
                toko.kelola_menu()
                print("Password salah. Akses ditolak.")
        elif pilihan == "4":
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")
