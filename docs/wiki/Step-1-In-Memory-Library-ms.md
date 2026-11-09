[English](Step-1-In-Memory-Library) · [Dansk](Step-1-In-Memory-Library-da) · **Bahasa Malaysia**

# Langkah 1: buku dalam senarai di memori

Laman web pertama menyimpan setiap buku dalam senarai `all_books`. Setiap buku ialah kamus dengan tajuk, pengarang dan penilaian. Halaman utama memaparkan buku-buku itu, atau teks "Library is empty.", dan pautan ke halaman untuk menambah buku.

## Cara menjalankannya

Sediakan persekitaran dahulu, lihat [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.main_in_memory
```

## Tangkapan skrin

![Tangkapan skrin 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-1-home.png)

![Tangkapan skrin 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-2-add-form.png)

![Tangkapan skrin 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-3-add-book.png)

![Tangkapan skrin 4](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-4-book-list.png)

![Tangkapan skrin 5](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-5-empty-library.png)

## Apa yang kita pelajari

- Laluan Flask ialah fungsi Python dengan penghias, dan nama fungsi boleh digunakan untuk membina pautan.
- Templat Jinja boleh mengulang senarai dan memilih dengan `if`/`else`, jadi perpustakaan kosong mempunyai mesejnya sendiri.
- Borang menghantar data dengan `POST`, dan Flask membacanya dengan `request.form`.
- Data dalam pemboleh ubah hilang apabila program berhenti. Itulah sebabnya kita memerlukan pangkalan data.
