# Data is Awesome
Opinionated visualized data and answered questions with data!

Whatever comes to mind.

## 📏 Rules

- Datasources must be publicly available
- No paywalls, or a way to climb ober it...
- Script(s) lead from data download to final JSON-file (data)
- Datafolder stores data in a data/ directory 
- Data sources have a README explaining the context

The README must:
- State the research question
- Answer the questions from the next chapter (Data)

## ToDos
- [ ] Add CONTRIBUTING.md + rules
- [ ] Refine Mission statement
- [ ] External Data storage - not all in the Git repo
- [ ] Docs - for (sub)project with Tutorial, How-To, requirements
- [ ] Add Docker containers per project to run data visuals
- [ ] Every project with it's own visualization?

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
I usually look at data to answer a question or settle an argument.
That context lives throughout the analysis and visualization.
Answering simple questions may result in consulting 5 different datasources.

Those sources have differing viewpoints and limitations which MUST be explained!
Nowadays there is so much data, but even more that hasn't been correlated in a clera and concise matter.

EXAMPLE:
Why were there more car accidents on a given Autobahn-segment?
One possible answer might be the recently lifted speedlimit. (We have sections without speedlimits here)
After all, higher speeds = more crashes?

However, looking at the data you might realize most crashes occur at speeds far below the speedlimit.
Correlating that observation with the usage (aka capacity) of that segemtn may lead to the far simpler "The street is simply overrun", explaining the lower speeds and the amount of accidents.


## Why JSON?
- Easy to manage 
- Don't know beforehand what data is available 
- Don't want to use a database...

JSON is good enough

## External dependencies?
Most data gathering and anaylsis is done using Python3 and some packages.
Every folder has a `requirements.txt` and should be used with a virtual environment.

## Contributing
- Create a Pull Request
- 
