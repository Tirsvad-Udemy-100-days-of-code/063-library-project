[English](Step-4-Library-With-Database) · [Dansk](Step-4-Library-With-Database-da) · **Bahasa Malaysia**

# Langkah 4: laman web perpustakaan dengan pangkalan data

Kini laman web dari langkah 1 menyimpan bukunya dalam SQLite. Halaman utama menyenaraikan setiap buku dari pangkalan data dengan pautan **Edit Rating** dan pautan **Delete**. Tambah, ubah dan padam semuanya berakhir dengan pengalihan ke halaman utama.

## Cara menjalankannya

Sediakan persekitaran dahulu, lihat [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.main
```

## Tangkapan skrin

![Tangkapan skrin 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-1-add-book.png)

![Tangkapan skrin 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-2-library-list.png)

![Tangkapan skrin 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-3-edit-rating.png)

![Tangkapan skrin 4](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-4-rating-changed.png)

![Tangkapan skrin 5](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-5-book-deleted.png)

## Apa yang kita pelajari

- Laman web bercakap dengan repositori, jadi senarai di memori dan pangkalan data boleh ditukar tanpa mengubah laluan.
- Id buku dibawa dalam alamat (`/edit?id=3`, `/delete?id=3`).
- Selepas perubahan kita mengalihkan ke halaman utama, jadi muat semula halaman tidak mengulangi perubahan.
- Tajuk pendua ialah ralat biasa yang ditunjukkan kepada pembaca, dan id yang tidak dikenali memberi 404.
- Satu ujian memulakan aplikasi kedua pada fail pangkalan data yang sama dan menunjukkan bahawa buku kekal selepas dimulakan semula.
