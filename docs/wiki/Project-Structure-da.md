[English](Project-Structure) · **Dansk** · [Bahasa Malaysia](Project-Structure-ms)

# Projektets opbygning og tests

Kildekoden er delt i fire lag i `src/library_project/`:

| Lag | Indhold |
| --- | --- |
| `domain` | `Book` og dens regler (titel, forfatter, bedømmelse). Den bruger ingen framework. |
| `application` | Brugstilfældene (tilføj, vis, ret bedømmelse, slet) og den lagringsport, de skal bruge. |
| `infrastructure` | Listen `all_books` i hukommelsen, SQLAlchemy-modellen `Book` og dens lager samt lektionsscripts. |
| `presentation` | Flask-ruterne `home`, `add`, `edit`, `delete` og Jinja-skabelonerne. |

`constants.py` indeholder alle fælles konstanter. `main_in_memory.py` og `main.py` bygger de to hjemmesider. Testene ligger i `tests/` og køres med `python -m pytest`. Skærmbillederne på siderne laves af `scripts/screenshots/capture_screenshot.sh`, som kører en browser uden vindue i en Docker-container, så der åbnes intet vindue på din skærm.

## Hvad vi lærte

- Forretningsreglerne afhænger ikke af Flask eller databasen, så de testes uden dem.
- Opgavens navne (`all_books`, `Book`, `db`, `home`, `add`, `edit`, `delete`) er bevaret, hvor de hører til.
- Skærmbillederne kan laves igen når som helst på samme måde i en container.
