Tugas Praktikum #2

Deskripsi soal:
    Salah satu kelemahan dari metode Trapezoidal adalah kita harus menggunakan jumlah interval yang besar untuk memperoleh akurasi yang diharapkan. Buatlah sebuah program komputer untuk menjelaskan bagaimana metode Integrasi Romberg dapat mengatasi kelemahan tersebut. Rancanglah user interface sedemikian rupa hingga pengguna dapat mudah menginputkan persamaan/fungsi yang akan dicari nilai hasil integrasinya.

Komponen penilaian dari tugas praktikum ini:
    1. Kebenaran algoritma dan output
    2. Fitur yang memudahkan pengguna & meningkatkan fleksibilitas program
    3. Tidak terindikasi plagiarisme dengan kelompok lain

Tools:
Bahasa: python

Pembagian Tugas (GUI Edition):

A. Farrel Marvellino Sugianto (GUI Architect & User Interface)
   - Merancang layout utama menggunakan `tkinter` dan `ttk` (Entry, Button, Labels).
   - Mengimplementasikan `ttk.Treeview` untuk menampilkan tabel Romberg secara dinamis dan rapi.
   - Menangani event handler untuk tombol "Hitung" dan manajemen jendela (root, geometry, styles).
   - Validasi input GUI: Memastikan input fungsi, batas (a, b), iterasi, dan toleransi tidak kosong dan valid.

B. Ferdyan Dimas Satria (Math Engine & Data Visualization)
   - Implementasi dasar integrasi: Aturan Trapezoidal tunggal dan rekursif.
   - Implementasi Visualisasi: Menggunakan `matplotlib` untuk memplot fungsi $f(x)$ dalam rentang $[a, b]$.
   - Fitur Shading: Memberikan efek arsiran (fill_between) pada area di bawah kurva untuk memvisualisasikan area yang diintegrasikan.
   - Integrasi plot matplotlib ke dalam jendela tkinter (menggunakan FigureCanvasTkAgg jika diperlukan atau window terpisah).

C. Hadryan Rizky Dimas Saputra (Romberg Logic & Controller)
   - Implementasi Algoritma Romberg: Richardson Extrapolation untuk memperbaiki akurasi.
   - Data Controller: Mengolah input string dari GUI (menggunakan `sympy` atau `eval` dengan aman) menjadi nilai numerik.
   - Formatting Result: Mengonversi matriks hasil Romberg menjadi format list/tuple yang siap dimasukkan ke dalam `Treeview` oleh Farrel.
   - Error Handling: Menangani kesalahan matematis (seperti pembagian nol atau fungsi yang tidak terdefinisi di rentang tertentu) dengan `messagebox`.