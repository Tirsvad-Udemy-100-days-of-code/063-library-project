[English](Step-3-SQLAlchemy-Lesson) · [Dansk](Step-3-SQLAlchemy-Lesson-da) · **Bahasa Malaysia**

# Langkah 3: pelajaran SQLAlchemy

Teks SQL mudah tersalah tulis, dan kesilapan taip hanya dikesan apabila kod dijalankan. SQLAlchemy ialah ORM: jadual ialah kelas Python, baris ialah objek dan lajur ialah atribut. Jadual `books` yang sama kini diterangkan oleh kelas `Book`.

## Cara menjalankannya

Sediakan persekitaran dahulu, lihat [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.infrastructure.lessons.sqlalchemy_lesson create
python -m library_project.infrastructure.lessons.sqlalchemy_lesson read
```

## Tangkapan skrin

![Tangkapan skrin 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-1-sqlalchemy-create.png)

![Tangkapan skrin 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-2-sqlalchemy-read.png)

![Tangkapan skrin 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-3-sqlalchemy-update.png)

![Tangkapan skrin 4](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-4-sqlalchemy-delete.png)

## Apa yang kita pelajari

- `db.create_all()` mencipta jadual daripada model, di dalam konteks aplikasi Flask.
- Cipta: `db.session.add()` dan `commit()`. Baca: `db.select()` dengan `scalars()` untuk banyak baris dan `scalar()` untuk satu baris.
- Kemas kini: ubah atribut objek yang dimuatkan dan simpan.
- Padam: `db.session.delete()` dan simpan. Id yang tiada dikendalikan sebagai ralat, bukan sebagai ranap.
