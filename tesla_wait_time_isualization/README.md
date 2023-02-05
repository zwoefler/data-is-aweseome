# Tesla Delivery Visualizer


## Scope
Collect all available Tesla Model data form the WaybackMachine.
Why?
- I don't need to build infrastructure to collect the data daily
- WaybackMachine has sufficient data
- Standardises the data gathering process
- Can still add it later on



## Info on used data
Our data is not 100% accurate and provides a trend overview, not a detailed analysis!
We gathered the data using the WebArchive and every single entry per tesla webpage for model and location.

The data is therefore offset to more recent dates, since the Webarchive
scrapped the webpages more frequently in recent times.
We cut out duplicate days and chose the first entry for a duplicate day.

A jump up in price on a specific date might have occured a few days before or after.
It could also be the case that certain price actions are simply missing from this data set!


## Limitations
The data is gathered automatically from the Wayback Machine which doesn't save the Tesla pages for every single day.
= price increases might have occured a few days before the date the visualizations shows.
Why? -You might ask

We download the data from the Wayback Archive.
If there are mutliple saved pages for the same day we simply download the first saved instance and discard the other ones.
Cutting out duplicates.


Example:
There are 3 saves on Feb 08, the next saved date is Feb 13.
On Feb 08 the saves occured in the morning, evening and night.
Let's say there was a price increase on Feb 08 in the night.
We didn't capture that because we only take the first element for the day.
Only our next entry on Feb 13 first shows the price incease, even though it already occured 5 days ago.

This might reuslt in us showing a price-action on say Feb 13, when in reality the price change occured late on Feb 08.

#### Why is not every single day represented?
The data is downloaded from the WaybackMachine which doesn't save the pages for every single day.

#### Why can there be missing price actions?
The WaybackMachine doesn't save the webpage every single day.
We automatically scrape the available pages from the Webarchive.
On potential errors while downloading we will skip the page.
Not every day is present in the dataset.
For example in late 2019 and early 2020 there are huge gaps of over a month.
Price action could have happened within these 4 weeks, which don't show up in the data!

#### Why are you using the WaybackMachine?
If you know of a repository for the old price data of Tesla, contact us!
However the WaybackMachine is the only source we thought of that saves "historic" pages for tesla design studio.

#### Why is there no "one price" for a given model?
Therea are different trims (All Wheel Drive, Rear Wheel Drive, Performance, etc.) and many variations including and excluding extras.
We simply want to show price moves in given vehicles and trims!
For example, the Tesla Model S Plaid was not avaialble outside the US shortly after it's launch and was only reintorduced one year later.
Similar happend for the Tesla Model 3 Long Range in the US. Also the stadard colors (free colors) changed throughout the years.

Calculating an average is not helpful.



