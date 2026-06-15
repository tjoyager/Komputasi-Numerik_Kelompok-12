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
    # TODO: Implementasi R(0,0)
    pass

def recursive_trapezoid(f, a, b, k, prev_R):
    # TODO: Implementasi R(k,0) rekursif
    pass

def plot_graph(canvas_frame, f_str, a, b):
    """
    Menampilkan grafik fungsi dan area integrasi di dalam GUI.
    """
    # TODO: Gunakan matplotlib untuk plot f(x) dan fill_between antara a dan b
    pass


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
