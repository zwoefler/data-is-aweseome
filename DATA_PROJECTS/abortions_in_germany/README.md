# 🤰 Abortions in Germany
Can't remember the reason.
But learning about the Genesis-Database API ("Database of the
Federal Statistical Office of Germany") might prove useful lateron.

🛑 STATE: DATA GATHERING BROKEN
✅ STATE: VISUALIZING DATA

Abtreibung= Abortion

1. Get abortion data from destatis/genesis online database
2. Visualize



## 📊 Abortions
**Abortion Rate** is measured of the amount of `Abortion / Women in fertile age (15 - 44)`

Apparently it is more **common** in countries with **less legal acces** to Abortion.
Therefore the **WHO** estimates that *45% of abortions* are **unsafe** and *97%* of those are performed in *developing countries*.

Abortion Rates by Country 2023
- 🔗 URL :: https://worldpopulationreview.com/country-rankings/abortion-rates-by-country

---

1. Get [[DeStatis API]] account
2. Download Table **23311-0003:** Schwangerschaftsabbrüche: Deutschland, Quartale
3. Get data into python
4. Visualize over years/quarters
5. Visualize with the amount of children being born
6. "Abortion-ratio". Abortions/Newborns



## 🏗️ How to use / Development?
After checking out this repo, and changing into this directory `abortions_in_germany` follow the instructions below.

You need to create a GENESIS account:
- 🔗 URL: https://www-genesis.destatis.de/genesis/online?Menu=RegistrierungForm&REGKUNDENTYP=001#abreadcrumb

Create a `.env` file in the project directory:
```BASH
API_USERNAME=<YOUR_GENESIS_USERNAME>
API_PASSWORD=<GENESIS_PASSWORD>
```

Actiavte Python3 Environment
```BASH
# Activate Python environment
python3 -m venv Env
source Env/bin/activate
pip install -r requirements.txt

# Have you create your .env file with GENESIS credentials?
```


USING `JUPYTER NOTEBOOK` (INTERAVTICE)
```BASH
# Start Jupyter Notebook
jupyter notebook
```


USING PYTHON SCRIPT.
```BASH
# Visualizes data in your browser
python3 abortions_in_germany/get_abortions_in_germany.py
```

## 🚧 Problems
- 404 error when trying to pull data
-


## 📋️ Docs

### GENESIS API
This is by far the most complicated API interface and usage I have ever seen :). However, there is some help from the folks in this docs:

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


---