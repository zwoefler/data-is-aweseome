# CO2 Emissions for given Electricity sources

🛑 STATE: BROKEN

The package `tabula-py` needs Java...
```BASH
JavaNotFoundError: `java` command is not found from this Python process.Please ensure Java is installed and PATH is set for `java`
```

## 🎯 Goals / Learnings
- Reading data from PDFs with Python3
- Create a visualization of Lifecycle-Emissions with Min/Median/Max
- Get the whole table as JSON to visualize

## 🏗️ Usage
- Clone repo: ```git@github.com:zwoefler/data-is-aweseome.git```
- Change directory: ```cd data-is-awesome/DATA_PROJECTS/average_abitur_grades/```

```BASH
python3 -m venv Env
source Env/bin/activate
pip install -r requirements.txt

python3 extract_co2_emissions/plotting_co_emissions.py
```

## 🚀 Improvements
Make separate components:
- Data Gathering from PDF
- Clean Data
- Export Data
- Visualize Data


## 🚧 Problems
- Have the report automatically download, so data gathering actually works


## 📚️ Resources

From the IPCC 2014 AR-5 report on page 1353
🔗 URL: https://www.ipcc.ch/site/assets/uploads/2018/02/ipcc_wg3_ar5_full.pdf#page=1353

## ToDo
- Add Download PDF for IPCC report as Python script
- Add Title "Electricity CO2-Emissions - IPCC 2014 AR-5 report"


