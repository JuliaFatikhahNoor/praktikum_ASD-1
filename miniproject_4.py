import math 
class Dessert:
    def __init__(self, nama_dessert, stok_dessert, harga, varian_rasa, jenis_dessert):
        self.nama = nama_dessert
        self.stok = stok_dessert
        self.harga = harga
        self.varian_rasa = varian_rasa 
        self.jenis = jenis_dessert
        self.next = None

class TokoDessert:
    def __init__(self, menu_dessert):
        self.head = None
        self.tail = None
        for dessert in menu_dessert:
            self.add_last(dessert["nama"], dessert["stok"], dessert["harga"], dessert["varian_rasa"], dessert["jenis"])

    def __len__(self):
        node = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def is_empty(self):
        return self.head is None

    def add_first(self, nama, stok, harga, varian_rasa, jenis):
        new_node = Dessert(nama, stok, harga, varian_rasa, jenis)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def add_last(self, nama, stok, harga, varian_rasa, jenis):
        new_node = Dessert(nama, stok, harga, varian_rasa, jenis)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def add_after(self, node_name, nama, stok, harga, varian_rasa, jenis):
        if self.is_empty():
            raise ValueError("List is empty.")
        new_node = Dessert(nama, stok, harga, varian_rasa, jenis)
        current_node = self.head
        while current_node.nama != node_name:
            current_node = current_node.next
            if current_node is None:
                raise ValueError(f"Node '{node_name}' not found.")
        new_node.next = current_node.next
        current_node.next = new_node

    def remove_first(self):
        if self.is_empty():
            raise ValueError("List is empty.")
        removed_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return removed_node

    def remove_last(self):
        if self.is_empty():
            raise ValueError("List is empty.")
        if self.head == self.tail:
            removed_node = self.head
            self.head = self.tail = None
            return removed_node
        previous_node = None
        current_node = self.head
        while current_node.next is not None:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        self.tail = previous_node
        return current_node

    def remove_after(self, node_name):
        if self.is_empty():
            raise ValueError("List is empty.")
        current_node = self.head
        previous_node = None
        while current_node.nama != node_name:
            previous_node = current_node
            current_node = current_node.next
            if current_node is None:
                raise ValueError(f"Node '{node_name}' not found.")
        if current_node == self.tail:
            self.tail = previous_node
        previous_node.next = current_node.next
        return current_node

    def find_by_name(self, nama):
        current_node = self.head
        while current_node is not None:
            if current_node.nama == nama:
                return current_node
            current_node = current_node.next
        return None
    
    def tambah_node_awal(self):
        nama = input("Masukkan nama dessert: ")
        stok = int(input("Masukkan stok dessert: "))
        harga = float(input("Masukkan harga dessert: "))
        varian_rasa_input = input("Masukkan varian rasa dessert (pisahkan dengan koma): ")
        varian_rasa = varian_rasa_input.split(',') if varian_rasa_input else []
        jenis = input("Masukkan jenis dessert: ")
        self.add_first(nama, stok, harga, varian_rasa, jenis)

    def tambah_node_akhir(self):
        nama = input("Masukkan nama dessert: ")
        stok = int(input("Masukkan stok dessert: "))
        harga = float(input("Masukkan harga dessert: "))
        varian_rasa_input = input("Masukkan varian rasa dessert (pisahkan dengan koma): ")
        varian_rasa = varian_rasa_input.split(',') if varian_rasa_input else []
        jenis = input("Masukkan jenis dessert: ")
        self.add_last(nama, stok, harga, varian_rasa, jenis)

    def tambah_node_setelah(self):
        node_name = input("Masukkan nama node setelahnya: ")
        nama = input("Masukkan nama dessert: ")
        stok = int(input("Masukkan stok dessert: "))
        harga = float(input("Masukkan harga dessert: "))
        varian_rasa_input = input("Masukkan varian rasa dessert (pisahkan dengan koma): ")
        varian_rasa = varian_rasa_input.split(',') if varian_rasa_input else []
        jenis = input("Masukkan jenis dessert: ")
        self.add_after(node_name, nama, stok, harga, varian_rasa, jenis)

    def hapus_node_awal(self):
        removed_node = self.remove_first()
        print(f"Dessert {removed_node.nama} berhasil dihapus dari menu.")

    def hapus_node_akhir(self):
        removed_node = self.remove_last()
        print(f"Dessert {removed_node.nama} berhasil dihapus dari menu.")

    def hapus_node_setelah(self):
        node_name = input("Masukkan nama node setelahnya: ")
        removed_node = self.remove_after(node_name)
        print(f"Dessert {removed_node.nama} berhasil dihapus dari menu.")

    def tampilkan_menu_dessert(self):
        if self.is_empty():
            print("Menu dessert kosong.")
            return

        current_node = self.head
        nomor_urut = 1

        print("=================================================================================")
        print("| No |            Nama             | Stok |   Harga   |        Varian Rasa      |")
        print("=================================================================================")

        while current_node is not None:
            varian_rasa = ', '.join(current_node.varian_rasa) if current_node.varian_rasa else "-"
            jenis = current_node.jenis if current_node.jenis else "-"
            print(f"| {nomor_urut:2} | {current_node.nama:27} | {current_node.stok:4} | {current_node.harga:9} | {varian_rasa:23} |")
            current_node = current_node.next
            nomor_urut += 1
        
        print("=================================================================================")

    def update_stok_dessert(self, nama_dessert, stok_baru):
        node = self.find_by_name(nama_dessert)
        if node:
            node.stok = stok_baru
            print(f"Stok {nama_dessert} berhasil diperbarui menjadi {stok_baru}.")
        else:
            print(f"{nama_dessert} tidak ditemukan dalam menu dessert.")

    def hapus_dessert(self, nama_dessert):
        if not nama_dessert:
            print("Masukkan nama dessert yang ingin dihapus.")
            return

        current_node = self.head
        previous_node = None
        while current_node is not None:
            if current_node.nama == nama_dessert:
                if previous_node is None:
                    self.head = current_node.next
                    if self.head is None:
                        self.tail = None
                else:
                    previous_node.next = current_node.next
                    if current_node.next is None:
                        self.tail = previous_node
                print(f"Dessert {nama_dessert} berhasil dihapus dari menu.")
                return
            previous_node = current_node
            current_node = current_node.next

        print(f"Dessert {nama_dessert} tidak ditemukan dalam menu dessert.")

    def lakukan_penjualan(self, nomor_dessert, jumlah):
        nomor_dessert = int(nomor_dessert)
        current_node = self.head
        nomor_urut = 1
        while current_node is not None and nomor_urut < nomor_dessert:
            current_node = current_node.next
            nomor_urut += 1

        if current_node is not None and nomor_urut == nomor_dessert:
            if current_node.stok >= jumlah:
                current_node.stok -= jumlah
                total_harga = jumlah * current_node.harga
                print(f"Pembelian {jumlah} {current_node.nama} berhasil. Total harga: Rp{total_harga}")
            else:
                print(f"Stok {current_node.nama} tidak mencukupi.")
        else:
            print("Dessert tidak ditemukan atau nomor urut tidak valid.")


    def kelola_menu(self):
        while True:
            print("\n--------------------------")
            print("|        Kelola Menu     |")
            print("--------------------------")
            print("|     1. Tambah Dessert  |")
            print("|     2. Hapus Dessert   |")
            print("|     3. Tampilkan Menu  |")
            print("|     4. Update Menu     |")
            print("|     5. Tambah Node     |")  
            print("|     6. Hapus Node      |")
            print("|     7. Kembali         |")
            print("--------------------------")
            pilihan = input("Masukkan pilihan menu: ")
            if pilihan == "1":
                self.menambahkan_dessert()
            elif pilihan == "2":
                nama_dessert = input("Masukkan nama dessert yang akan dihapus: ")
                self.hapus_dessert(nama_dessert)
            elif pilihan == "3":
                self.tampilkan_menu_dessert()
            elif pilihan == "4":
                nama_dessert = input("Masukkan nama dessert yang akan diupdate: ")
                stok_baru = int(input("Masukkan stok baru untuk dessert : "))
                self.update_stok_dessert(nama_dessert, stok_baru) 
            elif pilihan == "5":
                self.tambah_node_menu()  
            elif pilihan == "6":
                self.hapus_node_menu()  
            elif pilihan == "7":
                print("Terima kasih. Sampai jumpa!")
                break
            else:
                print("Pilihan tidak valid.")
                continue

    def tambah_node_menu(self):
        while True:
            print("\n-----------------------------")
            print("|      Tambah Node Menu     |")
            print("-----------------------------")
            print("|     1. Tambah Node Awal    |")
            print("|     2. Tambah Node Akhir   |")
            print("|     3. Tambah Node Setelah |")
            print("|     4. Kembali             |")
            print("-----------------------------")
            pilihan = input("Masukkan pilihan menu: ")
            if pilihan == "1":
                self.tambah_node_awal()  
            elif pilihan == "2":
                self.tambah_node_akhir()  
            elif pilihan == "3":
                self.tambah_node_setelah()  
            elif pilihan == "4":
                break
            else:
                print("Pilihan tidak valid.")

    def hapus_node_menu(self):
        while True:
            print("\n-----------------------------")
            print("|      Hapus Node Menu      |")
            print("-----------------------------")
            print("|     1. Hapus Node Awal     |")
            print("|     2. Hapus Node Akhir    |")
            print("|     3. Hapus Node Setelah  |")
            print("|     4. Kembali             |")
            print("-----------------------------")
            pilihan = input("Masukkan pilihan menu: ")
            if pilihan == "1":
                self.hapus_node_awal()  
            elif pilihan == "2":
                self.hapus_node_akhir()  
            elif pilihan == "3":
                self.hapus_node_setelah()  
            elif pilihan == "4":
                break
            else:
                print("Pilihan tidak valid.")

    def menambahkan_dessert(self):
        nama = input("Masukkan nama dessert: ")
        stok = int(input("Masukkan stok dessert: "))
        harga = float(input("Masukkan harga dessert: "))
        varian_rasa_input = input("Masukkan varian rasa dessert (pisahkan dengan koma): ")
        varian_rasa = varian_rasa_input.split(',') if varian_rasa_input else []
        jenis = input("Masukkan jenis dessert: ")
        self.add_last(nama, stok, harga, varian_rasa, jenis)

    def quick_sort(self, arr, atribut, naik=True):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]

            if naik:
                lebih_kecil_dari_pivot = [item for item in arr[1:] if getattr(item, atribut) < getattr(pivot, atribut)]
                lebih_besar_dari_pivot = [item for item in arr[1:] if getattr(item, atribut) >= getattr(pivot, atribut)]
            else:
                lebih_kecil_dari_pivot = [item for item in arr[1:] if getattr(item, atribut) > getattr(pivot, atribut)]
                lebih_besar_dari_pivot = [item for item in arr[1:] if getattr(item, atribut) <= getattr(pivot, atribut)]

            return self.quick_sort(lebih_kecil_dari_pivot, atribut, naik) + [pivot] + self.quick_sort(lebih_besar_dari_pivot, atribut, naik)
        
    def dapatkan_daftar_dessert(self):
        daftar_dessert = []
        current_node = self.head
        while current_node is not None:
            daftar_dessert.append(current_node)
            current_node = current_node.next
        return daftar_dessert

    def urutkan_dessert(self, atribut, naik=True):
        if atribut not in ["nama", "stok", "harga", "jenis"]:
            print("Atribut yang dimasukkan tidak valid.")
            return
        
    def __init__(self, menu_dessert):
        self.head = None
        self.tail = None
        self.id_counter = 1 
        for dessert in menu_dessert:
            self.add_last(dessert["nama"], dessert["stok"], dessert["harga"], dessert["varian_rasa"], dessert["jenis"])

    def jump_search_nama(self, nama_dessert):
        current_node = self.head
        while current_node is not None and current_node.nama != nama_dessert:
            current_node = current_node.next
        return current_node

    def jump_search_harga(self, harga_dessert):
        current_node = self.head
        while current_node is not None and current_node.harga != harga_dessert:
            current_node = current_node.next
        return current_node

    def jump_search_id(self, nomor_dessert):
        current_node = self.head
        count = 1
        while current_node is not None and count != nomor_dessert:
            current_node = current_node.next
            count += 1
        return current_node
    
    def cari_dessert(self):
        print("\n--------------------------")
        print("|     Pencarian Dessert   |")
        print("--------------------------")
        print("|   1. Berdasarkan Nama   |")
        print("|   2. Berdasarkan Harga  |")
        print("|   3. Berdasarkan ID     |")
        print("|   4. Kembali            |")
        print("--------------------------")
        pilihan = input("Masukkan pilihan pencarian: ")

        if pilihan == "1":
            nama_dessert = input("Masukkan nama dessert yang ingin dicari: ")
            dessert = self.jump_search_nama(nama_dessert)
            if dessert:
                print("Dessert ditemukan:\n")
                self.tampilkan_detail_dessert(dessert)
            else:
                print("Dessert tidak ditemukan.")
        elif pilihan == "2":
            harga_dessert = float(input("Masukkan harga dessert yang ingin dicari: "))
            dessert = self.jump_search_harga(harga_dessert)
            if dessert:
                print("Dessert ditemukan:\n")
                self.tampilkan_detail_dessert(dessert)
            else:
                print("Dessert tidak ditemukan.")
        elif pilihan == "3":
            nomor_dessert = int(input("Masukkan nomor dessert yang ingin dicari: "))
            dessert = self.jump_search_id(nomor_dessert)  # Menggunakan nomor urut sebagai id
            if dessert:
                print("Dessert ditemukan:\n")
                self.tampilkan_detail_dessert(dessert)
            else:
                print("Dessert tidak ditemukan.")
        elif pilihan == "4":
            pass  # Keluar dari menu pencarian
        else:
            print("Pilihan tidak valid.")

    def tampilkan_detail_dessert(self, dessert):
        print("Detail Dessert:")
        print(f"Nama: {dessert.nama}")
        print(f"Stok: {dessert.stok}")
        print(f"Harga: {dessert.harga}")
        print(f"Varian Rasa: {', '.join(dessert.varian_rasa)}")
        print(f"Jenis: {dessert.jenis}")


if __name__ == "__main__":

    menu_dessert = [
        {"nama": "pudding", "varian_rasa": ["coklat", "fla"], "jenis": "pudding", "stok": 20, "harga": 20000},
        {"nama": "cream pie", "varian_rasa": ["fruit pie"], "jenis": "pie", "stok": 15, "harga": 30000},
        {"nama": "frozen yogurth", "varian_rasa": ["strawberry", "vanilla"], "jenis": "froxen dessert", "stok": 15, "harga": 25000},
        {"nama": "chocolate chip cookies", "varian_rasa": ["coklat"], "jenis": "cookies", "stok": 25, "harga": 15000},
        {"nama": "peanut butter banana pie", "varian_rasa": ["peanut_banana"], "jenis": "pie", "stok": 20, "harga": 30000}
    ]
    toko = TokoDessert(menu_dessert)

    while True:
        print("\n--------------------------")
        print("|        Menu Utama      |")
        print("--------------------------")
        print("|     1. Lihat Menu      |")
        print("|     2. Pesan Dessert   |")
        print("|     3. Kelola Menu     |")
        print("|     4. Urutkan Dessert |")
        print("|     5. Mencari Dessert |")
        print("|     6. Keluar          |")
        print("--------------------------")
        pilihan = input("Masukkan pilihan menu: ")

        if pilihan == "1":
            toko.tampilkan_menu_dessert()
        elif pilihan == "2":
            nomor_dessert = input("Masukkan nomor dessert yang ingin dipesan: ")
            jumlah = int(input("Masukkan jumlah yang ingin dipesan: "))
            toko.lakukan_penjualan(nomor_dessert, jumlah)
        elif pilihan == "3":
            toko.kelola_menu()
        elif pilihan == "4":
            atribut_urut = input("Masukkan atribut yang ingin diurutkan (nama, stok, harga, jenis): ")
            if atribut_urut not in ["nama", "stok", "harga", "jenis"]:
                print("Atribut yang dimasukkan tidak valid.")
                continue
            urutan = input("Ascending (1) atau Descending (2)? ").upper()
            if urutan not in ["1", "2"]:
                print("Pilihan urutan tidak valid.")
                continue
            naik = urutan == "1"
            toko.urutkan_dessert(atribut_urut, naik)
            toko.tampilkan_menu_dessert()
        elif pilihan == "5":
            toko.cari_dessert()
        elif pilihan == "6":
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")
