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