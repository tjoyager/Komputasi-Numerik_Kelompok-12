# Algoritma Metode Regula Falsi

### Alur Pengerjaan Metode Falsi

1. 

### Code (Python)

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

1. Persiapan dan Pembuatan Antarmuka (GUI)

Program menggunakan pustaka tkinter untuk membuat antarmuka pengguna (GUI).
Program menyiapkan kolom input agar pengguna bisa memasukkan:
Fungsi matematika f(x).
Batas bawah x1 dan batas atas x2.
Jumlah batas iterasi maksimum.
Program juga menyiapkan sebuah tabel (Treeview) untuk menampilkan proses hitungan per iterasi, dan sebuah tombol "Hitung" untuk memulai perhitungan.
2. Pengambilan dan Validasi Input (Fungsi regula_falsi)

Saat tombol "Hitung" ditekan, program mengambil nilai dari semua kolom input.
Input fungsi matematika (dalam bentuk teks/string) dikonversi menjadi fungsi Python yang bisa dieksekusi (dihitung) menggunakan fungsi eval().
Validasi Perubahan Tanda: Program mengecek apakah f(x1) * f(x2) > 0. Jika hasilnya positif (keduanya memiliki tanda yang sama, misalnya sama-sama positif atau negatif), program akan menampilkan pesan error "Tidak ada perubahan tanda!". Artinya, tidak ada jaminan akar berada di antara rentang x1 dan x2 tersebut.
Validasi Pembagian Nol: Program mengecek apakah f(x1) == f(x2). Jika sama, program akan berhenti dan menampilkan error untuk mencegah pembagian dengan nol pada rumus Regula Falsi di tahap selanjutnya.
3. Proses Iterasi Metode Regula Falsi

Program membersihkan tabel GUI dari hasil perhitungan sebelumnya (jika ada).
Program memulai perulangan (looping) sebanyak jumlah iterasi yang diinputkan pengguna.
Di dalam perulangan, program menghitung perkiraan akar baru (xr) menggunakan rumus Regula Falsi: $$xr = x2 - \frac{f(x2) \cdot (x1 - x2)}{f(x1) - f(x2)}$$
Program kemudian menghitung nilai fungsi pada titik xr tersebut, yaitu f(xr).
Perhitungan Error: Program menghitung persentase error relatif semu (berdasarkan selisih xr sekarang dengan xr pada iterasi sebelumnya). Pada iterasi pertama, error diberi tanda "-" karena belum ada nilai sebelumnya untuk dibandingkan.
Hasil iterasi saat ini (Iterasi ke-i, nilai xr, nilai f(xr), dan nilai Error) dimasukkan ke dalam tabel GUI.
Pembaruan Batas (Update Interval): Program mengecek posisi akar selanjutnya dengan mengalikan f(x1) * f(xr):
Jika hasilnya < 0 (negatif, yang berarti ada perubahan tanda di antara x1 dan xr), maka batas atas yang baru bergeser menjadi xr (x2 = xr).
Jika tidak, maka batas bawah yang baru bergeser menjadi xr (x1 = xr).
4. Menampilkan Hasil Akhir

Setelah perulangan selesai, program akan memperbarui label hasil di bawah tabel untuk menampilkan estimasi nilai akar terakhir (Akar ≈ xr).
5. Visualisasi Grafik (Plotting)

Program menggunakan pustaka matplotlib untuk menggambar grafik fungsi f(x) di sekitar area pencarian awal (x1 hingga x2).
Program menggambar garis horizontal pada y = 0 (sumbu x).
Titik estimasi akar terakhir (xr, f(xr)) ditandai secara khusus dengan titik berwarna merah.
Grafik ini kemudian ditampilkan ke layar pada jendela baru.
6. Penanganan Error (Exception Handling)

Seluruh proses perhitungan dibungkus menggunakan blok try...except.
Jika pengguna memasukkan format angka atau fungsi matematika yang salah (misalnya, memasukkan huruf pada kolom batas x1), program tidak akan crash, melainkan akan menangkap kesalahan tersebut dan memunculkan pop-up error "Input tidak valid!".