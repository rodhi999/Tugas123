# Kelas Buku
class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status = "Tersedia"
        self.peminjam = "-"

    def tampil_info(self):
        print("Judul Buku :", self.judul)
        print("Penulis :", self.penulis)
        print("Tahun Terbit :", self.tahun_terbit)
        print("Status :", self.status)
        print("Peminjam :", self.peminjam)
        print("----------------------")

    def pinjam_buku(self, nama):
        self.status = "Dipinjam"
        self.peminjam = nama

    def kembalikan_buku(self):
        self.status = "Tersedia"
        self.peminjam = "-"


# Kelas Anggota
class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota

    def pinjam(self, buku):
        buku.pinjam_buku(self.nama)
        print(self.nama, "meminjam", buku.judul)

    def kembalikan(self, buku):
        buku.kembalikan_buku()
        print(self.nama, "mengembalikan", buku.judul)


# Kelas Perpustakaan
class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_buku(self):
        for buku in self.daftar_buku:
            buku.tampil_info()


# Program Utama

# Membuat 3 buku
buku1 = Buku("Pemrograman Python", "Andi", 2022)
buku2 = Buku("Basis Data", "Budi", 2021)
buku3 = Buku("Jaringan Komputer", "Candra", 2020)

# Membuat 3 anggota
anggota1 = Anggota("Budi", "A01")
anggota2 = Anggota("Ani", "A02")
anggota3 = Anggota("Rudi", "A03")

# Membuat perpustakaan
perpus = Perpustakaan()

# Menambah buku
perpus.tambah_buku(buku1)
perpus.tambah_buku(buku2)
perpus.tambah_buku(buku3)

print("Daftar Buku:")
perpus.tampilkan_buku()


# Semua anggota meminjam buku
anggota1.pinjam(buku1)
anggota2.pinjam(buku2)
anggota3.pinjam(buku3)


print("Setelah Dipinjam:")
perpus.tampilkan_buku()