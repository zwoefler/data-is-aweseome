# Average Abitur Grades in Germany since 2006
https://www.kmk.org/dokumentation-statistik/statistik/schulstatistik/abiturnoten.html

Visualizing the data for the Average Abitur grades in Germany.
Stuff we want to see:
- Average Grades over time (total, state)
- Histograms over years of grades (total, state)



## 1. Step
Average grades in Germany since 2006

## Design
Have a JSON-file with all years since earliest on KMK.org available.
The data should have:
- Grades (1.0 - 4.0) for every state
- Grades (1.0 - 4.0) for Germany (total)
- Average Grade for given year per state and total

The JSON format:
```
{
    years: [2006, ..., 2022]
    grades: {
        total: [1.2, ..., 3.2],
        bw: [1.2, ..., 3.2],
        nw: [1.2, ..., 3.2],
    },
    distribution: {
        total: {
            1.0: 56,
            1.1: 127,
            ...
            4.0: 24
        },
        bw: {
            1.0: 56,
            1.1: 127,
            ...
            4.0: 24
        },
        nw: {
            1.0: 56,
            1.1: 127,
            ...
            4.0: 24
        },
    }
}
```


1. Download Zips
- Zips to Excel in Excel folder
-