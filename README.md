
# 📊 Aplikasi Visualisasi Data Penjualan

Aplikasi ini dibuat dengan Streamlit untuk memvisualisasikan data penjualan dari file CSV atau Excel. Fitur utama termasuk histogram distribusi volume penjualan dan animasi grafik harga per tanggal.

---

## 🧰 Fitur Utama

- 📤 Upload file CSV / Excel
- 📊 Histplot distribusi kolom `Volume`
- 📈 Animasi pergerakan `Harga` terhadap `Tanggal`
- ⏱️ Slider untuk mengatur kecepatan animasi
- 🔒 Validasi kolom penting (`Volume`, `Harga`, `Tanggal`)
- 🖋️ Watermark hak cipta di grafik & halaman

---

## 🗂️ Struktur Folder

```
Project UAS/
├── app.py               # File utama aplikasi
├── contoh_data.csv      # Contoh data penjualan
└── .venv/               # Virtual environment (jangan upload ke repo)
```

---

## ⚙️ Cara Menjalankan Aplikasi

### 1. Buat dan aktifkan environment (opsional)
```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
```

### 2. Install dependensi
```bash
pip install streamlit pandas seaborn matplotlib openpyxl
```

### 3. Jalankan Streamlit
```bash
streamlit run app.py
```

---

## 🧪 Format Data yang Diharapkan

| Tanggal      | Harga   | Volume |
|--------------|---------|--------|
| 2025-01-01   | 15000   | 30     |
| 2025-01-02   | 14500   | 45     |

---

## 🧑‍💻 Dibuat Oleh

**Hilman**  
Mahasiswa Teknik Komputer & Jaringan  
© 2025 by Hilman
