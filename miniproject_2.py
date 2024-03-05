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

    def tampilkan_menu_dessert(self):
        if self.is_empty():
            print("Menu dessert kosong.")
            return
        print ("\n=========================")
        print ("|      Menu Dessert     |")
        print ("=========================")
        current_node = self.head
        while current_node is not None:
            print(f"Nama: {current_node.nama}")
            print(f"Stok: {current_node.stok}")
            print(f"Harga: {current_node.harga}")
            if current_node.varian_rasa:
                print(f"Varian Rasa: {', '.join(current_node.varian_rasa)}")
            if current_node.jenis:
                print(f"Jenis: {current_node.jenis}")
            print ("=========================")
            current_node = current_node.next

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

    def lakukan_penjualan(self, nama_dessert, jumlah):
        if not nama_dessert:
            print("Masukkan dessert yang ingin dipesan")
            return 
        if not jumlah:
            print("Masukkan jumlah yang ingin dipesan")
            return 
        
        node = self.find_by_name(nama_dessert)
        if node:
            if node.stok >= jumlah:
                node.stok -= jumlah
                total_harga = jumlah * node.harga
                print(f"Pembelian {jumlah} {nama_dessert} berhasil. Total harga: Rp{total_harga}")
            else:
                print(f"Stok {nama_dessert} tidak mencukupi.")
        else:
            print(f"{nama_dessert} tidak ditemukan dalam menu dessert.")

    def kelola_menu(self):
        while True:
            print("\n--------------------------")
            print("|        Kelola Menu     |")
            print("--------------------------")
            print("|     1. Tambah Dessert  |")
            print("|     2. Hapus Dessert   |")
            print("|     3. Tampilkan Menu  |")
            print("|     4. Update Menu     |")
            print("|     5. Keluar          |")
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
        self.add_last(nama, stok, harga, varian_rasa, jenis)

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
        print("|     4. Keluar          |")
        print("--------------------------")
        pilihan = input("Masukkan pilihan menu: ")

        if pilihan == "1":
            toko.tampilkan_menu_dessert()
        elif pilihan == "2":
            nama_dessert = input("Masukkan nama dessert yang ingin dipesan: ")
            jumlah = int(input("Masukkan jumlah yang ingin dipesan: "))
            toko.lakukan_penjualan(nama_dessert, jumlah)
        elif pilihan == "3":
                toko.kelola_menu()
        elif pilihan == "4":
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")
