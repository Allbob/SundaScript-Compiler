# SundaScript Mini Compiler

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Status](https://img.shields.io/badge/Status-Tahap_Pengembangan-yellow?style=for-the-badge) ![Lisensi](https://img.shields.io/badge/Lisensi-MIT-green?style=for-the-badge)

SundaScript Mini Compiler adalah proyek kompilator berukuran kecil yang mengadaptasi sebagian kosakata bahasa pemrograman ke dalam bahasa daerah Sundakabau. Proyek ini dibangun sebagai eksperimen dan implementasi praktikum untuk ranah ilmu Teknik Kompilasi. 

Perlu dicatat bahwa kompilator ini tidak menerjemahkan atau mengubah seluruh fitur bahasa Python secara penuh. Kompilator ini **murni sebuah bahasa *mini*** yang hanya menargetkan dan mendukung **subset kata kunci** serta operasi dasar tertentu untuk memvalidasi alur teori kompilasi dari awal hingga menjadi berkas eksekusi.

## Fitur Utama

- Sintaks Lokal Dasar: Mendukung kata kunci pemrograman esensial yang diubah ke bahasa Sunda (seperti `buek` untuk mendefinisikan fungsi, `kok` untuk kondisi logika, `salamo` untuk perulangan). Rujukan lengkap terdapat pada berkas REFERENSI_BAHASA.md.
- Standalone Binary: Dilengkapi dengan pengaturan pemaketan agar skrip penyusun kompilator dapat dibungkus menjadi satu berkas `sunda.exe` yang langsung berjalan di OS Windows.
- Pipeline Kompilasi Murni: Alur kerja menerapkan prinsip pembacaan leksikal, parsing AST, dan optimasi dasar seperti *Constant Folding* dan *Dead Code Elimination* sebelum eksekusi terjadi.

## Panduan Penggunaan `sunda.exe`

Bagi pengguna yang sudah memiliki berkas `sunda.exe` (atau mengunduhnya dari rilis), program ini dapat dijalankan langsung melalui Command Prompt atau PowerShell di Windows **tanpa memerlukan instalasi Python**.

### Persiapan Direktori & Environment Variables PATH
Agar eksekusi skrip berhasil, pastikan berkas kode berekstensi `.sunda` yang ingin dieksekusi berada di **satu folder yang sama** dengan `sunda.exe`. 

Namun, agar kompilator dapat dipanggil dari direktori mana saja tanpa harus selalu menyalin `sunda.exe`, direktori penyimpanannya perlu didaftarkan ke dalam *Environment Variables PATH* Windows:
1. Buka *Start Menu* Windows, ketik **Edit the system environment variables**, lalu tekan *Enter*.
2. Klik tombol **Environment Variables...** di sudut kanan bawah.
3. Pada area *System variables* (atau *User variables*), pilih variabel bernama **Path**, lalu klik **Edit...**
4. Klik **New**, lalu tempel (*paste*) jalur (*Path*) lengkap menuju folder tempat `sunda.exe` berada (contoh: `C:\Path\Menuju\Mini-Compiler\dist`).
5. Klik **OK** pada semua jendela. Setelah proses ini selesai, perintah `sunda.exe` sudah bisa dieksekusi dari direktori mana pun di dalam terminal.

### Menjalankan Skrip
Perintah `jalan` digunakan untuk **mengeksekusi berkas kode** berekstensi `.sunda` secara langsung.
```bash
sunda.exe jalan (nama_file).sunda
```

### Membangun Aplikasi Baru (Fitur Rilis)
Perintah `rilis` digunakan jika pembuat kode ingin **mempaketkan skrip** `.sunda` miliknya menjadi sebuah **aplikasi `.exe` tersendiri**. Ini berguna agar hasil program buatan (misal aplikasi kalkulator Sunda) bisa dibagikan dan dijalankan oleh orang lain, tanpa mengharuskan orang tersebut memiliki `sunda.exe` di komputernya.
```bash
sunda.exe rilis (nama_file).sunda
```
## Setup Builder (Membangun Ulang Kompilator)

Jika ada pembaruan pada inti kompilator, berkas `sunda.exe` dapat dibangun ulang melalui skrip utama `sunda.py` menggunakan `PyInstaller`. Pembuatan ini disarankan dilakukan di dalam **lingkungan virtual Python (Virtual Environment) yang bersih**.

1. Lakukan instalasi pustaka pembuat berkas eksekusi:
   ```bash
   pip install pyinstaller
   ```

2. Bangun program melalui perintah berikut:
   ```bash
   pyinstaller --onefile --name sunda sunda.py
   ```

Hasil kompilasi mesin kompilator tersebut akan berada di dalam direktori `dist/`.

## Pengujian (Testing)

Proyek ini mendefinisikan beberapa lapisan pengujian (*testing*) untuk membuktikan bahwa `sunda.exe` beroperasi secara stabil sesuai konsep awal perancangan kompilator.

### 1. Black Box & Functional Testing
Pengujian ini memvalidasi keluaran akhir tanpa mencampuri mesin kompilator di baliknya. Pengujian dilakukan secara otomatis menggunakan pustaka `pytest` yang berinteraksi langsung dengan berkas `sunda.exe` via sub-proses OS.

```python
import subprocess
import pytest

# Menggunakan pola Parameterized untuk menguji berbagai kosakata dasar Sunda
@pytest.mark.parametrize("kode_sunda, output_harapan", [
    ("cetak(5 + 5)", "10\n"),
    ("x = 10\ncetak(x)", "10\n"),
])
def test_fungsional_sunda(tmp_path, kode_sunda, output_harapan):
    jalur_skrip = tmp_path / "test.sunda"
    jalur_skrip.write_text(kode_sunda)

    hasil = subprocess.run(["dist/sunda.exe", "jalan", str(jalur_skrip)], capture_output=True, text=True)
    assert hasil.stdout == output_harapan
```
**Ekspektasi Penjelasan:** Jika script di atas dijalankan via `pytest test_sunda.py`, terminal akan mencetak status `PASSED`. Ini membuktikan bahwa mekanisme kompilasi untuk alokasi memori (penugasan variabel) dan *output console* (cetak) sukses bekerja dengan akurat.

### 2. Stress Testing (Beban Kompilasi)
Pengujian ekstrem diberikan untuk melihat apakah *Parser* dan *AST Builder* mampu menangani beban sintaks yang dalam (seperti rekursi berlapis atau perhitungan tak terbatas) tanpa mengalami kebocoran memori atau *Stack Overflow*.

Sebagai contoh, dilakukan injeksi operasi aritmatika brutal sebanyak puluhan ribu token dalam satu baris:
```text
cetak(1 + 2 * 3 - 4 / 5 + 6 * 7 ... [berulang hingga 10.000 token])
```
**Ekspektasi Penjelasan:** Karena kompilator ini memiliki modul Optimasi Fase 6 (*Constant Folding*), program pembaca tidak akan mogok (*crash*), melainkan mesin akan mendeteksi kerumitan tersebut dan menyederhanakan perhitungan raksasanya menjadi sebuah angka final seketika di belakang layar, lalu langsung mencetaknya dalam hitungan milidetik.

### 3. Negative Testing (Penanganan Cacat Kode)
Pengujian ini dilakukan dengan sengaja mengumpankan kode yang cacat secara tata bahasa (misalnya blok kurung kurawal `{` yang tidak pernah ditutup, atau menggunakan variabel yang belum dibuat).
**Ekspektasi Penjelasan:** Kompilator tidak boleh mati membeku secara mendadak, melainkan harus melempar pesan *SyntaxError* atau *SemanticError* yang *graceful*, memberitahu letak baris kerusakan secara presisi.

## Struktur Repositori

Repositori ini memuat seluruh kode sumber kompilator mulai dari mesin inti hingga berkas eksekusi:

```text
sundascript-compiler/
│
├── src/                      # Modul Inti Kompilator (Leksikal hingga Code Gen)
├── sunda.py                 # File Utama (Builder / CLI Setup)
├── trace_compiler.py         # Skrip Diagnostik (mencetak log visual Token & AST di terminal untuk debugging)
├── REFERENSI_BAHASA.md       # Daftar Kosakata SundaScript
├── README.md                 # Dokumentasi Proyek
├── LICENSE                   # Lisensi MIT
└── dist/
    └── sunda.exe            # Aplikasi Kompilator Mandiri
```

## Rencana Pengembangan (Roadmap)

Kompilator mini ini sedang dipersiapkan untuk peningkatan pada beberapa aspek:
- Penyempurnaan pelacakan error berbasis nomor baris (line number).
- Restrukturisasi presedensi operator aritmatika.
- Penambahan stabilitas pemetaan kata kunci kontrol bahasa.

