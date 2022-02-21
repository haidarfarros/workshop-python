<b>4.1 if Statement</b><p>
Pengambilan keputusan (kondisi if) digunakan untuk mengantisipasi kondisi yang terjadi saat jalanya program dan menentukan tindakan apa yang akan diambil sesuai dengan kondisi.

Pada python ada beberapa statement/kondisi diantaranya adalah if, else dan elif Kondisi if digunakan untuk mengeksekusi kode jika kondisi bernilai benar True.

Jika kondisi bernilai salah False maka statement/kondisi if tidak akan di-eksekusi.

#Kondisi if adalah kondisi yang akan dieksekusi oleh program jika bernilai benar atau TRUE

nilai = 9

#jika kondisi benar/TRUE maka program akan mengeksekusi perintah dibawahnya
if(nilai > 7):
    print("Sembilan Lebih Besar Dari Angka Tujuh") # Kondisi Benar, Dieksekusi

#jika kondisi salah/FALSE maka program tidak akan mengeksekusi perintah dibawahnya
if(nilai > 10):
    print("Sembilan Lebih Besar Dari Angka Sepuluh") # Kondisi Salah, Maka tidak tereksekusi

Dari contoh diatas, jika program dijalankan maka akan mencetak string "Sembilan Lebih Besar Dari Angka Tujuh" sebanyak 1 kali yaitu pada if pertama. Di if kedua statement bernilai salah, jadi perintah print("Sembilan Lebih Besar Dari Angka Sepuluh") tidak akan dieksekusi.

<b>4.2 for Statement</b><p>
untuk loop digunakan ketika Anda memiliki blok kode yang ingin Anda ulangi beberapa kali. For-loop selalu digunakan dalam kombinasi dengan objek yang dapat diusasikan, seperti daftar atau rentang. Python untuk pernyataan iterasi atas anggota urutan secara berurutan, mengeksekusi blok setiap kali.

<b>4.3 The range() Function</b><p>
Range() adalah fungsi bawaan di Python. Ini mengembalikan urutan angka mulai dari nol dan bertambah 1 secara default dan berhenti sebelum angka yang diberikan. ... langkah: Ini juga merupakan parameter opsional yang digunakan untuk menentukan kenaikan pada setiap iterasi; secara default, nilainya adalah satu.

<b>4.4 break and continue Statements, and else Clauses on Loops</b><p>
break statement keluar dari penutup terdalam untuk loop. break statement yang dijalankan di suite pertama mengakhiri loop tanpa menjalankan suite klausa lainnya. break statement digunakan untuk mengakhiri eksekusi loop for atau sementara loop, dan kontrol masuk ke pernyataan setelah badan loop for.
continue statement dengan iterasi loop berikutnya. continue statement yang dijalankan di suite pertama melewati sisa suite dan melanjutkan dengan item berikutnya atau dengan klausa lainnya, jika tidak ada item berikutnya.
Loop statement mungkin memiliki klausa lain. Ini dijalankan ketika loop untuk berakhir melalui kelelahan yang dapat diusala - tetapi tidak ketika loop diakhiri dengan pernyataan istirahat.

<b>4.5 pass Statement</b><p>
pass adalah pernyataan nol. Penerjemah tidak mengabaikan pernyataan lulus, tetapi tidak ada yang terjadi dan pernyataan itu tidak berlaku. Pernyataan lulus berguna ketika Anda tidak menulis implementasi fungsi tetapi Anda ingin menerapkannya di masa depan.

<b>4.6 match Statement</b><p>
match statement mengambil ekspresi dan membandingkan nilainya dengan pola berturut-turut yang diberikan sebagai satu atau lebih blok kasus. Ini secara dangkal mirip dengan pernyataan switch di C, Java atau JavaScript (dan banyak bahasa lainnya), tetapi juga dapat mengekstrak komponen (elemen urutan atau atribut objek) dari nilai ke dalam variabel.

<b>4.7 Defining Functions<p></b>
Fungsi adalah blok kode yang hanya berjalan ketika dipanggil. Anda dapat meneruskan data, yang dikenal sebagai parameter, ke dalam fungsi. Fungsi dapat mengembalikan data sebagai hasilnya.