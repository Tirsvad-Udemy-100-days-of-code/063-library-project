[English](Step-4-Library-With-Database) · **Dansk** · [Bahasa Malaysia](Step-4-Library-With-Database-ms)

# Trin 4: bibliotekets hjemmeside med database

Nu gemmer hjemmesiden fra trin 1 sine bøger i SQLite. Forsiden viser alle bøger fra databasen med et link **Edit Rating** og et link **Delete**. Tilføj, ret og slet slutter alle med en omdirigering til forsiden.

## Sådan kører du det

Gør først miljøet klar, se [README](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/src/branch/main/README.md).

```bash
python -m library_project.main
```

## Skærmbilleder

![Skærmbillede 1](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-1-add-book.png)

![Skærmbillede 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-2-library-list.png)

![Skærmbillede 3](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-3-edit-rating.png)

![Skærmbillede 4](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-4-rating-changed.png)

![Skærmbillede 5](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/063-library-project/raw/branch/main/docs/images/step-4-5-book-deleted.png)

## Hvad vi lærte

- Hjemmesiden taler med et lager, så listen i hukommelsen og databasen kan byttes uden at ændre ruterne.
- En bogs id følger med i adressen (`/edit?id=3`, `/delete?id=3`).
- Efter en ændring omdirigerer vi til forsiden, så en opdatering af siden ikke gentager ændringen.
- En titel, der findes i forvejen, er en normal fejl, som læseren får at se, og et ukendt id giver 404.
- En test starter en ny app på den samme databasefil og viser, at bøgerne overlever en genstart.
