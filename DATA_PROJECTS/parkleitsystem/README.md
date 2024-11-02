# Auslesen Parkleitsystem Gießen
The data is sourced from the **Universitätsstadt Gießen**.
The dataset includes information from their parking guidance system (`Parkleitsystem`).

🔗 URL: https://www.giessen.de/Umwelt_und_Verkehr/Parken/

<div align="center">
  <img src="https://www.giessen.de/layout/giessen2017/assets/img/giessen-logo.png" alt="Universitätsstadt Gießen Logo" width="150"/>
</div>


## 🚀 Usage
The `scraping_parkleitsstem.py` pulls the last updated parkhouse occupational data form the webpage and prints it as JSON fromat to the console
```SHELL
python3 scraping_parkleitsstem.py
```

**🏗️ How to use / Development?**
Changed into `DATA_PROJECTS/parkleitsystem/`?
```BASH
# Create / Activate Python Virtual Environment
python3 -m venv Env
# source Env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Get last updated data in JSON format
python3 scraping_parkleitsystem.py
```

## The data format
```JSON
{
  "timestamp": "ddmmyyyy-hhmm",
  "parkhouses": [
    {
      "name": "NAME",
      "free_spaces": INT,
      "occupied_spaces": INT,
      "max_spaces": INT
    },
    {
        ...
    }
  ]
}
```


## What and Where?
- `data/`: JSON dumps form the parkhouse data approx. every 5 minutes
- `tests/`: Tests
- `parkhouse_aggregator/`: Python3 script that aggregate the raw data from `data/` per parkhouse
    - `parkhouse_aggregator.py`: Aggregates the raw data from `data/` per parkhouse into the `parkhouse_data/` directory
- `parkhouse_data/`: JSON files with parkhouse occupation data for parkhouses

## 🚧 Limitations
- The webpage from which the data is sources usually updates only between 9 in the morning and evening. So nightly changes are not included
- Some large parkhouses in Gießen are not present in the dataset
- Parkhouses that are closed will sometimes not be updated on the webpage (Parkhaus "Am Kino")


## How to include dataset on webpage?
1. Aggregate parkhouse data: Run `python3 parkhouse_aggregator/parkhouse_aggregator.py`
2. Copy `parkhouse_data/` to assets in WEBPAGE folder: `cp parkhouse_data/*.json ../../WEBPAGE/assets/parkhouses/`
