# I/O

I/O atau nit input adalah (masukan) unit luar yang digunakan untuk memasukkan data dari luar ke dalam mikroprosesor ini, contohnya data yang berasal dari keyboard atau mouse. Sementara unit output (keluaran) biasanya digunakan untuk menampilkan data, atau dengan kata lain untuk menangkap data yang dikirimkan oleh mikroprosesor, contohnya data yang akan ditampilkan pada layar monitor komputer atau printer.

Bagian input (masukan) dan juga keluaran (output) ini juga memerlukan sinyal kontrol, antara lain untuk membaca I/O (Input/Ouput Read, IOR) dan untuk tulis I/O (Input/Output Write, IOW).

## Fancier Output Formatting
Ada beberapa cara untuk menyajikan output dari sebuah program. Data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang, atau bahkan dalam beberapa bentuk tertentu lainnya. Pengguna sering menginginkan lebih banyak kontrol atas pemformatan output daripada hanya mencetak nilai yang dipisahkan ruang. Ada beberapa cara untuk memformat output. 

Memformat output menggunakan String modulo operator(%) : 
Operator % juga dapat digunakan untuk pemformatan string. Ini menafsirkan argumen kiri seperti format printf () -style seperti dalam string bahasa C yang akan diterapkan ke argumen yang tepat. Dalam Python, tidak ada fungsi printf() tetapi fungsi printf kuno terkandung dalam Python. Untuk tujuan ini, operator modulo % kelebihan beban oleh kelas string untuk melakukan pemformatan string. Oleh karena itu, sering disebut string modulo (atau kadang-kadang bahkan disebut modulus) operator. 

Operator modulo string (% ) masih tersedia dalam Python (3.x) dan banyak digunakan. Tetapi saat ini gaya pemformatan lama dihapus dari bahasa. 

## Reading and Writing Files
Salah satu masalah yang sering ditemui ketika bekerja dengan data file adalah representasi dari garis baru atau garis akhir. Garis akhir memiliki akar dari kembali di era Kode Morse, ketika pro-tanda tertentu digunakan untuk mengkomunikasikan akhir transmisi atau akhir dari garis.

Kemudian, ini distandarisasi untuk teleprinter oleh Organisasi Internasional untuk Standardisasi (ISO) dan American Standards Association (ASA). Standar ASA menyatakan bahwa akhiran baris harus menggunakan urutan Carriage Return (CR atau r) dan karakter Line Feed (LF atau n) (CR +LF atau rn). Namun standar ISO memungkinkan untuk karakter CR + LF atau hanya karakter LF.