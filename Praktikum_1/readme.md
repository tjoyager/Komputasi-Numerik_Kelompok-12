# Laporan Algoritma Metode Regula Falsi

## Kelompok 12
| NRP | Nama |
| :--- | :--- |
| 5025251018 | Farrel Marvellino Sugianto |
| 5025251034 | Ferdyan Dimas Satria |
| 5025251027 | Hadryan Rizky Dimas Saputra |

### Metode Regula Falsi

Regula Falsi adalah metode untuk mencari akar persamaaan dengan menggunakan interpolasi linear dimana kita menarik garis lurus antara titik koordinat bawah (xl, f(xl) ke batas atas (xu, f(xu))). Titik di mana garis lurus tersebut memotong sumbu X dijadikan sebagai tebakan akar baru (xr). Karena titik ini "palsu" (bukan di kurva asli), metode ini disebut False Position.

### Alur Pengerjaan Metode Falsi

1. Pilih sembarang dua titik yang akan menjadi xl dan xu. Untuk memastikan pilihan kita valid, kita harus memasukannya ke f(xl) kali f(xu) < 0 :
   - Jika hasilnya negatif, maka terdapat akar di antara interval xl dan xu, kurva telah menyeberangi sumbu x dan bisa lanjut ke langkah 2
   - Jika hasilnya positif, maka tidak ada akar di antara interval xl dan xu, kurva belum memotong sumbu x dan harus mencari titik tebakan baru
   - Jika f(xl) kali f(xu) = 0, maka batas tebakan xl atau xu itu sendiri yang merupakan nilai akar pastinya
2. Jika hasilnya negatif, maka kita bisa mencari nilai tengah atau nilai x baru(xr) menggunakan rumus :
   xr = xu - [ f(xu) * (xl - xu) / (f(xl) - f(xu))]
3. Masukan xr ke f(xr), kemudian kembali evaluasi f(xl) kali f(xr) < 0 :
   - Jika hasilnya negatif, maka akar berada di sub-interval atas/kanan. Maka batas bawah akan bergeser xl = xr
   - Jika hasilnya positif, maka akar berada di sub-interval bawah/kiri. Maka batas atas akan bergeser xu = xr
   - Jika f(Xl) kali f(Xr) = 0, maka akar sudah ditemukan yaitu xr, iterasi selesai
4. Ulangi proses, kembali ke langkah nomor 2 dengan nilai a dan b yang sudah diperbarui. Lakukan perulangan ini berulang-ulang sampai kondisi toleransi error di langkah nomor 3 terpenuhi.

### Full Code (Python)

```python
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox

def regula_falsi():
    try:
        fungsi_str = input_fungsi.get()
        x1 = float(input_x1.get())
        x2 = float(input_x2.get())
        n = int(input_iterasi.get())

        def f(x):
            return eval(fungsi_str, {"x": x, "np": np})

        if f(x1) * f(x2) > 0:
            messagebox.showerror("Error", "Tidak ada perubahan tanda!")
            return

        x1_awal = x1
        x2_awal = x2

        if f(x1) == f(x2):
            messagebox.showerror("Error", "Pembagian nol (f(x1) = f(x2))")
            return

        for row in tree.get_children():
            tree.delete(row)

        xr_old = None

        for i in range(1, n+1):
            xr = x2 - (f(x2) * (x1 - x2)) / (f(x1) - f(x2))
            fx = f(xr)

            if xr_old is None:
                error = "-"
            else:
                error = abs((xr - xr_old) / xr) * 100

            tree.insert("", "end", values=(
                i,
                f"{xr:.6f}",
                f"{fx:.6f}",
                error if error == "-" else f"{error:.6f}%"
            ))

            if f(x1) * fx < 0:
                x2 = xr
            else:
                x1 = xr

            xr_old = xr

        label_hasil.config(text=f"Akar ≈ {xr:.6f}")

        x_plot = np.linspace(x1_awal - 1, x2_awal + 1, 200)
        y_plot = [f(i) for i in x_plot]

        plt.figure(figsize=(6,4))
        plt.plot(x_plot, y_plot, label="f(x)")
        plt.axhline(0)
        plt.scatter(xr, f(xr), color='red', label="Akar")
        plt.title("Grafik Regula Falsi")
        plt.legend()
        plt.grid()
        plt.show()

    except:
        messagebox.showerror("Error", "Input tidak valid!")

root = tk.Tk()
root.title("Metode Regula Falsi")
root.geometry("750x500")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=3)
root.grid_rowconfigure(5, weight=1)

style = ttk.Style()
style.configure("Treeview", font=("Consolas", 9), rowheight=22)
style.configure("Treeview.Heading", font=("Consolas", 10, "bold"))

tk.Label(root, text="f(x):").grid(row=0, column=0, sticky="w", padx=5)
input_fungsi = tk.Entry(root)
input_fungsi.grid(row=0, column=1, sticky="ew", padx=5, pady=2)
input_fungsi.insert(0, "(1 - 0.6*x)/x")

tk.Label(root, text="x1:").grid(row=1, column=0, sticky="w", padx=5)
input_x1 = tk.Entry(root)
input_x1.grid(row=1, column=1, sticky="ew", padx=5, pady=2)
input_x1.insert(0, "1")

tk.Label(root, text="x2:").grid(row=2, column=0, sticky="w", padx=5)
input_x2 = tk.Entry(root)
input_x2.grid(row=2, column=1, sticky="ew", padx=5, pady=2)
input_x2.insert(0, "2")

tk.Label(root, text="Iterasi:").grid(row=3, column=0, sticky="w", padx=5)
input_iterasi = tk.Entry(root)
input_iterasi.grid(row=3, column=1, sticky="ew", padx=5, pady=2)
input_iterasi.insert(0, "5")

tk.Button(root, text="Hitung", command=regula_falsi)\
    .grid(row=4, column=0, columnspan=2, pady=10)

columns = ("Iterasi", "xr", "f(xr)", "Error")
tree = ttk.Treeview(root, columns=columns, show="headings", height=8)

tree.heading("Iterasi", text="Iterasi")
tree.heading("xr", text="xr")
tree.heading("f(xr)", text="f(xr)")
tree.heading("Error", text="Error")

tree.column("Iterasi", anchor="center", width=70)
tree.column("xr", anchor="center", width=130)
tree.column("f(xr)", anchor="center", width=130)
tree.column("Error", anchor="center", width=130)

tree.grid(row=5, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)

scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=5, column=2, sticky="ns")

label_hasil = tk.Label(root, text="Akar ≈ -", font=("Arial", 12, "bold"))
label_hasil.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
```

### Alur Kerja Program

1. Persiapan Antarmuka/Tampilan (GUI)
    Program membuat tampilan visual menggunakan library tkinter dengan menyediakan:
    - Kolom untuk menerima fungsi matematika `f(x)`, batas bawah (`x1`), batas atas (`x2`), dan jumlah iterasi maksimum dari user.
    - Tabel (Treeview) untuk menampilkan rincian data per iterasi dan label untuk estimasi hasil akhir.
    - Tombol `Hitung` untuk menjalankan logika perhitungan.

2. Pengambilan dan Validasi Input
    Saat tombol ditekan, fungsi `regula_falsi` menjalankan prosedur berikut:
    - Mengubah teks input `f(x)` menjadi perhitungan matematika yang dapat dihitung melalui perintah `eval()`, dengan library numpy (np).
    - Mengecek apakah `f(x1) * f(x2) > 0`. Jika iya, muncul pesan error "Tidak ada perubahan tanda!" karena secara teoritis akar tidak ada dalam rentang tersebut.
    - Memastikan `f(x1)` tidak sama dengan `f(x2)` guna menghindari kegagalan kalkulasi (pembagian dengan nol) pada rumus utama.

3. Eksekusi Iterasi Regula Falsi
    Program membersihkan data lama pada tabel dan memulai proses looping:
    - Menentukan titik potong garis lurus yang menghubungkan `f(x1)` dan `f(x2)` pada sumbu x menggunakan rumus:
    `xr = x2 - (f(x2) * (x1 - x2)) / (f(x1) - f(x2))`
    - Menghitung nilai `f(xr)` pada titik baru tersebut.
    - Menghitung persentase error relatif semu berdasarkan selisih `xr` saat ini dengan `xr` sebelumnya. Khusus iterasi pertama, nilai error ditandai dengan "-".
    - Memasukkan nomor iterasi, nilai `xr`, `f(xr)`, dan error ke dalam tabel GUI.
    - Pembaruan Batas (Update Interval): 
    a. Jika `f(x1) * f(xr) < 0`, maka batas atas (`x2`) diperbarui menjadi `xr`.
    b. Jika tidak, maka batas bawah (`x1`) diperbarui menjadi `xr`.

4. Penyajian Hasil Akhir
    Setelah seluruh iterasi selesai, program memperbarui label di bawah tabel untuk menampilkan estimasi akar terakhir secara jelas (Akar ≈ `xr`).

5. Visualisasi Grafik (Plotting)
    Program menggunakan matplotlib untuk memberikan gambaran visual:
    - Menampilkan kurva `f(x)` di area sekitar pencarian awal (`x1-1` hingga `x2+1`).
    - Menggambar sumbu x (garis horizontal y = 0) untuk melihat perpotongan.
    - Menandai titik estimasi akar terakhir (`xr`, `f(xr)`) dengan titik khusus berwarna merah.

6. Penanganan Kesalahan (Exception Handling)
    - Jika ditemukan kesalahan format, seperti memasukkan karakter non-angka pada kolom koordinat atau penulisan fungsi yang tidak dikenali Python, program tidak akan berhenti mendadak (crash).
    - Program akan menangkap error tersebut dan memunculkan pop-up peringatan "Input tidak valid!".