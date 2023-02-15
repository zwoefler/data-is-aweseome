# Tesla Delivery Visualizer


## Order!
1. Get Waybackmachine URL: saveWebArchiveTeslaURLs.py
-
2. Read Model WaybackMachine URLs: downloadHistoricHTML.py model3_en_US_LinkList.json
3. extractJSONFromHTML.py
4. getTeslaModelData.py
5. aggregateModelData.py


## Problems
- Chinese Font/text isn't redenred correctly in images

## ToDos
- [ ] Get data for all regions available since "the beginning"
- [ ] Get data for China
- [ ] Include earliest delivery date into aggreagted data
- [ ] Include options: Name, Price, specs (range, accel)
- [X] Get List of available locales (getLocales.py)
- [X] Make price range from 0 to max!
- [X] Make timeline from earliest datapoint until latest
- [X] Combine ALL graphs i nthe same chart
- [X] Simplyfy script to get the price and date for a given model/trim
- [X] Stitch trim data together (All Long Range variants, all SR and so on)
- [ ] Write scipt that compares all available URLs from the Waybackmachine with the downloaded HTML and extracted JSON files!
- [ ] Use that script to exclude old URLs from being redownloaded!
- [ ] Combine steps of downloading HTML and extracting JSON without saving the HTML!
- [ ] Get visualization online!

## Stitching data together
A few problems:
- Datasaet includes non sold vehicles (Include flag #notSold)
- stitch together similar vehicles by price and date



---

## Scope
Collect all available Tesla Model data form the WaybackMachine.
Why?
- I don't need to build infrastructure to collect the data daily
- WaybackMachine has sufficient data
- Standardises the data gathering process
- Can still add it later on



# Info on used data
Our data is not 100% accurate and provides a trend overview, not a detailed analysis!
We gathered the data using the WebArchive and every single entry per tesla webpage for model and location.

The data is therefore offset to more recent dates, since the Webarchive
scrapped the webpages more frequently in recent times.
We cut out duplicate days and chose the first entry for a duplicate day.

A jump up in price on a specific date might have occured a few days before or after.
It could also be the case that certain price actions are simply missing from this data set!

Especially older dates (Pre 2018) couldn't (yet) been included!


## Limitations
The data is gathered automatically from the Wayback Machine which doesn't save the Tesla pages for every single day.

We download the data from the Wayback Archive.
For multiple saved pages for the same day we download the first saved instance and discard the others. Cutting out duplicates.

Our automation pipeline isn't yet able to gather "older" (pre 2018) data.
Working on that!

The data (currently) doesn't account for discontinued or currently unavailable models.
For example there used to be a "Model 3 Standard Range Plus" which became simply the "Model 3".
And the vehicle didn't magically decided it kicks off the "Standard Range Plus" Label.
It is simply the cheapest available option.
However, looking at the code we (currently) plot the vehicles price by it's identifier!
The Model 3 displayed in the design studio has the ID "$MT322" and the name "Model 3 Rear-Wheel Drive" but is displayed as "Model 3".
One of the earlier cheapest Model 3 offerings has the internal ID "$MT308" and the name "Standard Range Plus Rear-Wheel Drive".



Example:
There are 3 saves on Feb 08, the next saved date is Feb 13.
On Feb 08 the saves occured in the morning, evening and night.
Let's say there was a price increase on Feb 08 in the night.
We didn't capture that because we only take the first element for the day.
Only our next entry on Feb 13 first shows the price incease, even though it already occured 5 days ago.

This might reuslt in us showing a price-action on say Feb 13, when in reality the price change occured late on Feb 08.



# FAQ

### Why are there some missing values?
We use an automated process to count. We are not maniacs!
Many things can go wrong:
- Interrupted connection when downloading the data
- Gaps in our automation that don't catch all data representations
- We are NOT using live data. The timelag is about 2 days
- Using the Waybackmachine for "historic" data. The Waybackmachine didn't capture the webpage on every day

### Why is not every single day represented?
The data is downloaded from the WaybackMachine which doesn't save the pages for every single day.

### Why can there be missing price actions?
The WaybackMachine doesn't save the webpage every single day.
We automatically scrape the available pages from the Webarchive.
On potential errors while downloading we will skip the page.
Not every day is present in the dataset.
For example in late 2019 and early 2020 there are huge gaps of over a month.
Price action could have happened within these 4 weeks, which don't show up in the data!

### Why are you using the WaybackMachine?
If you know of a repository for the old price data of Tesla, contact us!
However the WaybackMachine is the only source we thought of that saves "historic" pages for tesla design studio.

### Why is there no "one price" for a given model?
Therea are different trims (All Wheel Drive, Rear Wheel Drive, Performance, etc.) and many variations including and excluding extras.
We simply want to show price moves in given vehicles and trims!
For example, the Tesla Model S Plaid was not avaialble outside the US shortly after it's launch and was only reintorduced one year later.
Similar happend for the Tesla Model 3 Long Range in the US. Also the stadard colors (free colors) changed throughout the years.

Calculating an average is not helpful.




# Errors

## Extracting JSON from HTML
Specify `html.parser` explicitly in the script
```
extractJSONFromHTML.py:35: GuessedAtParserWarning: No parser was explicitly specified, so I'm using the best available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on another system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 35 of the file extractJSONFromHTML.py. To get rid of this warning, pass the additional argument 'features="html.parser"' to the BeautifulSoup constructor.

  soup = bs4.BeautifulSoup(html)
```

## Could not extract JSON from (older) HTMLs
The older data is an HTML which doesn't immediately load the data.
It looks like a Embedded JavaScript or Embedded Ruby Template.

Maybe load them individually and extract JSON form the HTML directly...

html_raw_en_US_models_20171211020721.html does not contain valid JSON!
