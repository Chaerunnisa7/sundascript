# 🌿 SundaScript Compiler

> Compiler mini bahasa pemrograman berbasis **Bahasa Sunda** — dibuat menggunakan Python.

---

## 📖 Deskripsi

**SundaScript** adalah bahasa pemrograman sederhana yang menggunakan **keyword Bahasa Sunda** sebagai sintaksnya. Project ini merupakan implementasi compiler mini yang mencakup seluruh tahapan kompilasi, mulai dari analisis leksikal hingga eksekusi kode hasil kompilasi.

---

## 🗂️ Struktur File

```
sundascript/
├── main.py             → Entry point utama (jalankan ini)
├── lexer.py            → Lexical Analyzer (tokenizer)
├── ast_builder.py      → Definisi node-node AST
├── parser.py           → Syntax Analyzer (parser)
├── semantic.py         → Semantic Analyzer
├── optimizer.py        → Code Optimizer (constant folding)
├── code_generator.py   → Code Generator (output Python)
├── parse_tree.py       → Visualisasi Parse Tree
└── README.md           → Dokumentasi ini
```

---

## 🔑 Keyword Bahasa Sunda

| Keyword SundaScript | Arti (Bahasa Sunda) | Fungsi |
|---|---|---|
| `naro` | menyimpan / menaruh | Deklarasi variabel |
| `cetakkeun` | cetakkan | Print / tampilkan output |
| `lamun` | lamun (kalau) | If / percabangan |
| `atawa` | atau | Else |
| `bari` | sambil / selama | While loop |
| `eureun` | berhenti | Break |
| `balik` | kembali | Return |
| `bener` | benar | True |
| `salah` | salah | False |

---

## 🚀 Cara Menjalankan

### Prasyarat
- Python 3.x sudah terinstal

### Langkah-langkah

**1. Clone / download project ini**

**2. Buka terminal di folder `sundascript/`**

**3. Jalankan compiler:**
```bash
python main.py
```

**4. Tulis kode SundaScript, tekan Enter tiap baris, lalu ketik `SELESAI`**

**5. Ketik `KALUAR` untuk keluar dari program**

---

## 💡 Contoh Program

### Hello World
```
naro nama = "Sunda";
cetakkeun nama;
SELESAI
```

### Percabangan (if-else)
```
naro umur = 20;
lamun (umur > 17) {
    cetakkeun "geus dewasa";
}
atawa {
    cetakkeun "can dewasa";
}
SELESAI
```

### Perulangan (while)
```
naro x = 1;
bari (x < 6) {
    cetakkeun x;
    x = x + 1;
}
SELESAI
```

### Operasi Aritmatika
```
naro a = 10;
naro b = 5;
naro hasil = a + b;
cetakkeun hasil;
SELESAI
```

---

## ⚙️ Tahapan Kompilasi

```
Kode Sumber (.sunda)
        │
        ▼
┌───────────────┐
│  1. LEXER     │  → Memecah kode jadi token-token
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  2. PARSER    │  → Menyusun token jadi Parse Tree / AST
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  3. SEMANTIC  │  → Cek variabel sudah dideklarasi, dsb
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  4. OPTIMIZER │  → Constant folding (sederhanakan ekspresi)
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  5. CODE GEN  │  → Generate kode Python
└───────┬───────┘
        │
        ▼
┌───────────────┐
│  6. EXECUTE   │  → Jalankan hasil kompilasi
└───────────────┘
```

---

## 📌 Komponen Penilaian

| No | Komponen | File |
|---|---|---|
| 1 | Desain Bahasa | README.md (tabel keyword) |
| 2 | Lexer | `lexer.py` |
| 3 | Parser | `parser.py` |
| 4 | AST | `ast_builder.py` + `parse_tree.py` |
| 5 | Semantic Analysis | `semantic.py` |
| 6 | Code Optimization | `optimizer.py` |
| 7 | Code Generation | `code_generator.py` |
| 8 | Dokumentasi | README.md + `main.py` |

---

## 👥 Informasi Proyek

- **Nama Proyek:** SundaScript Compiler  
- **Mata Kuliah:** Teknik Kompilasi  
- **Bahasa Implementasi:** Python 3  
- **Bahasa Sumber:** Bahasa Sunda  
- **Bahasa Target:** Python (sebagai intermediate)

---

## 📝 Catatan

- Keyword bersifat **case-sensitive** (harus huruf kecil semua)
- Setiap statement diakhiri dengan **titik koma** `;`
- Blok kode menggunakan **kurung kurawal** `{ }`
- Komentar menggunakan `//` di awal baris

---

> *"Ulah poho ka wiwitan"* — Jangan lupa pada asal mulanya 🌿