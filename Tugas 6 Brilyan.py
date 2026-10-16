"""Tugas Minggu 6 Metode Numerik
f(x) = 4x^3 - 15x^2 + 17x - 6 = 0
Metode: Bagidua (Bolzano), Regula-Falsi (tertutup); Secant, Fixed Point (terbuka)
Pembanding : Newton-Raphson (minggu 5)
"""
LEBAR = 76
EPS = 1e-6
NMAKS = 100

f  = lambda x: 4*x**3 - 15*x**2 + 17*x - 6
df = lambda x: 12*x**2 - 30*x + 17

def cetak(t=""): print(t)

def judul(t):
    cetak("\n" + "=" * LEBAR); cetak(t.center(LEBAR)); cetak("=" * LEBAR)

def subjudul(t):
    cetak(f"\n>> {t}"); cetak("-" * LEBAR)

def tabel(kepala, baris, lebar):
    garis = "+" + "+".join("-" * (w + 2) for w in lebar) + "+"
    fmt = lambda r: "|" + "|".join(f" {str(c):^{w}} " for c, w in zip(r, lebar)) + "|"
    cetak(garis); cetak(fmt(kepala)); cetak(garis)
    for b in baris: cetak(fmt(b))
    cetak(garis)

# ---------------- Cari selang yang mengandung akar ----------------
def cari_selang(a, b, h):
    n = round((b - a) / h)
    xs = [a + i * h for i in range(n + 1)]
    return [(xs[i], xs[i + 1]) for i in range(n) if f(xs[i]) * f(xs[i + 1]) < 0]

# ---------------- Metode tertutup ----------------
def bagidua(a, b, eps=EPS):
    riwayat = []
    for r in range(NMAKS):
        c = (a + b) / 2
        riwayat.append([r, f"{a:.6f}", f"{c:.6f}", f"{b:.6f}", f"{f(c):.6f}", f"{abs(b-a):.6f}"])
        if f(a) * f(c) < 0: b = c
        else:               a = c
        if abs(b - a) < eps or abs(f(c)) < 1e-8:
            return c, r + 1, riwayat
    raise RuntimeError("bagidua tidak konvergen")

def regula_falsi(a, b, eps=EPS):
    riwayat, c_lama = [], None
    for r in range(NMAKS):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        dx = abs(c - c_lama) if c_lama is not None else None
        riwayat.append([r, f"{a:.6f}", f"{c:.6f}", f"{b:.6f}", f"{f(c):.6f}",
                        "-" if dx is None else f"{dx:.6f}"])
        if abs(f(c)) < 1e-8 or (dx is not None and dx < eps):
            return c, r + 1, riwayat
        if f(a) * f(c) < 0: b = c
        else:               a = c
        c_lama = c
    raise RuntimeError("regula-falsi tidak konvergen")

# ---------------- Metode terbuka ----------------
def secant(x0, x1, eps=EPS):
    riwayat = [[0, f"{x0:.6f}", f"{f(x0):.6f}", "-"],
               [1, f"{x1:.6f}", f"{f(x1):.6f}", f"{abs(x1-x0):.6f}"]]
    for r in range(2, NMAKS):
        if f(x1) == f(x0):
            raise ZeroDivisionError("f(x1) = f(x0)")
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        riwayat.append([r, f"{x2:.6f}", f"{f(x2):.6f}", f"{abs(x2-x1):.6f}"])
        if abs(x2 - x1) < eps:
            return x2, r, riwayat
        x0, x1 = x1, x2
    raise RuntimeError("secant tidak konvergen")

def titik_tetap(g, x0, eps=EPS, nmaks=NMAKS):
    x, riwayat = x0, [[0, f"{x0:.6f}", f"{f(x0):.6f}", "-"]]
    for r in range(1, nmaks + 1):
        x_lama, x = x, g(x)
        riwayat.append([r, f"{x:.6e}" if abs(x) > 1e6 else f"{x:.6f}",
                        f"{f(x):.6e}" if abs(f(x)) > 1e6 else f"{f(x):.6f}",
                        f"{abs(x - x_lama):.6e}" if abs(x - x_lama) > 1e6 else f"{abs(x - x_lama):.6f}"])
        if abs(x - x_lama) < eps:
            return x, r, True, riwayat
        if abs(x) > 1e12:
            return x, r, False, riwayat
    return x, nmaks, False, riwayat

# dua bentuk g(x) dari f(x) = 0
g_a = lambda x: (-4*x**3 + 15*x**2 + 6) / 17     # 17x = -4x^3 + 15x^2 + 6
g_c = lambda x: 4*x**3 - 15*x**2 + 18*x - 6      # x = x + f(x)

def dg(g, x, h=1e-6):
    return (g(x + h) - g(x - h)) / (2 * h)

def newton(x0, eps=EPS):
    x = x0
    for r in range(1, NMAKS):
        x_baru = x - f(x) / df(x)
        if abs(x_baru - x) < eps:
            return x_baru, r
        x = x_baru
    raise RuntimeError("newton tidak konvergen")

# ======================== PROGRAM UTAMA ========================
if __name__ == "__main__":
    judul("TUGAS MINGGU 6 - AKAR f(x) = 4x^3 - 15x^2 + 17x - 6")
    cetak(f"Toleransi eps = {EPS}   |   akar sebenarnya: 0.75, 1, 2")

    # 1. Pencarian selang
    judul("1. PENCARIAN SELANG YANG MENGANDUNG AKAR")
    H = 0.3
    cetak(f"Tabel f(x) pada [0, 3] dengan h = {H} (tanda berubah = ada akar)")
    xs = [round(i * H, 10) for i in range(11)]
    tabel(["x", "f(x)", "Tanda"], [[f"{x:.2f}", f"{f(x):.6f}", "+" if f(x) > 0 else ("-" if f(x) < 0 else "0")] for x in xs], [6, 12, 6])
    selang = cari_selang(0, 3, H)
    cetak("\nSelang yang mengandung akar: " + ", ".join(f"[{a:.2f}, {b:.2f}]" for a, b in selang))

    # 2. Bagidua
    judul("2. METODE BAGIDUA (BOLZANO) - TERTUTUP")
    a, b = 1.5, 3.0
    cetak(f"Selang awal [{a}, {b}]:  f({a}) = {f(a):.4f},  f({b}) = {f(b):.4f}  (beda tanda)")
    akar_bd, n_bd, riw = bagidua(a, b)
    tabel(["r", "a", "c", "b", "f(c)", "lebar"], riw, [3, 10, 10, 10, 11, 10])
    cetak(f"\nHASIL: akar = {akar_bd:.6f}  ({n_bd} iterasi)")

    # 3. Regula-falsi
    judul("3. METODE REGULA-FALSI - TERTUTUP")
    cetak(f"Selang awal [{a}, {b}]   c = b - f(b)(b-a)/(f(b)-f(a))")
    akar_rf, n_rf, riw = regula_falsi(a, b)
    tabel(["r", "a", "c", "b", "f(c)", "|c-c_lama|"], riw, [3, 10, 10, 10, 11, 11])
    cetak(f"\nHASIL: akar = {akar_rf:.6f}  ({n_rf} iterasi)")

    # 4. Secant
    judul("4. METODE SECANT - TERBUKA")
    x0, x1 = 3.0, 2.5
    cetak(f"Tebakan awal x0 = {x0}, x1 = {x1}   x2 = x1 - f(x1)(x1-x0)/(f(x1)-f(x0))")
    akar_sc, n_sc, riw = secant(x0, x1)
    tabel(["r", "x_r", "f(x_r)", "|dx|"], riw, [3, 10, 11, 10])
    cetak(f"\nHASIL: akar = {akar_sc:.6f}  ({n_sc} iterasi)")

    # 5. Titik-tetap
    judul("5. METODE FIXED POINT - TERBUKA")
    cetak("Susun f(x)=0 menjadi x = g(x),  x_(r+1) = g(x_r),  x0 = 3")
    subjudul("Bentuk A: g(x) = (-4x^3 + 15x^2 + 6) / 17")
    cetak(f"|g'(2)| = {abs(dg(g_a, 2.0)):.4f} < 1  ->  seharusnya konvergen")
    akar_tt, n_tt, ok, riw = titik_tetap(g_a, 3.0)
    tabel(["r", "x_r", "f(x_r)", "|dx|"], riw, [3, 10, 11, 10])
    cetak(f"\nHASIL: akar = {akar_tt:.6f}  ({n_tt} iterasi)  -> KONVERGEN")
    subjudul("Bentuk C: g(x) = 4x^3 - 15x^2 + 18x - 6   (x = x + f(x))")
    cetak(f"|g'(2)| = {abs(dg(g_c, 2.0)):.4f} > 1  ->  seharusnya divergen")
    x_c, n_c, ok_c, riw = titik_tetap(g_c, 3.0)
    tabel(["r", "x_r", "f(x_r)", "|dx|"], riw, [3, 14, 14, 14])
    cetak(f"\nHASIL: {'konvergen' if ok_c else 'DIVERGEN'} (nilai meledak pada iterasi ke-{n_c})")

    # 6. Perbandingan
    judul("6. PERBANDINGAN SEMUA METODE (akar = 2)")
    akar_nr, n_nr = newton(3.0)
    baris = [
        ["Bagidua (Bolzano)", "Tertutup", "[1.5, 3]",     f"{akar_bd:.6f}", f"{abs(akar_bd-2):.2e}", n_bd],
        ["Regula-Falsi",      "Tertutup", "[1.5, 3]",     f"{akar_rf:.6f}", f"{abs(akar_rf-2):.2e}", n_rf],
        ["Secant",            "Terbuka",  "3 dan 2.5",    f"{akar_sc:.6f}", f"{abs(akar_sc-2):.2e}", n_sc],
        ["Fixed Point",       "Terbuka",  "x0 = 3",       f"{akar_tt:.6f}", f"{abs(akar_tt-2):.2e}", n_tt],
        ["Newton-Raphson",    "Terbuka",  "x0 = 3",       f"{akar_nr:.6f}", f"{abs(akar_nr-2):.2e}", n_nr],
    ]
    tabel(["Metode", "Jenis", "Awal", "Akar", "Galat", "Iterasi"], baris, [18, 9, 10, 10, 10, 7])

    # 6. Semua akar dengan bagidua
    subjudul("Bonus: ketiga akar dengan bagidua")
    baris = []
    for (sa, sb) in selang:
        c, n, _ = bagidua(sa, sb)
        baris.append([f"[{sa:.1f}, {sb:.1f}]", f"{c:.6f}", n])
    tabel(["Selang", "Akar", "Iterasi"], baris, [14, 10, 8])
    judul("SELESAI")
