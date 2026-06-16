import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp

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
        # 2. Parsing fungsi string menjadi callable (Bagian C)
        # 3. Jalankan Integrasi Romberg (Bagian C)
        # 4. Update Treeview (Bagian A)
        # 5. Update Plot (Bagian B)
        pass
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan: {e}")


# =========================================================================
# BAGIAN A: Farrel Marvellino Sugianto (GUI Layout & Treeview)
# =========================================================================
def setup_gui():
    root = tk.Tk()
    root.title("Praktikum 2: Integrasi Romberg")
    root.geometry("900x600")

    # --- Panel Input (Kiri) ---
    input_frame = ttk.LabelFrame(root, text=" Input Parameter ")
    input_frame.pack(side="left", fill="y", padx=10, pady=10)

    # TODO: Tambahkan Entry untuk f(x), a, b, max_iter, tol
    # Contoh:
    # tk.Label(input_frame, text="f(x):").grid(row=0, column=0, sticky="w")
    # entry_f = ttk.Entry(input_frame)
    # entry_f.grid(row=0, column=1, padx=5, pady=5)

    btn_hitung = ttk.Button(input_frame, text="Hitung Integrasi", command=on_calculate)
    btn_hitung.pack(pady=20)

    # --- Panel Hasil & Grafik (Kanan) ---
    right_frame = ttk.Frame(root)
    right_frame.pack(side="right", expand=True, fill="both", padx=10, pady=10)

    # --- Treeview untuk Tabel Romberg ---
    # TODO: Konfigurasi kolom Treeview untuk R(k,0), R(k,1), dst.
    tree = ttk.Treeview(right_frame, show="headings")
    tree.pack(side="top", fill="both", expand=True)

    # --- Canvas untuk Matplotlib ---
    # plot_frame = ttk.Frame(right_frame)
    # plot_frame.pack(side="bottom", fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
