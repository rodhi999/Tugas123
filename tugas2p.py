# Kelas Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def tampil(self):
        print("Judul :", self.title)
        print("Author :", self.author)
        print("ISBN :", self.isbn)
        print("Dipinjam :", self.is_borrowed)
        print("----------------------")


# Kelas Member
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []


# Kelas Staff
class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id


# Kelas BorrowTransaction
class BorrowTransaction:
    def __init__(self, book, member, staff, borrow_date):
        self.book = book
        self.member = member
        self.staff = staff
        self.borrow_date = borrow_date
        self.returned = False

    def borrow_book(self):

        self.book.borrow()

        self.member.borrowed_books.append(self.book)

        print(self.member.name, "meminjam", self.book.title)
        print("Tanggal Pinjam:", self.borrow_date)
        print("Dilayani Staff:", self.staff.name)
        print("----------------------")


    def return_book(self):

        self.book.return_book()

        self.returned = True

        print(self.member.name, "mengembalikan", self.book.title)
        print("----------------------")


# Program Utama

print("=== DATA BUKU ===")

# 3 Buku
book1 = Book("Pemrograman Python", "Andi", "ISBN001")
book2 = Book("Basis Data", "Budi", "ISBN002")
book3 = Book("Jaringan Komputer", "Candra", "ISBN003")

book1.tampil()
book2.tampil()
book3.tampil()


print("\n=== DATA MEMBER ===")

# 3 Member
member1 = Member("Budi", "M01")
member2 = Member("Ani", "M02")
member3 = Member("Rudi", "M03")

print(member1.name, member1.member_id)
print(member2.name, member2.member_id)
print(member3.name, member3.member_id)


print("\n=== DATA STAFF ===")

# 1 Staff
staff1 = Staff("Admin", "S01")

print(staff1.name, staff1.staff_id)


print("\n=== TRANSAKSI PEMINJAMAN ===")

# 3 Transaksi
t1 = BorrowTransaction(book1, member1, staff1, "25-02-2026")
t2 = BorrowTransaction(book2, member2, staff1, "25-02-2026")
t3 = BorrowTransaction(book3, member3, staff1, "25-02-2026")

t1.borrow_book()
t2.borrow_book()
t3.borrow_book()


print("\n=== STATUS BUKU SETELAH DIPINJAM ===")

book1.tampil()
book2.tampil()
book3.tampil()