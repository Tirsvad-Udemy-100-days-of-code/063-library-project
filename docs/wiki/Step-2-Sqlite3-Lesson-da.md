[English](Step-2-Sqlite3-Lesson) · **Dansk** · [Bahasa Malaysia](Step-2-Sqlite3-Lesson-ms)

# Trin 2: sqlite3-lektionen

I trin 1 forsvinder bøgerne, når serveren stopper. En database gemmer dem. SQLite er indbygget i Python, så modulet `sqlite3` kræver ingen installation. Vi forbinder til en fil, laver en markør (cursor), kører SQL-kommandoer og gemmer med commit.

## Sådan kører du det

Gør først miljøet klar, se [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.infrastructure.lessons.sqlite3_lesson create
python -m library_project.infrastructure.lessons.sqlite3_lesson insert
python -m library_project.infrastructure.lessons.sqlite3_lesson show
```

## Skærmbilleder

![Skærmbillede 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-2-1-sqlite3-create-table.png)

![Skærmbillede 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-2-2-sqlite3-insert.png)

## Hvad vi lærte

- En databasefil oprettes, første gang vi forbinder til den.
- En markør kører SQL: `CREATE TABLE`, `INSERT` og senere `SELECT`.
- En tabel har typede felter; `PRIMARY KEY`, `NOT NULL` og `UNIQUE` beskytter data.
- Ændringer gemmes først efter `commit()`.
- En lille tastefejl i en SQL-tekst opdages først, når den køres. SQLAlchemy fjerner den risiko.
