[English](Step-1-In-Memory-Library) · **Dansk** · [Bahasa Malaysia](Step-1-In-Memory-Library-ms)

# Trin 1: bøger i en liste i hukommelsen

Den første hjemmeside gemmer alle bøger i listen `all_books`. Hver bog er en ordbog med titel, forfatter og bedømmelse. Forsiden viser bøgerne eller teksten "Library is empty." og et link til siden, hvor man tilføjer en bog.

## Sådan kører du det

Gør først miljøet klar, se [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.main_in_memory
```

## Skærmbilleder

![Skærmbillede 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-1-home.png)

![Skærmbillede 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-2-add-form.png)

![Skærmbillede 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-3-add-book.png)

![Skærmbillede 4](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-4-book-list.png)

![Skærmbillede 5](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-1-5-empty-library.png)

## Hvad vi lærte

- En Flask-rute er en Python-funktion med en dekorator, og funktionens navn kan bruges til at lave links.
- En Jinja-skabelon kan løbe en liste igennem og vælge med `if`/`else`, så et tomt bibliotek får sin egen besked.
- En formular sender data med `POST`, og Flask læser dem med `request.form`.
- Data i en variabel går tabt, når programmet stopper. Derfor har vi brug for en database.
