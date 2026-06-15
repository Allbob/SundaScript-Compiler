# Referensi Bahasa SundaScript

Dokumen ini berisi daftar lengkap pemetaan (*mapping*) kata kunci (keywords) dan fungsi bawaan (built-in functions) dari bahasa Python ke bahasa SundaScript.

## 1. Kata Kunci Dasar (Keywords)

### Boolean & Nilai Khusus
* `True` ➔ `Leres`
* `False` ➔ `Lepat`
* `None` ➔ `Suwung`

### Logika
* `and` ➔ `jeung`
* `or` ➔ `atawa`
* `not` ➔ `henteu`

### Percabangan
* `if` ➔ `lamun`
* `elif` ➔ `lamun_sanes`
* `else` ➔ `sanesna`

### Perulangan
* `for` ➔ `pikeun`
* `while` ➔ `salami`
* `in` ➔ `dina`
* `break` ➔ `eureun`
* `continue` ➔ `teras`
* `pass` ➔ `liwatan`

### Fungsi
* `def` ➔ `jieun`
* `return` ➔ `pulangkeun`
* `yield` ➔ `hasilkeun`
* `lambda` ➔ `fungsi_leutik`

### Class / Pemrograman Berorientasi Objek (OOP)
* `class` ➔ `kelas`
* `self` ➔ `sorangan`
* `super` ➔ `indung`

### Penanganan Error (Exception Handling)
* `try` ➔ `coba`
* `except` ➔ `iwal`
* `finally` ➔ `tungtungna`
* `raise` ➔ `angkat`
* `assert` ➔ `pastikeun`

### Import & Modul
* `import` ➔ `candak`
* `from` ➔ `ti`
* `as` ➔ `salaku`

### Scope / Konteks
* `global` ➔ `sadayana`
* `nonlocal` ➔ `sanes_lokal`
* `with` ➔ `sareng_ieu`

### Asynchronous (Python 3.5+)
* `async` ➔ `babarengan`
* `await` ➔ `antosan`

### Pattern Matching (Python 3.10+)
* `match` ➔ `cocog`
* `case` ➔ `kaayaan`

### Lainnya
* `del` ➔ `hapus`
* `is` ➔ `nyaeta`

---

## 2. Fungsi Bawaan (Built-in Functions)

### Input / Output
* `print` ➔ `citak`
* `input` ➔ `tanya`

### Konversi Tipe Data
* `int` ➔ `angka`
* `float` ➔ `desimal`
* `str` ➔ `tulisan`
* `bool` ➔ `logika`
* `complex` ➔ `kompleks`

### Koleksi / Struktur Data
* `list` ➔ `daptar`
* `tuple` ➔ `kumpulan`
* `set` ➔ `himpunan`
* `dict` ➔ `kamus`
* `frozenset` ➔ `himpunan_baku`

### Operasi Angka
* `abs` ➔ `mutlak`
* `round` ➔ `buleudkeun`
* `pow` ➔ `pangkat`
* `divmod` ➔ `bagisesa`
* `sum` ➔ `jumlah`
* `max` ➔ `pangluhurna`
* `min` ➔ `panghandapna`

### Iterasi
* `len` ➔ `panjang`
* `range` ➔ `rentang`
* `enumerate` ➔ `daptarkeun`
* `zip` ➔ `gabung`
* `iter` ➔ `ulang`
* `next` ➔ `lajeng`
* `reversed` ➔ `balikeun`
* `sorted` ➔ `urutkeun`

### Pengecekan Logika Tipe / Refleksi
* `all` ➔ `sadayanana`
* `any` ➔ `salah_sahiji`
* `type` ➔ `jenis`
* `isinstance` ➔ `uji_kelas`
* `issubclass` ➔ `uji_subkelas`
* `id` ➔ `tanda`
* `callable` ➔ `tiasa_panggil`

### Karakter & Encoding
* `chr` ➔ `aksara`
* `ord` ➔ `urutan`
* `ascii` ➔ `aski`
* `bin` ➔ `biner`
* `oct` ➔ `oktal`
* `hex` ➔ `heksa`

### Utilitas Objek & Atribut
* `getattr` ➔ `candak_sipat`
* `setattr` ➔ `atur_sipat`
* `hasattr` ➔ `aya_sipat`
* `delattr` ➔ `hapus_sipat`

### Namespace & Memori
* `globals` ➔ `sadayanana_global`
* `locals` ➔ `lokalna`
* `vars` ➔ `variabelna`
* `dir` ➔ `arah`
* `bytes` ➔ `bait`
* `bytearray` ➔ `susunan_bait`
* `memoryview` ➔ `tempo_memori`

### Utilitas Eksekusi & Kelas
* `eval` ➔ `evaluasi`
* `exec` ➔ `jalankeun`
* `compile` ➔ `kompilasi`
* `open` ➔ `buka`
* `map` ➔ `petakeun`
* `filter` ➔ `saring`
* `property` ➔ `properti`
* `staticmethod` ➔ `metode_statis`
* `classmethod` ➔ `metode_kelas`
* `__import__` ➔ `__candak__`
* `breakpoint` ➔ `titik_eureun`
* `format` ➔ `bentuk`
* `repr` ➔ `wakil`
* `hash` ➔ `acak`
* `help` ➔ `tolong`
* `slice` ➔ `potong`
* `object` ➔ `objek`
