from abc import ABC, abstractmethod
import hashlib


# =========================================
# Superclass / Abstract Class
# =========================================
class HashAlgorithm(ABC):

    @abstractmethod
    def hash(self, text: str) -> str:
        pass


# =========================================
# Subtype MD5
# =========================================
class MD5Hash(HashAlgorithm):

    def hash(self, text: str) -> str:
        return hashlib.md5(text.encode()).hexdigest()


# =========================================
# Subtype SHA1
# =========================================
class SHA1Hash(HashAlgorithm):

    def hash(self, text: str) -> str:
        return hashlib.sha1(text.encode()).hexdigest()


# =========================================
# Subtype SHA256
# =========================================
class SHA256Hash(HashAlgorithm):

    def hash(self, text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()


# =========================================
# Subtype SHA512
# =========================================
class SHA512Hash(HashAlgorithm):

    def hash(self, text: str) -> str:
        return hashlib.sha512(text.encode()).hexdigest()


# =========================================
# Manager Class
# =========================================
class HashManager:

    def __init__(self, algorithm: HashAlgorithm):
        self.algorithm = algorithm

    def set_algorithm(self, algorithm: HashAlgorithm):
        self.algorithm = algorithm

    def generate_hash(self, text: str) -> str:
        return self.algorithm.hash(text)


# =========================================
# Program Utama
# =========================================
def main():

    print("===== PROGRAM HASH STRING =====")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA512")

    pilihan = input("Pilih algoritma hash: ")
    text = input("Masukkan text: ")

    # Polymorphism & Subtyping
    if pilihan == "1":
        algo = MD5Hash()

    elif pilihan == "2":
        algo = SHA1Hash()

    elif pilihan == "3":
        algo = SHA256Hash()

    elif pilihan == "4":
        algo = SHA512Hash()

    else:
        print("Pilihan tidak valid!")
        return

    # Object manager menerima subtype HashAlgorithm
    manager = HashManager(algo)

    hasil = manager.generate_hash(text)

    print("\n===== HASIL HASH =====")
    print("Text Asli :", text)
    print("Hash      :", hasil)


# Menjalankan program
main()