# Penanganan Error dan Exception
Error dalam PHP terjadi ketika ada sesuatu yang salah dalam kode PHP. 
Contoh error bisa seperti titik koma yang hilang, atau serumit memanggil variabel yang salah.
Untuk menyelesaikan masalah PHP secara efisien dalam skrip, kita harus memahami error seperti apa yang terjadi.

## Syntax Errors
Syntax error bisa disamakan dengan kesalahan tata bahasa atau gramatika. Contoh kesalahan yang termasuk dalam kategori ini adalah menuliskan perintah yang sebenarnya tidak ada, lupa menuliskan tanda kurung kotak, tanda kurung bulat dan titik koma, serta salah mengeja variabel.

## Exceptions
Exception adalah suatu kondisi abnormal yang terjadi pada saat menjalankan program. 
Karena dalam java segala sesuatu merupakan objek, maka exception juga direpresentasikan 
dalam sebuah objek yang menjelaskan tentang exception tersebut.

## Handling Exceptions
Handling Exceptions merupakan mekanisme yang paling diperlukan dalam menangani error yang terjadi pada saat runtime (program berjalan) atau yang lebih dikenal dengan sebutan runtime error. 
Secara umum, adanya kesalahan / error yang terjadi pada program pada saat runtime dapat menyebabkan program berhenti atau hang

## Raising Exceptions
Sebagai pengembang Python, 
kita dapat memilih untuk memberikan exception jika suatu kondisi terjadi.
Untuk melempar (or raise) exception, gunakan kata kunci raise.
Kita dapat menentukan jenis error yang harus raise, 
dan teks yang akan dicetak kepada pengguna.

## Exception Chaining
Exception chaining, atau exception wrapping adalah 
teknik pemrograman berorientasi objek untuk menangani exception dengan re-throw
exception yang tertangkap setelah wrap di dalam exception baru.

## User-defined Exceptions
User defined exceptions dalam python dibuat oleh programmer untuk menegakkan batasan pada value
yang dapat diambil oleh variabel dalam program.
Python memiliki banyak exception 
bawaan yang dinaikkan ketika ada beberapa kesalahan dalam program.
