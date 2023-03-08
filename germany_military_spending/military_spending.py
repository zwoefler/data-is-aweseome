import requests
import os
import pandas as pd

# get bip germany
# get percentages of military spending vs. german gdp

# gdp_dataframe
df = pd.read_html("gdp_germany_table.html")[0]

# percentage military spending df
percentage_df = pd.read_csv("military_spending_percentage_gdp.csv")
print(percentage_df)
