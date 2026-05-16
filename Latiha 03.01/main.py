class User:
    def __init__(self, nama, email):
        self.nama = nama
        self.email = email

    def login(self):
        print(f"[LOGIN] {self.nama} berhasil login menggunakan email {self.email}")


# Inheritance dari User
class Admin(User):
    def __init__(self, nama, email):
        super().__init__(nama, email)

    def tambah_game(self, game):
        print(f"[ADMIN] {self.nama} menambahkan game '{game.judul}' ke sistem")


# Inheritance dari User
class Customer(User):
    def __init__(self, nama, email):
        # super() digunakan untuk memanggil constructor parent
        super().__init__(nama, email)

    def beli_game(self, game):
        print(f"[CUSTOMER] {self.nama} memilih game '{game.judul}'")
        print("[TRANSAKSI] Memproses pembayaran...")
        print(f"[TRANSAKSI BERHASIL] {self.nama} berhasil membeli game '{game.judul}'")
        print(f"[TOTAL PEMBAYARAN] Rp{game.harga}")


class Game:
    def __init__(self, judul, harga):
        self.judul = judul
        self.harga = harga

    def tampilkan_info(self):
        print("===== INFORMASI GAME =====")
        print(f"Judul Game : {self.judul}")
        print(f"Harga      : Rp{self.harga}")
        print("===========================")



# MEMBUAT DATA GAME


game1 = Game("Minecraft", 300000)
game2 = Game("GTA V", 250000)


# MEMBUAT USER


admin = Admin("Rodhi", "admin@gmail.com")
customer = Customer("Asep", "user@gmail.com")


# SUBTYPING


print("===== LOGIN USER =====")

users = [admin, customer]

for user in users:
    user.login()

print()


# AKTIVITAS ADMIN


print("===== AKTIVITAS ADMIN =====")

admin.tambah_game(game1)
admin.tambah_game(game2)

print("[STATUS] Semua game berhasil ditambahkan")

print()


# AKTIVITAS CUSTOMER


print("===== AKTIVITAS CUSTOMER =====")

customer.beli_game(game1)

print()

customer.beli_game(game2)

print()


# MENAMPILKAN DATA GAME


game1.tampilkan_info()

print()

game2.tampilkan_info()

print()


# PENUTUP SISTEM


print("===== SISTEM =====")
print("Terima kasih telah menggunakan Game Store Management System")