# Module di phyton

Module pada Python adalah sebuah file yang berisikan sekumpulan kode fungsi, class dan variabel yang disimpan dalam satu file berekstensi .py dan dapat dieksekusi oleh interpreter Python. Nama dari module .py merupakan nama nama dari file itu sendiri. Misalkan kita memiliki file bernama "dqlab.py", maka kita telah membuat sebuah module bernama "dqlab. Dan module sendiri bisa memiliki berbagai macam isi, baik itu fungsi, class, maupun variabel.

## 6.1. More on Modules¶
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya saat pertama kali modul diimpor ke suatu tempat.

Setiap modul memiliki tabel simbol pribadinya sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, pembuat modul dapat menggunakan variabel global dalam modul tanpa mengkhawatirkan bentrokan yang tidak disengaja dengan variabel global pengguna. Di sisi lain, jika Anda tahu apa yang Anda lakukan, Anda dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke fungsinya, modname.itemname.

Modul dapat mengimpor modul lain. Merupakan kebiasaan tetapi tidak diharuskan untuk menempatkan semua importpernyataan di awal modul (atau skrip, dalam hal ini). Nama modul yang diimpor ditempatkan di tabel simbol global modul pengimpor.

## 6.2. Standard Modules

Dalam Python, Modul hanyalah file dengan ekstensi ".py" yang berisi kode Python yang dapat diimpor ke dalam Program Python lain.

Secara sederhana, kita dapat menganggap modul sama dengan pustaka kode atau file yang berisi sekumpulan fungsi yang ingin Anda sertakan dalam aplikasi Anda.

Dengan bantuan modul, kita dapat mengatur fungsi terkait, kelas, atau blok kode apa pun dalam file yang sama. Jadi, Ini dianggap sebagai praktik terbaik saat menulis kode yang lebih besar untuk proyek tingkat produksi di Ilmu Data adalah dengan membagi blok kode Python besar menjadi  modul  yang berisi hingga 300–400 baris kode.

## 6.3. The dir() Function

Fungsi dir()mengembalikan semua properti dan metode dari objek yang ditentukan, tanpa nilai.

Fungsi ini akan mengembalikan semua properti dan metode, bahkan properti bawaan yang merupakan default untuk semua objek.

## 6.4. Packages
Paket pada dasarnya adalah direktori dengan file Python dan file dengan nama __init__.py. Ini berarti bahwa setiap direktori di dalam jalur Python, yang berisi file bernama __init__.py, akan diperlakukan sebagai paket oleh Python. Dimungkinkan untuk memasukkan beberapa modul ke dalam Paket.

Paket adalah cara untuk menyusun ruang nama modul Python dengan menggunakan "nama modul bertitik". AB adalah singkatan dari submodule bernama B dalam sebuah paket bernama A. Dua paket yang berbeda seperti P1 dan P2 keduanya dapat memiliki modul dengan nama yang sama, katakanlah A, misalnya. Submodul A dari paket P1 dan submodul A dari paket P2 bisa sangat berbeda. Paket diimpor seperti modul "normal". Kita akan memulai bab ini dengan contoh sederhana.

