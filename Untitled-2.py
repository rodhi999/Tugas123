class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.status = "Tersedia"

    def tampil_info(self):
        print(f"Judul Buku: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun_terbit}")
        print(f"Status: {self.status}")

    def ubah_status(self, status_baru):
        self.status = status_baru


class Anggota:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota
        self.daftar_pinjam = []
        print(f"Anggota baru dibuat: {self.nama} (ID: {self.id_anggota})")

    def pinjam_buku(self, buku):
        if buku.status == "Tersedia":
            buku.ubah_status("Dipinjam")
            self.daftar_pinjam.append(buku)
            print(f"{self.nama} berhasil meminjam {buku.judul}")
        else:
            print("Buku sedang tidak tersedia")

    def kembalikan_buku(self, buku):
        if buku in self.daftar_pinjam:
            buku.ubah_status("Tersedia")
            self.daftar_pinjam.remove(buku)
            print(f"{self.nama} mengembalikan {buku.judul}")



class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []
        self.daftar_anggota = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def hapus_buku(self, buku):
        self.daftar_buku.remove(buku)

    def daftar_semua_buku(self):
        for buku in self.daftar_buku:
            buku.tampil_info()
            print("------------------")



buku1 = Buku("Pemrograman Python", "Adit", 2022)
anggota1 = Anggota("Upin", "A001")
perpus = Perpustakaan("Perpustakaan Kampus")

perpus.tambah_buku(buku1)
anggota1.pinjam_buku(buku1)
perpus.daftar_semua_buku()
