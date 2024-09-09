import requests
import pandas as pd
from io import StringIO
from dotenv import load_dotenv
import os

load_dotenv()


def getTableWithInfo(id):
    req = {
        "username": os.getenv("API_USERNAME"),
        "password": os.getenv("API_PASSWORD"),
        "name": id,
        "area": "all",
        "compress ": "false",
        "transpose": "false",
        "job": "false",
        "stand": "01.01.1970 01:00",
        "language": "en",
    }
    url = "https://www-genesis.destatis.de/genesisWS/rest/2020/data/table"
    resp = requests.get(url, params=req)
    return resp


def getColumns(response):
    columns = []
    for column in response.json()["Object"]["Structure"]["Columns"]:
        columns.append(column["Content"])

    return columns


def getIndex(response):
    index_list = []
    for index in response.json()["Object"]["Structure"]["Rows"]:
        index_list.append(index["Content"])
        for subindex in index["Structure"]:
            index_list.append(subindex["Content"])

    return index_list


def tableDFAndInfo(tableID):
    table_resp = getTableWithInfo(tableID)
    print(table_resp)
    table_csv = StringIO(table_resp.json()["Object"]["Content"])
    columns = getColumns(table_resp)
    index = getIndex(table_resp)
    names = index + columns
    title = table_resp.json()["Object"]["Structure"]["Head"]["Content"]
    resp_df = pd.read_csv(table_csv, delimiter=";", header=0, names=names)
    return resp_df, index


def reindexDfWithDates(df):
    """Creates a list with first day of each quarter"""
    quarters = []
    for year, quarter in df[df.columns[:2]].values:
        if quarter == "Quarter 1":
            quarters.append(f"{year}-01-01")
        elif quarter == "Quarter 2":
            quarters.append(f"{year}-04-01")
        elif quarter == "Quarter 3":
            quarters.append(f"{year}-07-01")
        elif quarter == "Quarter 4":
            quarters.append(f"{year}-10-01")

    period_index = pd.PeriodIndex(quarters, freq="Q").to_timestamp()
    return period_index


def keepOnlyNumbers(df):
    df = df.apply(pd.to_numeric, errors="coerce")
    df = df[~pd.isna(df[df.columns[0]])]
    return df


tableID = "23311-0003"
resp_df, index = tableDFAndInfo(tableID)
df = resp_df.dropna()
df.index = reindexDfWithDates(df)
df.drop(["Year", "Quarters"], axis=1, inplace=True)
df = keepOnlyNumbers(df)

df.to_csv(f"data/{df.columns[0]}.csv")

df = pd.read_csv(filepath_or_buffer="data/Terminations of pregnancy.csv", index_col=0)
# plot_abortions(df)
