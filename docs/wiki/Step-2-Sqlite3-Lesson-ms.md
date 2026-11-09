[English](Step-2-Sqlite3-Lesson) · [Dansk](Step-2-Sqlite3-Lesson-da) · **Bahasa Malaysia**

# Langkah 2: pelajaran sqlite3

Dalam langkah 1 buku hilang apabila pelayan berhenti. Pangkalan data menyimpannya. SQLite sudah terbina dalam Python, jadi modul `sqlite3` tidak perlu dipasang. Kita menyambung ke fail, mencipta kursor (cursor), menjalankan arahan SQL dan menyimpan dengan commit.

## Cara menjalankannya

Sediakan persekitaran dahulu, lihat [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.infrastructure.lessons.sqlite3_lesson create
python -m library_project.infrastructure.lessons.sqlite3_lesson insert
python -m library_project.infrastructure.lessons.sqlite3_lesson show
```

## Tangkapan skrin

![Tangkapan skrin 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-2-1-sqlite3-create-table.png)

![Tangkapan skrin 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-2-2-sqlite3-insert.png)

## Apa yang kita pelajari

- Fail pangkalan data dicipta apabila kita menyambung kepadanya buat kali pertama.
- Kursor menjalankan SQL: `CREATE TABLE`, `INSERT` dan kemudian `SELECT`.
- Jadual mempunyai medan bertaip; `PRIMARY KEY`, `NOT NULL` dan `UNIQUE` melindungi data.
- Perubahan hanya disimpan selepas `commit()`.
- Kesilapan taip kecil dalam teks SQL hanya dikesan apabila ia dijalankan. SQLAlchemy menghapuskan risiko itu.
