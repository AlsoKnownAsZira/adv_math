#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

const double PI = 3.14159265358979323846;

// Mengubah derajat ke radian
double derajatKeRadian(double derajat) {
    return derajat * PI / 180.0;
}

// Menghitung faktorial
long double faktorial(int n) {
    long double hasil = 1.0;

    for (int i = 2; i <= n; i++) {
        hasil *= i;
    }

    return hasil;
}

// Hampiran sin(x) dengan Deret Maclaurin
long double sinusMaclaurin(long double x, int n) {
    long double hasil = 0.0;

    for (int k = 0; k <= n; k++) {
        int pangkat = 2 * k + 1;
        long double suku =
            pow(-1, k) * pow(x, pangkat) / faktorial(pangkat);

        hasil += suku;
    }

    return hasil;
}

// Hampiran cos(x) dengan Deret Maclaurin
long double cosinusMaclaurin(long double x, int n) {
    long double hasil = 0.0;

    for (int k = 0; k <= n; k++) {
        int pangkat = 2 * k;
        long double suku =
            pow(-1, k) * pow(x, pangkat) / faktorial(pangkat);

        hasil += suku;
    }

    return hasil;
}

// Hampiran e^x dengan Deret Maclaurin
long double eksponensialMaclaurin(long double x, int n) {
    long double hasil = 0.0;

    for (int k = 0; k <= n; k++) {
        long double suku = pow(x, k) / faktorial(k);
        hasil += suku;
    }

    return hasil;
}

// Hampiran ln(x) menggunakan ln(1 + u)
// Syarat: -1 < u <= 1
long double logaritmaMaclaurin(long double x, int n) {
    long double u = x - 1.0;
    long double hasil = 0.0;

    for (int k = 1; k <= n; k++) {
        long double suku =
            pow(-1, k + 1) * pow(u, k) / k;

        hasil += suku;
    }

    return hasil;
}

int main() {
    int pilihan;
    int n;
    long double x;
    long double hampiran;
    long double nilaiEksak;
    long double galatMutlak;
    long double galatRelatif;
    long double residu;

    cout << fixed << setprecision(12);

    cout << "============================================\n";
    cout << " PROGRAM DERET MACLAURIN\n";
    cout << "============================================\n";
    cout << "1. sin(x)\n";
    cout << "2. cos(x)\n";
    cout << "3. e^x\n";
    cout << "4. ln(x)\n";
    cout << "Pilih fungsi: ";
    cin >> pilihan;

    cout << "\nMasukkan nilai x: ";
    cin >> x;

    cout << "Masukkan banyak suku/iterasi: ";
    cin >> n;

    if (n <= 0) {
        cout << "\nBanyak suku harus lebih besar dari nol.\n";
        return 0;
    }

    switch (pilihan) {
        case 1:
            // Fungsi C++ sin() menggunakan radian
            hampiran = sinusMaclaurin(x, n - 1);
            nilaiEksak = sin(x);
            break;

        case 2:
            // Fungsi C++ cos() menggunakan radian
            hampiran = cosinusMaclaurin(x, n - 1);
            nilaiEksak = cos(x);
            break;

        case 3:
            hampiran = eksponensialMaclaurin(x, n - 1);
            nilaiEksak = exp(x);
            break;

        case 4:
            if (x <= 0 || x > 2) {
                cout << "\nUntuk deret ln(1 + u), nilai x harus memenuhi:\n";
                cout << "0 < x <= 2\n";
                cout << "Karena u = x - 1 harus berada pada -1 < u <= 1.\n";
                return 0;
            }

            hampiran = logaritmaMaclaurin(x, n);
            nilaiEksak = log(x);
            break;

        default:
            cout << "\nPilihan fungsi tidak valid.\n";
            return 0;
    }

    galatMutlak = fabsl(nilaiEksak - hampiran);
    galatRelatif = galatMutlak / fabsl(nilaiEksak);
    residu = galatMutlak;

    cout << "\n============================================\n";
    cout << "HASIL PERHITUNGAN\n";
    cout << "============================================\n";
    cout << "Nilai hampiran       = " << hampiran << endl;
    cout << "Nilai eksak          = " << nilaiEksak << endl;
    cout << "Galat mutlak         = " << galatMutlak << endl;
    cout << "Galat relatif        = " << galatRelatif << endl;
    cout << "Galat relatif (%)    = " << galatRelatif * 100.0L << "%" << endl;
    cout << "Residu               = " << residu << endl;

    return 0;
}