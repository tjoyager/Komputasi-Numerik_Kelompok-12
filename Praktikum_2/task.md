Tugas Praktikum #2

Deskripsi soal:
    Salah satu kelemahan dari metode Trapezoidal adalah kita harus menggunakan jumlah interval yang besar untuk memperoleh akurasi yang diharapkan. Buatlah sebuah program komputer untuk menjelaskan bagaimana metode Integrasi Romberg dapat mengatasi kelemahan tersebut. Rancanglah user interface sedemikian rupa hingga pengguna dapat mudah menginputkan persamaan/fungsi yang akan dicari nilai hasil integrasinya.

Komponen penilaian dari tugas praktikum ini:
    1. Kebenaran algoritma dan output
    2. Fitur yang memudahkan pengguna & meningkatkan fleksibilitas program
    3. Tidak terindikasi plagiarisme dengan kelompok lain

Tools:
Bahasa: python

Pembagian Tugas:
A. Farrel Marvellino Sugianto (UI, Parser, & Output Visualization)
   - Implementasi modul input yang fleksibel: Memungkinkan pengguna memasukkan fungsi matematika dalam bentuk string (menggunakan library seperti sympy).
   - Validasi Input: Memastikan batas integrasi (a, b) dan jumlah iterasi awal adalah valid.
   - Visualisasi Output: Membuat fungsi untuk mencetak "Romberg Table" ke terminal dengan format yang rapi dan mudah dibaca.
   - Penjelasan Program: Menambahkan narasi di dalam program yang menjelaskan keunggulan Romberg dibandingkan Trapezoidal biasa berdasarkan hasil output.

B. Ferdyan Dimas Satria (Base Trapezoidal Implementation)
   - Implementasi Aturan Trapezoidal: Membuat fungsi dasar untuk menghitung integral dengan metode Trapezoidal.
   - Optimasi Kolom Pertama (R[k,0]): Menggunakan metode rekursif trapezoidal untuk efisiensi perhitungan (menghitung nilai baru hanya pada titik-titik tengah baru).
   - Struktur Data: Merancang matriks atau array dua dimensi untuk menampung nilai-nilai integrasi Romberg.

C. Hadryan Rizky Dimas Saputra (Romberg Core & Extrapolation Logic)
   - Implementasi Richardson Extrapolation: Menghitung kolom-kolom berikutnya (R[k, j]) dari tabel Romberg menggunakan rumus ekstrapolasi.
   - Kontrol Iterasi & Toleransi: Mengatur kapan iterasi harus berhenti berdasarkan nilai toleransi error yang diinginkan atau batas maksimum iterasi.
   - Logika Perbandingan: Mengintegrasikan hasil dari Ferdyan dan menerapkan logika perbaikan akurasi secara bertahap hingga mencapai nilai optimal.