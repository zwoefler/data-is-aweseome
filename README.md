# Data is Awesome
Opinionated visualized data and answered questions with data!

Whatever comes to mind.

## 📏 Rules

- Datasources must be publicly available
- No paywalls
- Script(s) lead from data download to final JSON-file (data)
- Each datafolder stores the data in a data/ directory 
- Data sources have a README explaining the context

The README must:
- State the research question
- Answer the questions from the next chapter (Data)


##  Data
All Data has a README answering the following questions:
- WHERE is the data valid? (City, Country, Continent, Celestial Body)
- WHEN is the data valid? (Far gone time period, valid today + estimates in the future?
- WHO ordered/comissioned/gathered the data?
- HOW was the data gathered? (Survey (participants), counting hand vs. technical)
- WHAT is the public source? A link or links with an explanation should the data be aggreageted.

### Data Explanations
#### Absolute vs. Percentage? 
A company like Meta might grow slowly at just under 3% new User Account growth.
But those 3% are about 100 million accounts created yearly. The scale is massive!

#### Average or Median?
Income data can be heavily skewed. 
An increase in average salary of 10% can mean nothing to most people in that population.
Looking at the median, the value in the middle, might reveal massiv income increases went only to a hand full of people.

This effect also works in the oposite direction.
Average CO2-Emissions for some energy-sources is usually lower than the median, indicating there are a few heavy outliers!


---

# ❓️ Questions
## Why opinionated?
Most data gathered and analysed is a reaction to an argument. 
Furthermore answering a simple question can result in consulting 5 diferent datasources and weighing their implications.
Those implications must be explained and come from a firm conviction/opinion.

Nowadays there is so much data out there which in some cases is not correalted with other important data to give an answer to your question.

Why were there more car accidents on that Autobahn-segment?
Some might answer: because of a lifted speedlimit which leads to more accidents.
However, realizing the accidents occur at slow speeds and correlating them with the usage of the road one might conclude it is mainly a street running over capacity.


## Why JSON?
- Easy to manage, 
- don't know beforehand what data is available 
- and don't want to use a database...

JSON is good enough and well supported

## External dependencies?
Most data gathering and anaylsis is done using Python3 and some packages.
Every folder has a requirements-file and should be used with a virtual env

## Contributing?
- Create a Pull Request
