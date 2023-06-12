# Average Abitur Grades in Germany since 2006
https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html

Visualizing the data for the Average Abitur grades in Germany.
Stuff we want to see:
- Average Grades over time (total, state)
- Histograms over years of grades (total, state)


## Design
Have a JSON-file with all years since earliest on KMK.org available.
The data should have:
- Grades (1.0 - 4.0) for every state
- Grades (1.0 - 4.0) for Germany (total)
- Average Grade for given year per state and total



## Requirements
- Each selection "BW" - must hvae corresponding name "Baden Würtemberg"
- Each state has it's own datarow [2.25, 2.20, 2.19, etc.]


## ToDo
Change dataset:
Filter for Average Grades:
```
years: [],
average_grade: {
    "Total": [],
    "BW": []
}
```

- Data order in the JSON is weird! Years should probably always be together with the data for easier visualization