# Volební scraper 2017

Program slouží ke stažení výsledků parlamentních voleb z roku 2017 přímo z webu volby.cz a jejich uložení do CSV souboru.

---

## Co budeš potřebovat

- Python 3.10 nebo novější
- Nainstalované knihovny ze souboru `requirements.txt`

---

## Instalace

Nejdřív si vytvoř virtuální prostředí:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Linux / macOS:
source venv/bin/activate
```

Pak nainstaluj závislosti:

```bash
pip install -r requirements.txt
```

---

## Jak spustit

```bash
python projekt_3.py
```

Program automaticky stáhne data pro územní celek Prostějov a uloží je do souboru `vysledky_prostejov.csv`.

---

## Struktura výstupního souboru

Každý řádek v CSV odpovídá jedné obci a obsahuje tyto údaje:

- `code` – kód obce
- `location` – název obce
- `registered` – počet voličů v seznamu
- `envelopes` – počet vydaných obálek
- `valid` – počet platných hlasů
- další sloupce – hlasy pro jednotlivé kandidující strany

**Ukázka:**
```
code,location,registered,envelopes,valid,Občanská demokratická strana,...
589268,Bedihošť,834,527,524,51,...
589276,Bílovice-Lutotín,431,279,275,13,...
```
