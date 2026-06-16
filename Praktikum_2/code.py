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
    # TODO: Implementasikan logika Romberg yang sudah kita diskusikan
    # Pastikan mengembalikan data yang bisa dibaca oleh Treeview
    pass

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
            
        # 2. Parsing fungsi string menjadi callable (Bagian C)
        
        # 3. Jalankan Integrasi Romberg (Bagian C)

        # 4. Update Treeview (Bagian A)

        # 5. Update Plot (Bagian B)
        
        messagebox.showinfo("Info", "Input tervalidasi. Menunggu penyelesaian fungsi Romberg (Bagian C).")
        
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

    # --- Panel Input (Kiri) ---
    left_frame = ttk.Frame(root, width=250)
    left_frame.pack(side="left", fill="y", padx=10, pady=10)
    left_frame.pack_propagate(False)

    input_frame = ttk.LabelFrame(left_frame, text=" Input Parameter ")
    input_frame.pack(fill="x", pady=5)

    input_frame.columnconfigure(1, weight=1)

    # TODO: Tambahkan Entry untuk f(x), a, b, max_iter, tol
    # Contoh:
    # tk.Label(input_frame, text="f(x):").grid(row=0, column=0, sticky="w")
    # entry_f = ttk.Entry(input_frame)
    # entry_f.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(input_frame, text="Fungsi f(x):").grid(row=0, column=0, sticky="w", padx=5, pady=8)
    entry_f = ttk.Entry(input_frame)
    entry_f.insert(0, "sin(x)")
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
    # TODO: Konfigurasi kolom Treeview untuk R(k,0), R(k,1), dst.
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
    # plot_frame = ttk.Frame(right_frame)
    # plot_frame.pack(side="bottom", fill="both", expand=True)
    plot_frame = ttk.LabelFrame(paned_window, text=" Visualisasi Area Integrasi ")
    paned_window.add(plot_frame, weight=2)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
