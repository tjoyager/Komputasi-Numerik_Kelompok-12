# Komputasi Numerik (D)

## Kelompok 12

| NRP | Nama | Peran |
| --- | --- | --- |
| 5025251018 | Farrel Marvellino Sugianto | Bagian A (GUI Layout & Treeview) |
| 5025251034 | Ferdyan Dimas Satria | Bagian B (Math Foundation & Visualization) |
| 5025251027 | Hadryan Rizky Dimas Saputra | Bagian C (Romberg Logic & Controller) |

### Metode Integrasi Romberg

Integrasi Romberg adalah metode numerik untuk menghitung nilai aproksimasi integral tentu dari sebuah fungsi. Metode ini menggabungkan Aturan Trapesium (Trapezoidal Rule) dengan Ekstrapolasi Richardson untuk mendapatkan hasil yang lebih presisi tanpa harus mengevaluasi fungsi pada terlalu banyak titik. Pada dasarnya, Romberg menghitung estimasi integral dengan interval pias yang terus dibagi dua, lalu mengekstrapolasi hasil-hasil tersebut untuk menghilangkan error secara sistematis dan mendapatkan akurasi tingkat tinggi (orde yang lebih tinggi).

### Alur Pengerjaan Metode Integrasi Romberg

1. Tentukan fungsi f(x), batas bawah integrasi a, batas atas integrasi b, serta kriteria penghentian berupa batas iterasi maksimum k dan nilai toleransi error.
2. Hitung nilai aproksimasi awal (iterasi k = 0) menggunakan Aturan Trapesium untuk keseluruhan interval a hingga b:
R(0,0) = [ (b - a) / 2 ] * [ f(a) + f(b) ]
3. Mulai iterasi k = 1, 2, ..., hingga batas maksimal iterasi. Untuk setiap iterasi, tentukan ukuran langkah baru h = (b - a) / (2^k) dan hitung estimasi Trapesium baru R(k,0) menggunakan pendekatan rekursif dengan memanfaatkan data sebelumnya R(k-1, 0):
R(k,0) = 0.5 * R(k-1,0) + h * Total Penjumlahan [ f(a + (2i-1)h) ]
(di mana i berjalan dari 1 hingga 2^(k-1))
4. Terapkan Ekstrapolasi Richardson untuk menghitung nilai estimasi dengan akurasi orde yang lebih tinggi pada kolom-kolom berikutnya di baris k:
R(k,j) = R(k, j-1) + [ R(k, j-1) - R(k-1, j-1) ] / [ (4^j) - 1 ]
(untuk j = 1, 2, ..., k)
5. Lakukan evaluasi toleransi error dengan membandingkan estimasi terbaik di iterasi saat ini dengan iterasi sebelumnya:
* Jika nilai absolut dari selisih R(k,k) dan R(k-1,k-1) kurang dari nilai toleransi, maka hasil sudah dianggap konvergen dan iterasi dihentikan.
* Jika tidak, kembali ke langkah 3 selama batas maksimal iterasi belum tercapai.


6. Hasil akhir integral adalah nilai R(k,k) pada iterasi terakhir yang dikalkulasikan.

### Full Code (Python)

```python
import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp

entry_f = None
entry_a = None
entry_b = None
entry_iter = None
entry_tol = None
tree = None
plot_frame = None

# =========================================================================
# BAGIAN B: Ferdyan Dimas Satria (Math Foundation & Visualization)
# =========================================================================
def initial_trapezoid(f, a, b):
    return (b - a) / 2.0 * (f(a) + f(b))


def recursive_trapezoid(f, a, b, k, prev_R):
    n = 2 ** k
    h = (b - a) / n

    jumlah_titik_baru = 2 ** (k - 1)
    sigma = 0.0
    for i in range(1, jumlah_titik_baru + 1):
        x_baru = a + (2 * i - 1) * h
        sigma += f(x_baru)

    return 0.5 * prev_R + h * sigma


def plot_graph(canvas_frame, f_str, a, b):
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    x = sp.Symbol('x')
    expr = sp.sympify(f_str)
    f_numeric = sp.lambdify(x, expr, modules=['numpy'])

    margin = (b - a) * 0.2 if b != a else 1.0
    x_vals = np.linspace(a - margin, b + margin, 400)
    y_vals = np.array(f_numeric(x_vals), dtype=float)

    fig, ax = plt.subplots(figsize=(5, 4))
    ax.plot(x_vals, y_vals, color="royalblue", linewidth=2, label=f"f(x) = {f_str}")

    x_fill = np.linspace(a, b, 200)
    y_fill = np.array(f_numeric(x_fill), dtype=float)
    ax.fill_between(x_fill, y_fill, color="skyblue", alpha=0.5, label=f"Luas [{a}, {b}]")

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title("Grafik Fungsi dan Area Integrasi")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()

    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

    return canvas


# =========================================================================
# BAGIAN C: Hadryan Rizky Dimas Saputra (Romberg Logic & Controller)
# =========================================================================
def romberg_integration(f_callable, a, b, max_iter, tol):
    """
    Logika utama Romberg (Richardson Extrapolation).
    Mengembalikan 2D list berisi tabel Romberg.
    """
    R = []
    # k = 0: Initial Trapezoid
    R0 = [initial_trapezoid(f_callable, a, b)]
    R.append(R0)
    
    for k in range(1, max_iter + 1):
        row = [0.0] * (k + 1)
        # R(k, 0): Recursive Trapezoid
        row[0] = recursive_trapezoid(f_callable, a, b, k, R[k-1][0])
        
        # R(k, j): Richardson Extrapolation
        for j in range(1, k + 1):
            row[j] = row[j-1] + (row[j-1] - R[k-1][j-1]) / (4**j - 1)
        
        R.append(row)
        
        # Cek toleransi: selisih antara estimasi terbaik saat ini dan sebelumnya
        if abs(R[k][k] - R[k-1][k-1]) < tol:
            break
            
    return R

def on_calculate():
    """
    Event handler saat tombol 'Hitung' ditekan.
    """
    try:
        # 1. Ambil input dari GUI (Bagian A)
        f_str = entry_f.get()
        a_val = float(entry_a.get())
        b_val = float(entry_b.get())
        max_i = int(entry_iter.get())
        tol_val = float(entry_tol.get())

        if not f_str:
            raise ValueError("Fungsi f(x) tidak boleh kosong.")
        
        if max_i < 1:
            raise ValueError("Iterasi minimal adalah 1.")
            
        # 2. Parsing fungsi string menjadi callable (Bagian C)
        x = sp.Symbol('x')
        expr = sp.sympify(f_str)
        f_numeric = sp.lambdify(x, expr, modules=['numpy'])
        
        # 3. Jalankan Integrasi Romberg (Bagian C)
        romberg_table = romberg_integration(f_numeric, a_val, b_val, max_i, tol_val)

        # 4. Update Treeview (Bagian A)
        # Hapus data lama
        for item in tree.get_children():
            tree.delete(item)
            
        # Konfigurasi kolom secara dinamis berdasarkan hasil Romberg
        max_cols = len(romberg_table[-1])
        columns = ["k"] + [f"R(k,{j})" for j in range(max_cols)]
        tree["columns"] = columns
        
        tree.heading("k", text="k")
        tree.column("k", width=60, anchor="center", stretch=False)
        for j in range(max_cols):
            col_id = f"R(k,{j})"
            header_text = "Trapezoid" if j == 0 else f"Orde {j}"
            tree.heading(col_id, text=f"{col_id} ({header_text})")
            tree.column(col_id, width=150, anchor="center", minwidth=120)

        # Masukkan baris data
        for k, row in enumerate(romberg_table):
            display_row = [k] + [f"{val:.10f}" for val in row]
            # Isi kolom sisa dengan string kosong
            display_row += [""] * (max_cols - len(row))
            tree.insert("", "end", values=display_row)

        # 5. Update Plot (Bagian B)
        plot_graph(plot_frame, f_str, a_val, b_val)
        
        final_result = romberg_table[-1][-1]
        messagebox.showinfo("Berhasil", f"Integrasi Selesai!\nHasil Akhir: {final_result:.10f}")
        
    except ValueError as ve:
        messagebox.showerror("Kesalahan Input", f"Format input salah: {ve}")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")


# =========================================================================
# BAGIAN A: Farrel Marvellino Sugianto (GUI Layout & Treeview)
# =========================================================================
def setup_gui():
    global entry_f, entry_a, entry_b, entry_iter, entry_tol, tree, plot_frame
    
    root = tk.Tk()
    root.title("Praktikum 2: Integrasi Romberg")
    root.geometry("950x650")
    
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))
    # Tambahkan rowheight untuk mencegah teks saling bertumpuk
    style.configure("Treeview", rowheight=30, font=('Helvetica', 10))

    # --- Panel Input (Kiri) ---
    # Lebarkan frame menjadi 320 agar proporsional
    left_frame = ttk.Frame(root, width=700)
    left_frame.pack(side="left", fill="y", padx=10, pady=10)
    left_frame.pack_propagate(False)

    input_frame = ttk.LabelFrame(left_frame, text=" Input Parameter ")
    input_frame.pack(fill="x", pady=5)

    input_frame.columnconfigure(1, weight=1)

    ttk.Label(input_frame, text="Fungsi f(x):").grid(row=0, column=0, sticky="w", padx=5, pady=8)
    entry_f = ttk.Entry(input_frame)
    entry_f.insert(0, "sin(x)")
    # Ubah padx dari 50 menjadi 5 agar tidak mendorong entry terlalu ke kanan
    entry_f.grid(row=0, column=1, sticky="ew", padx=5, pady=8)

    ttk.Label(input_frame, text="Batas Bawah (a):").grid(row=1, column=0, sticky="w", padx=5, pady=8)
    entry_a = ttk.Entry(input_frame)
    entry_a.insert(0, "0")
    entry_a.grid(row=1, column=1, sticky="ew", padx=5, pady=8)

    ttk.Label(input_frame, text="Batas Atas (b):").grid(row=2, column=0, sticky="w", padx=5, pady=8)
    entry_b = ttk.Entry(input_frame)
    entry_b.insert(0, "3.14159")
    entry_b.grid(row=2, column=1, sticky="ew", padx=5, pady=8)

    ttk.Label(input_frame, text="Maks Iterasi (k):").grid(row=3, column=0, sticky="w", padx=5, pady=8)
    entry_iter = ttk.Entry(input_frame)
    entry_iter.insert(0, "5")
    entry_iter.grid(row=3, column=1, sticky="ew", padx=5, pady=8)

    ttk.Label(input_frame, text="Toleransi Error:").grid(row=4, column=0, sticky="w", padx=5, pady=8)
    entry_tol = ttk.Entry(input_frame)
    entry_tol.insert(0, "1e-6")
    entry_tol.grid(row=4, column=1, sticky="ew", padx=5, pady=8)

    btn_hitung = ttk.Button(left_frame, text="Hitung Integrasi Romberg", command=on_calculate)
    btn_hitung.pack(fill="x", pady=15, ipady=5)

    info_lbl = ttk.Label(left_frame, text="Catatan:\nGunakan format python untuk math.\nMisal: x**2 + sin(x) * exp(x)", foreground="gray", justify="left")
    info_lbl.pack(anchor="w", padx=5)

    # --- Panel Hasil & Grafik (Kanan) ---
    right_frame = ttk.Frame(root)
    right_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    paned_window = ttk.PanedWindow(right_frame, orient="vertical")
    paned_window.pack(fill="both", expand=True)

    table_frame = ttk.LabelFrame(paned_window, text=" Tabel Hasil Ekstrapolasi Romberg ")
    paned_window.add(table_frame, weight=1)
    
    tree_scroll_y = ttk.Scrollbar(table_frame, orient="vertical")
    tree_scroll_y.pack(side="right", fill="y")
    tree_scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
    tree_scroll_x.pack(side="bottom", fill="x")

    # --- Treeview untuk Tabel Romberg ---
    tree = ttk.Treeview(table_frame, show="headings", 
                        yscrollcommand=tree_scroll_y.set, 
                        xscrollcommand=tree_scroll_x.set)
    tree.pack(side="left", fill="both", expand=True)
    
    tree_scroll_y.config(command=tree.yview)
    tree_scroll_x.config(command=tree.xview)

    tree["columns"] = ("k", "R(k,0)", "R(k,1)")
    tree.heading("k", text="k (Iterasi)")
    tree.column("k", width=80, anchor="center")
    tree.heading("R(k,0)", text="R(k,0) Trapezoid")
    tree.column("R(k,0)", width=150, anchor="center")
    tree.heading("R(k,1)", text="R(k,1)")
    tree.column("R(k,1)", width=150, anchor="center")

    # --- Canvas untuk Matplotlib ---
    plot_frame = ttk.LabelFrame(paned_window, text=" Visualisasi Area Integrasi ")
    paned_window.add(plot_frame, weight=2)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()

```

### Screenshot Hasil Program

Hasil kalkulasi program untuk mencari nilai luasan (integral) dari fungsi f(x) = sin(x), dengan batas bawah a = 0, batas atas b = 3.14159, maksimal iterasi 5, dan toleransi 1e-6:


### Alur Kerja Program

1. **Persiapan Antarmuka/Tampilan (GUI)**
Program membangkitkan antarmuka menggunakan library tkinter. Area antarmuka dibagi menjadi dua:
* Panel Input di kiri untuk menerima persamaan matematika fungsi, batas integrasi bawah dan atas, jumlah iterasi maksimum, serta toleransi.
* Panel Output di kanan berupa tabel dinamis Treeview untuk rincian tabel Romberg dan panel visualisasi grafik area bawah kurva.


2. **Pengambilan dan Parsing Input (SymPy)**
Saat user menekan tombol Hitung, teks dari kolom fungsi diproses menggunakan fungsi dari library SymPy. Ini memungkinkan pembacaan ekspresi aljabar dalam bentuk string menjadi fungsi numerik standar yang dapat dihitung oleh pustaka NumPy.
3. **Eksekusi Integrasi Romberg (Math Logic)**
Program menghapus data lama pada tabel lalu menjalankan inti algoritma:
* Evaluasi nilai trapesium awal untuk iterasi 0 menggunakan batas a dan b.
* Iterasi secara terus menerus membelah ukuran partisi sambil menyimpan setiap kalkulasi dalam matriks 2D bernama R.
* Menggunakan relasi Ekstrapolasi Richardson pada setiap baris untuk menghitung titik-titik matriks hingga diagonal utama matriks R.
* Proses ini akan berhenti lebih awal jika persyaratan error terpenuhi (selisih mutlak aproksimasi trapesium dengan estimasi orde tertinggi berada di bawah nilai toleransi input).


4. **Penyajian Tabel Hasil**
Kolom tabel akan secara dinamis ditambahkan dan disesuaikan ukurannya bergantung pada ukuran matriks hasil integrasi Romberg. Tabel lalu diisi dengan nilai-nilai dari matriks dengan akurasi 10 angka di belakang koma. Jika hasil akhir tercapai, pop-up messagebox akan memunculkan nilai Integral akhir yang dicari.
5. **Visualisasi Grafik (Plotting area dengan Matplotlib)**
Fungsi ini menghitung larik sumbu-x lalu memetakannya pada sumbu-y untuk menggambar garis kurva f(x). Program kemudian mengarsir (memberi warna shading biru muda) pada ruang antara sumbu-x dengan fungsi matematika untuk memvisualisasikan luas area di bawah kurva dari nilai integrasi tertentu di batas spesifik. Grafik tersebut kemudian dimunculkan ke dalam kanvas GUI.
6. **Penanganan Kesalahan (Exception Handling)**
Apabila terdapat nilai yang tidak dapat diselesaikan atau input yang dibiarkan kosong, fungsi try-except dalam Python akan menangkap permasalahan tersebut. Akan ada notifikasi error "Kesalahan Input" untuk menghindari berhentinya paksa atau *crash* pada program.

### Screenshot Hasil Program dengan Contoh Lain

Fungsi x^2
Batas a = 0, Batas b = 2, Iterasi = 5
![Alt Text](https://github.com/tjoyager/Komputasi-Numerik_Kelompok-12/blob/5b9bfe0bd80acd4815289cd22db9697d4d6a4be3/Praktikum_2/files/Screenshot%202026-06-19%20122506.png)

Fungsi (exp(x))
Batas a = 0, Batas b = 1, Iterasi = 5
![Alt Text](https://github.com/tjoyager/Komputasi-Numerik_Kelompok-12/blob/5b9bfe0bd80acd4815289cd22db9697d4d6a4be3/Praktikum_2/files/Screenshot%202026-06-19%20123328.png)

Fungsi x^3 - 4x + 5
Batas a = -1, Batas b = 3, Iterasi = 5
![Alt Text](https://github.com/tjoyager/Komputasi-Numerik_Kelompok-12/blob/5b9bfe0bd80acd4815289cd22db9697d4d6a4be3/Praktikum_2/files/Screenshot%202026-06-19%20123439.png)
