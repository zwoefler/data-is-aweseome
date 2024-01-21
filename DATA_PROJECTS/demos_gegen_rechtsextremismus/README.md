# Demos gegen Rechtsextremismus

In the days after the release of the [Correctiv research](https://correctiv.org/aktuelles/neue-rechte/2024/01/10/geheimplan-remigration-vertreibung-afd-rechtsextreme-november-treffen/) regarding plans by the right wing party AfD many protests occured in Germany.
This project aims to visulaize them all, initially focussing on protests in Hessen.



🔗 URL: <POTENTIAL LINK>

| Created | Updated | Data Collection | Data Processing | Visualization |
| ------- | ------- | --------- | --------- | -------------- |
| 📆 21.01.24     | 📆      | 🛑 BROKEN | 🛑 BROKEN | 🛑 BROKEN |


# 🚀 Vision / Outcome
- Map of all protests that were organised after the release of Correctiv research in Hessen
- Show amount of participants per city
- Show date
- Show info/sources/comments
- Animate on a timescale


# 📋️ Docs
## 🛠️ Setup
Activate Python3 Environment
```BASH
python3 -m venv Env
source Env/bin/activate
pip install -U pip
pip install -r requirements.txt
```


## 🏗️ How to use / Development?
```BASH
python3 your_python_project/
```

1. Create .env file and put "OPENCAGE_API_KEY" in there
2. Get your key from https://opencagedata.com. Create an account and paste APi key to .env file
3.

## 🔍️ Dataset exploration

Dataformat:
```CSV
|City|Date|Participants|Comments|Sources|
|---|---|---|---|---|
```

## Data Collection
Collecting data by hand. Skimming through articles.
Only use the police numbers!

## Data Processing
Filter by cities in Hessen first!
Order by date

## Data Visualization
1. Start with a map and basic pins on it


## ❓️ Questions
- WHERE is the data valid?
- WHEN is the data valid?
- WHO ordered/comissioned/gathered the data?
- HOW was the data gathered?
- WHAT is the public source?



## 🚧 Problems
- How to select only cities in Hessen from the dataset?
- What data (lat/long) does the visualization need?


- ImportError: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
> `pip install openpyxl`

## 📚️ Resources
🔗 URL: https://www.hessenschau.de/gesellschaft/rund-70000-hessen-bei-demos-gegen-afd-und-rechtsextremismus-v14,demos-gegen-rechts-100.html
🔗 URL: https://www.tagesschau.de/inland/regional/hamburg/hamburg-demonstration-rechtsextremismus-100.html
🔗 URL: https://www.gnz.de/lokales/main-kinzig-kreis/gelnhausen/gelnhausen-hand-aufs-herz-kuendigt-demo-gegen-rechts-an-3V4K3DMAWVGEZE2VUVTD2JXS2Y.html?outputType=valid_amp
🔗 URL: https://www.dgb.de/themen/++co++5bab75ee-b521-11ee-bea4-001a4a160123#uuid-e6200bd0-b527-11ee-a000-001a4a160123



