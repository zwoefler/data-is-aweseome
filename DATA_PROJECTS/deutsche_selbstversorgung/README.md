# Deutsche Selbstversorgung
With the agricultural sector fighting to keep their subsidies, some people ask why the "Selbstversorgungsgrad" aka "how much stuff do we actually produce ourselves", is perceived low for vegetables and fruit.

🛑 STATE: BROKEN (On so many levels)

Show the "Selbstversorgungsgrad" for:
- Agricultural products
- Oil & Gas
- Electricity
- Raw materials
- etc.


| Created     | Updated | Data Collection | Data Processing | Visualization |
| ----------- | ------- | --------- | --------- | -------------- |
| 📆 09.01.24 | 📆      | 🛑 BROKEN | 🛑 BROKEN | 🛑 BROKEN |


# 🚀 Vision / Outcome
- Have datasource available as link
- Automated process to retrieve cleaned up data as dataframe
- Visualize all in same chart (percentages)

- Provide sources to explanations why the numbers are the way they are.

## 🛠️ Setup
```BASH
python3 -m venv Env
source Env/bin/activate
pip install -U pip
pip install -r requirements.txt
```


## 🏗️ How to use / Development?
```BASH
python3 poc_plot_selbstversorgung.py
```

## 🚧 Problems
- Freaking `tabula-py` requres Java...


## 📚️ Resources
Der Selbstversorgungsgrad: Wie ist es um die Versorgung mit Lebensmitteln in Deutschland bestellt?
🔗 URL: https://www.landwirtschaft.de/landwirtschaft-verstehen/wie-funktioniert-landwirtschaft-heute/markt-und-handel/der-selbstversorgungsgrad-wie-ist-es-um-die-versorgung-mit-lebensmitteln-in-deutschland-bestellt

Versorungsbilanzen DE
🔗 URL: https://www.bmel-statistik.de/ernaehrung-fischerei/versorgungsbilanzen#c8618

Warum ist der Selbstversorgungsgrad bei Obst und Gemüse in Deutschland so niedrig.
🔗 URL: https://www.heimischelandwirtschaft.de/aktuelles/warum-ist-der-selbstversorgungsgrad-bei-obst-und-gemuese-deutschland-so-niedrig-interview


📊 DATA:
Selbstversorgungsgrad Obst & Gemüse 2010/11 - 2020/21 vorläufig
🔗 URL: https://www.bmel-statistik.de/fileadmin/daten/0070010-0000.pdf

Selbstversorgungsgrad - Landwirtschaftliche Erzeugnisse - Excel file
🔗 URL: https://www.bmel-statistik.de/fileadmin/daten/4010200-0000.xlsx


Selbstversorgungsgrad von Gemüsen nach Arten
🔗 URL: https://www.bmel-statistik.de/fileadmin/daten/0070012-0000.pdf

---

Erdöl-Förderung Deutschland:
🔗 URL: https://www.bveg.de/die-branche/erdgas-und-erdoel-in-deutschland/erdoel-in-deutschland/

Erdgasförderung Deutschland:
🔗 URL: https://www.bveg.de/die-branche/erdgas-und-erdoel-in-deutschland/erdgas-in-deutschland/

---