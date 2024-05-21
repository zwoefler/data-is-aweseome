# Auslesen Parkleitsystem Gießen
Gather data form the parkhouse data system in Gießen.

## How?
Every 5 minutes. However the site isn't updated every day at 2100.
1. Download Page from: https://www.giessen.de/Umwelt_und_Verkehr/Parken/

## What and Where?
- `data/`: JSON dumps form the parkhouse data every 5 minutes
- `tests/`: Tests
- `parkhouse_aggregator/`: Python3 scripts
    1. Download the parkhouse data from Gießen Parkhouse Webapp
    2. Aggregate Parkhouse Data into parkhouses
- `parkhouse_data/`: JSON files with parkhouse occupation data for parkhouses


## What it should do?
A script `scraping_parkleitsystem.py` gathers all available json files from the `data/` directory.
The output format per parkhouse should be:
```JSON
// Dern-Passage.json
{
    "name": "Dern-Passage",
    "parkhouse_occupation": [
        {
            "timestamp": 09112023-0900,
            "max_spaces": 300,
            "occupied_spaces": 100,
            "fre_spaces": 200
        },
        {
            "timestamp": 09112023-0905,
            "max_spaces": 300,
            "occupied_spaces": 100,
            "fre_spaces": 200
        }
    ]
}
```

The `parkhouse_occupation` key is ordered by the `timestamp` in ascending order!
If the parkhouse data already exists:
- append the data to `parkhouse_occupation`


# 🚧 Work in Progress
1. Gather data form webpage - DONE
2. data is in format:
```json
{ "timestamp": "31102023-2045", "parkhouses": [ { "name": "Liebig-Center", "free_spaces": 242, "occupied_spaces": 8, "max_spaces": 250 }, { "name": "Neust\u00c3\u20acdter Tor", "free_spaces": 721, "occupied_spaces": 149, "max_spaces": 870 }, { "name": "Rathaus", "free_spaces": 165, "occupied_spaces": 85, "max_spaces": 250 }, { "name": "Selters Tor", "free_spaces": 147, "occupied_spaces": 11, "max_spaces": 158 }, { "name": "Westanlage", "free_spaces": 217, "occupied_spaces": 18, "max_spaces": 235 }, { "name": "Am Bahnhof", "free_spaces": 216, "occupied_spaces": 26, "max_spaces": 242 } ] }

```

Cleanup for each parkhouse:
```JSON
{
    "name": "Dern-Passage",
    "location": {
        "long": 123,
        "lat": 312
    },
    "data": [
        {
            "timestamp": 31102023-2045,
            "free_spaces": 147,
            "occupied_spaces": 11,
            "max_spaces": 158
        },
        {
            "timestamp": 31102023-2045,
            "free_spaces": 147,
            "occupied_spaces": 11,
            "max_spaces": 158
        }
    ]

}
```

Important questions:
- What type of timestapm does the visulaization need to work properly?
- Aggregate per hour for weekly, monthly or quarterly view?
