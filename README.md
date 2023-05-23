# Book_Agreegation_Alwi
# Manajemen Toko Buku

Program ini merupakan contoh implementasi sederhana untuk manajemen toko buku. Program ini menggunakan konsep Aggregation dengan dua kelas utama yaitu Book (Buku) dan Bookstore (Toko Buku). Setiap objek Bookstore akan memiliki beberapa objek Book yang merupakan daftar buku yang tersedia di toko tersebut.

## Kelas Book

Kelas Book memiliki atribut-atribut berikut:

- title (string): judul buku.
- author (string): penulis buku.
- price (float): harga buku.

## Kelas Bookstore

Kelas Bookstore memiliki atribut-atribut berikut:

- name (string): nama toko buku.
- books (list): daftar objek Book yang tersedia di toko.

Selain itu, kelas Bookstore memiliki metode-metode berikut:

- add_book(book): untuk menambahkan buku baru ke dalam daftar buku toko.
- display_books(): untuk menampilkan daftar buku yang tersedia beserta informasi detailnya, seperti judul, penulis, dan harga.

## Cara Menggunakan Program

Berikut adalah langkah-langkah untuk menggunakan program ini:

1. Buat objek Bookstore dengan nama toko buku menggunakan konstruktor Bookstore("Toko Buku ALWI").

2. Program akan meminta Anda untuk memasukkan data buku secara manual. Anda akan diminta untuk memasukkan judul buku, nama penulis, dan harga buku. Jika Anda ingin menghentikan memasukkan buku, cukup tekan Enter tanpa mengisi judul buku.

3. Setelah selesai memasukkan data buku, program akan menampilkan daftar buku yang tersedia di Bookstore menggunakan metode display_books().


