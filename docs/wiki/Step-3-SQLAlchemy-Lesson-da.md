[English](Step-3-SQLAlchemy-Lesson) · **Dansk** · [Bahasa Malaysia](Step-3-SQLAlchemy-Lesson-ms)

# Trin 3: SQLAlchemy-lektionen

SQL-tekst er let at skrive forkert, og en tastefejl opdages først, når koden kører. SQLAlchemy er en ORM: en tabel er en Python-klasse, en række er et objekt, og en kolonne er en egenskab. Tabellen `books` beskrives nu af klassen `Book`.

## Sådan kører du det

Gør først miljøet klar, se [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.infrastructure.lessons.sqlalchemy_lesson create
python -m library_project.infrastructure.lessons.sqlalchemy_lesson read
```

## Skærmbilleder

![Skærmbillede 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-1-sqlalchemy-create.png)

![Skærmbillede 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-2-sqlalchemy-read.png)

![Skærmbillede 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-3-sqlalchemy-update.png)

![Skærmbillede 4](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-3-4-sqlalchemy-delete.png)

## Hvad vi lærte

- `db.create_all()` opretter tabellerne ud fra modellen inde i Flask-appens kontekst.
- Opret: `db.session.add()` og `commit()`. Læs: `db.select()` med `scalars()` til mange rækker og `scalar()` til én.
- Ret: ændr egenskaben på et indlæst objekt og gem.
- Slet: `db.session.delete()` og gem. Et id, der ikke findes, håndteres som en fejl og ikke som et nedbrud.
