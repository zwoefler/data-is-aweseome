# 🤰 Abortions in Germany
- Learning about the Genesis-Database API ("Database of the
Federal Statistical Office of Germany")

- 🛑 STATE: DATA GATHERING BROKEN
- ✅ STATE: VISUALIZING DATA
- ℹ️ `Abtreibung = Abortion`


## 🏗️ How to use / Development?
- Clone repo: ```git@github.com:zwoefler/data-is-aweseome.git```
- Change directory: ```cd data-is-awesome/DATA_PROJECTS/abortions_in_germany/```

**PREREQUISITES**
Create a GENESIS-Account:
- 🔗 URL: https://www-genesis.destatis.de/genesis/online?Menu=RegistrierungForm&REGKUNDENTYP=001#abreadcrumb


Create a `.env` file. (Excluded from git by default. See `.gitignore`):
```BASH
API_USERNAME=<YOUR_GENESIS_USERNAME>
API_PASSWORD=<GENESIS_PASSWORD>
```

Actiavte Python3 Environment
```BASH
python3 -m venv Env
source Env/bin/activate
pip install -r requirements.txt
```

USING `JUPYTER NOTEBOOK` (INTERAVTICE)
```BASH
jupyter notebook
```

USING PYTHON SCRIPT.
```BASH
python3 scripts/get_abortions_in_germany.py
```

## 📊 Abortions
**Abortion Rate** is measured of the amount of `Abortion / Women in fertile age (15 - 44)`

Apparently it is more **common** in countries with **less legal acces** to Abortion.
Therefore the **WHO** estimates that *45% of abortions* are **unsafe** and *97%* of those are performed in *developing countries*.

Abortion Rates by Country 2023
- 🔗 URL :: https://worldpopulationreview.com/country-rankings/abortion-rates-by-country

---

1. Get [[DeStatis API]] account
2. Download Table: `**23311-0003:** Schwangerschaftsabbrüche: Deutschland, Quartale`
3. Get data into python
4. Visualize over years/quarters
5. Visualize with the amount of children being born
6. "Abortion-ratio". Abortions/Newborns


## 🚧 Problems
- 404 error when trying to pull data

## 📋️ Docs

### GENESIS API
By far the most complicated API I have ever seen :).
However, there is help in from the docs:

Link: https://www-genesis.destatis.de/genesis/misc/GENESIS-Webservices_Einfuehrung.pdf

Page 8.
2.1 Allgemeines
Der vorliegende RESTful-Webservice umfasst mehr als 40 Methoden, die auf die folgenden
Services aufgeteilt sind:
 HelloWorld: Methoden zum ersten Testen der API
Bsp: Test der Anmeldung im System mit den Zugangsdaten.
 Find: Methoden zum Finden von Informationen
Bsp: Tabellen mit Daten zu „Import“
 Cataloque: Methoden zum Auflisten von Objekten
Bsp: Tabellen aus der Statistik „Mikrozensus“
 Data: Methoden zum Herunterladen von Daten
Bsp: Tabelle „11111-0002 – Gebietsfläche: Kreise, Stichtag“
 Metadata: Methoden zum Herunterladen von Metadaten
Bsp: Statistik 11111 –Feststellung des Gebietsstandes
 Profile: Methoden zur Pflege des eigenen Accounts
Bsp: Passwort ändern.


The OpenAPI docs: https://destatis.api.bund.dev/

#### 🛠️ Steps
1. Create Destatis account: https://www-genesis.destatis.de/genesis/online?Menu=RegistrierungForm&REGKUNDENTYP=001#abreadcrumb

Nutzungsrechte/Copyright

© Statistisches Bundesamt 2023
Vervielfältigung und Verbreitung, auch auszugsweise, mit Quellenangabe gestattet.