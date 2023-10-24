# Auslesen Parkleitsystem Gießen
Daten sammeln zur Auslastung des Parkleitsystems

## Wie?
Every minute
1. Download Page from: https://www.giessen.de/Umwelt_und_Verkehr/Parken/
2. Write logs with


# How to?
- Run every five minutes to build a dataset
- Have the resulting file as a JSON in the data/ directory!

- Build GitHub Action every five minutes
- Run scrape_parkleitsystem.py --> data to <timestamp.json>, if timestamp.json already exists, skip
