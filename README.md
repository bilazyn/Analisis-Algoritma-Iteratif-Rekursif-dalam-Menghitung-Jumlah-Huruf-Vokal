**Algoritma Rekursif & Iteratif dalam Menghitung Jumlah Huruf Vokal**

Tugas Besar AKA - Kelompok 8
- Nabila Zain (103112400137)
- Devi Rahmawati - 103112400088
- Rizky Iffat Venardi - 2311102301

**Study Case:**
Studi kasus ini berfokus pada perbandingan algoritma rekursif dan iteratif dalam menghitung jumlah huruf vokal (a, i, u, e, o) pada sebuah kalimat. 
Input yang digunakan berupa kalimat, dimana nilai n didefinisikan sebagai panjang kalimat (jumlah karakter). Model ini bertujuan untuk :
- Menganalisis perbedaan waktu eksekusi antara algoritma iteratif dan rekursif.
- Mengamati pengaruh ukuran input (panjang kalimat) terhadap performa algoritma.
- Menampilkan hasil analisis dalam bentuk tabel dan grafik.

**Analysis & Result**
Berdasarkan hasil pengujian yang dilakukan, diperoleh bahwa kedua algoritma, baik rekursif maupun iteratif, mampu menghasilkan jumlah huruf vokal yang sama untuk setiap kalimat yang diuji. 
Namun, terdapat perbedaan pada waktu eksekusi. Pada kalimat dengan panjang pendek, perbedaan waktu antara algoritma rekursif dan iteratif tidak terlalu signifikan. 
Akan tetapi, seiring dengan bertambahnya panjang kalimat (nilai n semakin besar), waktu eksekusi algoritma rekursif cenderung lebih besar dibandingkan algoritma iteratif.
Hal ini disebabkan oleh:
- Pemanggilan fungsi berulang pada metode rekursif
- Adanya overhead stack pada setiap pemanggilan rekursif
Sementara itu, algoritma iteratif hanya menggunakan satu proses perulangan sehingga lebih efisien dalam penggunaan waktu dan memori.

**Conclusion**
Berdasarkan hasil analisis dan pengujian yang telah dilakukan, dapat disimpulkan bahwa:
- Algoritma rekursif dan iteratif sama-sama dapat digunakan untuk menghitung jumlah huruf vokal dalam sebuah kalimat.
- Untuk input dengan ukuran kecil, kedua algoritma memiliki waktu eksekusi yang relatif mirip.
- Untuk input dengan ukuran yang lebih besar, algoritma iteratif lebih efisien dibandingkan algoritma rekursif.
Dengan demikian, algoritma iteratif lebih disarankan untuk digunakan pada data berukuran besar karena memiliki efisiensi waktu yang lebih baik.
