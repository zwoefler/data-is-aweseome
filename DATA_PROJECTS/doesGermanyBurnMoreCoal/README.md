# Does Germany burn more coal for electricity generation after shutting down nuclear?

Germany phased out Nuclear energy as a source for electricity.

Now that nuclear is missing in the electricity mix some people worry that:
1. We will burn more Coal now
2. Emit more CO2 emissions because a low carbon electricity source is missing
3. There is not enough electricity
4. Nuclear Powerplants should have continued to run
All above statements are false.

| Created     | Updated | Data Collection | Data Processing | Visualization |
| ----------- | ------- | --------- | --------- | -------------- |
| 📆 09.01.24 | 📆 09.09.24 | 🚧 Incomplete | ✅ WORKS | ✅ WORKS |

> ℹ️ Datasource has missing data between mid November 2023 and January 2024

- `coal_data.json` - Aggreagted coal production data over the years
- `search_urls.json` - download links for json data


## 🏗️ Usage
- Clone repo: ```git@github.com:zwoefler/data-is-aweseome.git```
- Change directory: ```cd data-is-awesome/DATA_PROJECTS/doesGermanyBurnMoreCoal/```

```BASH
python3 -m venv Env
source Env/bin/activate
pip install -r requirements.txt

python3 scripts/create_download_links.py
python3 scripts/pull_energy_charts_data.py
python3 scripts/generate_coal_data.py

# See longterm coal trend!
python3 scripts/long_ter_coal_overlook.py

# See 2023 coal production
python3 scripts/yearly_coal_comparison_2023.py
```

---

## Deutschland = Strombettler?
- Electricity production in Germany
- Imports
- Imports France & Poland

---

This decision has been in the making since the early 2000s, was reaffirmed in the early 2010s, after the Nuclear Powerplant in Fukushima, Japan had an accident.

The phaseout was scheduled for late 2022.

But the Invasion of Russia into Ukraine, some energy concerns in France and the political climate demanded the ramaining 3 power plants

- Emsland
- Neckarwesthelm 2
- Isar 2

to run until 15. April 2023.



# The arguments

In 2021, when 6 nuclear power plants were still running it made up 12,6% (65,4 TWh) of Germanys electricty production.

In 2022 it was 6,4% (32,7 TWh).

# 📜 The History

SInce 2002 the consturction of new Nuclear Powerplants was prohibited.

In 2011 on 14.03.2011, three days after the Fukushima accident 7 Nuclear Powerplants were turned off.
-   Biblis A und Biblis B,
-   Brunsbüttel,
-   Isar 1,
-   Neckarwestheim 1,
-   Unterweser und
-   Philippsburg 1.

In the following years 2015, 2017 and 2019 three more Nuclear Powerplants were shut down.
-   Grafenrheinfeld,
-   Gundremmingen B,
-   Philippsburg 2

During 2021 three more Nuclear Powerplants were taken from the grid, leaving only 3 remaining. Keep in mind this was BEFORE Russia invaded the Ukraine! So before the "Energycrisis".

Therefore each year these powerplants were taken from the grid, the electricity needed to be substituted!

Now on 15. April 2023 the remaining three Nuclear Powerplants were shut down.
-   [Isar 2](https://www.base.bund.de/DE/themen/kt/ausstieg-atomkraft/abschaltung-akw/2022/die-drei-letzten-akw.html;jsessionid=74C6437DE0AD927E842C003365C7B8F8.internet942 "Abschaltung der Atomkraftwerke Isar 2, Emsland & Neckarwestheim 2 (Öffnet neues Fenster)"),
-   [Emsland](https://www.base.bund.de/DE/themen/kt/ausstieg-atomkraft/abschaltung-akw/2022/die-drei-letzten-akw.html;jsessionid=74C6437DE0AD927E842C003365C7B8F8.internet942 "Abschaltung der Atomkraftwerke Isar 2, Emsland & Neckarwestheim 2") und
-   [Neckarwestheim 2](https://www.base.bund.de/DE/themen/kt/ausstieg-atomkraft/abschaltung-akw/2022/die-drei-letzten-akw.html;jsessionid=74C6437DE0AD927E842C003365C7B8F8.internet942 "Abschaltung der Atomkraftwerke Isar 2, Emsland & Neckarwestheim 2").

Bullet Point History of Nuclear Phase out in Germay
🔗 URL :: https://www.base.bund.de/DE/themen/kt/ausstieg-atomkraft/ausstieg.html


# The Rebuttals

Let's start with the last argument.
Keep in mind the electricity grid, market and production is complicated and are three seperate "things".

For example:
Many industries produce their own energy, that is NOT sold or avaialble to the "public" and not part of the electricity grid.
Partly the Power Plant in Wolfsburg by VW produces electricity for it's factory and heat energy for the city.


Furthermore there are diffreent values for the "same" metric.
According to the "BNetzA", the grid provider for Gas, Electricity, Mail-Service and Train-Network there was a Net-Energyproduction of
506,8 TWh

| Year | Net Electricity Production (BNetzA) | Grid Feed (Statistics Office)    |
| ---- | ----------------------------------- | --- |
| 2021 | 505 TWh                             | 519,4 TWh    |
| 2022 | 506,8 TWh                           |  509,4 TWh   |

🔗 URL :: https://www.destatis.de/DE/Presse/Pressemitteilungen/2023/03/PD23_090_43312.html

🔗 URL :: https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/DE/2023/20230104_smard.html

## Nuclear Powerplants should have continued to run
The Nuclear Powerplants should have continued to run until the "Energycrisis" is over.


Makes sense, why wouldn't you continue running something that works, makes you less dependent on CO2 intensive coal and have for some people a peace of mind?

Well, the nuclear phase out is exactly that... a phase out and not a switch.

The supply chains for the nuclear inustry in Germany have been disassembled over the past decades. Letting the nuclear power plants continue to run is a "stretching operation" where the remaining fuel rods will be used over a longer time, but NOT yield more energy.
With each day the power from those rods will decline.

The problem here is beisdes the fact that no new rods were ordered, the operators of the Nuclear Powerplants don't want to take responsibility over the inital phase out date.
Furthermore the last security check for the remaining three power plants was skipped in 2019.
The last security check was over 13 years ago.


## 📚️ Sources

Nulcear Phaseout in Germany on 15. April 2023
🔗 URL: https://www.br.de/nachrichten/deutschland-welt/atomausstieg-was-sie-zur-akw-abschaltung-wissen-muessen,TbI9xYU

Electricty Geenration Germany 2021 vs. 2022
🔗 URL: https://www.destatis.de/DE/Presse/Pressemitteilungen/2023/03/PD23_090_43312.html



Criticism for nuclear phase out in Germay
🔗 URL: https://www.zdf.de/nachrichten/wirtschaft/dihk-atomausstieg-energiekosten-100.html

 Bundestag beschließt AKW-Laufzeitverlängerung bis Mitte April 2023 (11.11.2022)
🔗 URL :: https://www.bundestag.de/dokumente/textarchiv/2022/kw45-de-atomgesetz-freitag-917474

"Stretching Operation" - Why the phaseout will happen in April 2023
🔗 URL :: https://www.tagesschau.de/inland/atomenergie-streckbetrieb-103.html

VW - Powerplant in Wolfsburg, under the point "Energy"
🔗 URL :: https://www.volkswagen-newsroom.com/de/volkswagen-ag-werk-wolfsburg-6811
