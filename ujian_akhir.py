def tambah(a, b):
    return (a + b)
def main():
    print("=== Ujian Akhir SundaScript ===")
    teks_a = input("Masukkan angka pertama: ")
    teks_b = input("Masukkan angka kedua: ")
    angka_a = int(teks_a)
    angka_b = int(teks_b)
    hasil = tambah(angka_a, angka_b)
    print("Hasil Penambahan:")
    print(hasil)
    print("-----------------------")
    print("Tes Perulangan (Looping)")
    angka_awal = 1
    while (angka_awal <= 3):
        print("Iterasi ke-")
        print(angka_awal)
        angka_awal = (angka_awal + 1)
    print("-----------------------")
    tes_optimasi = 52
    if (tes_optimasi > 50):
        print("Optimasi Matematika Berhasil!")
    else:
        print("Gagal Optimasi")
    input("Tekan Enter untuk keluar...")
main()
