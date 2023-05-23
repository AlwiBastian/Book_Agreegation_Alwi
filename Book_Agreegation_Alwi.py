class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

class Bookstore:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Daftar Buku di", self.name)
        if len(self.books) == 0:
            print("Tidak ada buku yang tersedia.")
        else:
            for book in self.books:
                print("Judul:", book.title)
                print("Penulis:", book.author)
                print("Harga:", book.price)
                print()

# Membuat objek Bookstore
bookstore = Bookstore("Toko Buku ALWI")

# Memasukkan data buku secara manual
while True:
    title = input("Masukkan judul buku (Tekan Enter jika ingin stop): ")
    if title == "":
        break
    author = input("Masukkan nama penulis: ")
    price =float(input("Masukkan harga buku: "))

    book = Book(title, author, price)
    bookstore.add_book(book)

# Menampilkan daftar buku yang tersedia di Bookstore
bookstore.display_books()
