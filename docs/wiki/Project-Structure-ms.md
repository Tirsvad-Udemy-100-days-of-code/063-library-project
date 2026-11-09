[English](Project-Structure) · [Dansk](Project-Structure-da) · **Bahasa Malaysia**

# Struktur projek dan ujian

Kod sumber dibahagikan kepada empat lapisan dalam `src/library_project/`:

| Lapisan | Kandungan |
| --- | --- |
| `domain` | `Book` dan peraturannya (tajuk, pengarang, penilaian). Ia tidak menggunakan rangka kerja. |
| `application` | Kes penggunaan (tambah, senarai, ubah penilaian, padam) dan port storan yang diperlukan. |
| `infrastructure` | Senarai `all_books` di memori, model dan repositori `Book` SQLAlchemy serta skrip pelajaran. |
| `presentation` | Laluan Flask `home`, `add`, `edit`, `delete` dan templat Jinja. |

`constants.py` menyimpan semua pemalar yang dikongsi. `main_in_memory.py` dan `main.py` membina dua laman web itu. Ujian berada dalam `tests/` dan dijalankan dengan `python -m pytest`. Tangkapan skrin pada halaman ini dibuat oleh `scripts/screenshots/capture_screenshot.sh`, yang menjalankan pelayar tanpa tetingkap dalam bekas Docker, jadi tiada tetingkap dibuka pada desktop anda.

## Apa yang kita pelajari

- Peraturan perniagaan tidak bergantung pada Flask atau pangkalan data, jadi ia diuji tanpanya.
- Nama dalam tugasan (`all_books`, `Book`, `db`, `home`, `add`, `edit`, `delete`) dikekalkan di tempat yang sesuai.
- Tangkapan skrin boleh dibuat semula pada bila-bila masa dengan cara yang sama dalam bekas.
