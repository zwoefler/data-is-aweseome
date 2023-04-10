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



1. Download Zips
- Zips to Excel in Excel folder
-



## User Stories
GIVEN: I provide a KMK.org link
WHEN: My functions exectues
THEN: I have a list of zip links
- As a User for providing KMK-links I receive a list of links to download zips
- As a User I want the average grade data from a list of links of KMK.org
- As a User I receive a bunch of Excel-files for given KMK.org links
- As a User I want to provide a list of zip files and be returnd Excel-files
- A User provides a list of KMK links and returns a JSON Object
- A User can provide a KMK-link and returns a JSON with zip links to download
- A User can provide a list of zip-links and download them to drive
- A User provides a list of excel files parsed to JSON
- A User