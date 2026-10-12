"""Tugas #05 Metode Numerik"""
import math

LEBAR = 72
def cetak(teks=""):
    print(teks)

def judul(teks):
    cetak("\n" + "=" * LEBAR)
    cetak(teks.center(LEBAR))
    cetak("=" * LEBAR)

def subjudul(teks):
    cetak(f"\n>> {teks}")
    cetak("-" * LEBAR)

def tabel(kepala, baris, lebar):
    """Cetak tabel berbingkai. kepala: list str, baris: list of list."""
    garis = "+" + "+".join("-" * (w + 2) for w in lebar) + "+"
    fmt = lambda row: "|" + "|".join(f" {str(c):^{w}} " for c, w in zip(row, lebar)) + "|"
    cetak(garis); cetak(fmt(kepala)); cetak(garis)
    for b in baris:
        cetak(fmt(b))
    cetak(garis)

# ---------------------------------------------------------------
# SOAL 1: Konvergen vs divergen (titik-tetap)
# ---------------------------------------------------------------
def titik_tetap(g, x0, eps=1e-6, nmaks=30):
    x = x0
    for i in range(1, nmaks + 1):
        x_lama, x = x, g(x)
        if abs(x - x_lama) < eps:
            return x, i, True
        if abs(x) > 1e12:
            return x, i, False
    return x, nmaks, False

def dg(g, x, h=1e-6):
    return (g(x + h) - g(x - h)) / (2 * h)

def soal1():
    judul("SOAL 1 - KONVERGENSI LELARAN TITIK-TETAP")
    cetak("f(x) = x^2 - 2x - 3 = 0  (akar: 3 dan -1),  x0 = 4,  eps = 1e-6")
    cetak("Syarat konvergen: |g'(x)| < 1 di sekitar akar")

    kasus = [
        ("g(x) = sqrt(2x+3)", lambda x: math.sqrt(2*x + 3), 3.0),
        ("g(x) = 3/(x-2)",    lambda x: 3/(x - 2),          -1.0),
        ("g(x) = (x^2-3)/2",  lambda x: (x**2 - 3)/2,        3.0),
    ]
    baris = []
    for nama, g, akar in kasus:
        x, n, ok = titik_tetap(g, 4.0)
        hasil = f"{x:.6f}" if ok else "meledak"
        baris.append([nama, f"{abs(dg(g, akar)):.4f}",
                      "KONVERGEN" if ok else "DIVERGEN", hasil, n])
    subjudul("Perbandingan bentuk g(x)")
    tabel(["Bentuk g(x)", "|g'(akar)|", "Status", "Hasil", "Iterasi"],
          baris, [20, 10, 10, 10, 7])

    subjudul("Cara mengatasi divergen")
    for s in ["1. Susun ulang f(x)=0 menjadi g(x) dengan |g'| < 1",
              "2. Pilih tebakan awal yang lebih dekat ke akar",
              "3. Pasang batas iterasi maksimum (Nmaks)",
              "4. Pindah ke metode tertutup (bagidua / regula-falsi)"]:
        cetak("   " + s)

# ---------------------------------------------------------------
# SOAL 2: Newton-Raphson
# ---------------------------------------------------------------
f  = lambda x: 4*x**3 - 15*x**2 + 17*x - 6
df = lambda x: 12*x**2 - 30*x + 17

def newton_raphson(x0, eps=1e-6, nmaks=50):
    x, riwayat = x0, [[0, f"{x0:.6f}", f"{f(x0):.6f}", f"{df(x0):.6f}", "-"]]
    for r in range(1, nmaks + 1):
        if df(x) == 0:
            raise ZeroDivisionError("f'(x)=0")
        x_baru = x - f(x)/df(x)
        dx = abs(x_baru - x)
        x = x_baru
        riwayat.append([r, f"{x:.6f}", f"{f(x):.6f}", f"{df(x):.6f}", f"{dx:.6f}"])
        if dx < eps:
            return x, r, riwayat
    raise RuntimeError("tidak konvergen")

def soal2():
    judul("SOAL 2 - NEWTON-RAPHSON")
    cetak("f(x)  = 4x^3 - 15x^2 + 17x - 6")
    cetak("f'(x) = 12x^2 - 30x + 17")
    cetak("x_(r+1) = x_r - f(x_r)/f'(x_r),   x0 = 3,   eps = 1e-6")

    akar, n, riwayat = newton_raphson(3.0)
    subjudul("Tabel lelaran")
    tabel(["r", "x_r", "f(x_r)", "f'(x_r)", "|dx|"], riwayat, [3, 10, 10, 10, 10])
    cetak(f"\nHASIL: akar = {akar:.6f}  ({n} iterasi),  f(akar) = {f(akar):.2e}")

    subjudul("Pengaruh tebakan awal (akar sebenarnya: 0.75, 1, 2)")
    baris = []
    for x0 in (0.0, 0.9, 1.5, 3.0):
        a, k, _ = newton_raphson(x0)
        baris.append([x0, f"{a:.6f}", k])
    tabel(["x0", "Akar", "Iterasi"], baris, [6, 10, 8])

if __name__ == "__main__":
    soal1()
    soal2()
    judul("SELESAI")
