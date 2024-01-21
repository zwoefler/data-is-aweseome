import pandas as pd
import folium
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import os


#########################
# DATA CLEANUP / FILTERING
##########################
def write_df_to_csv(dataframe, file_name):
    data_dir = "data"
    file_path = os.path.join(data_dir, file_name)

    dataframe.to_csv(file_path, index=False)


def get_coordinates_for(city):
    try:
        result = geocoder.geocode(
            city + ", Germany", countrycode="DE", no_annotations=1
        )
        if (
            result
            and "geometry" in result[0]
            and "lat" in result[0]["geometry"]
            and "lng" in result[0]["geometry"]
        ):
            return result[0]["geometry"]["lat"], result[0]["geometry"]["lng"]
        else:
            return None, None
    except Exception as e:
        print(f"Error for city {city}: {e}")
        return None, None


load_dotenv()
api_key = os.getenv("OPENCAGE_API_KEY")
geocoder = OpenCageGeocode(api_key)


def read_excel_file_as_df():
    # 1. Read Excel
    excel_path = "data/Demos gegen Rechtsextremismus.xlsx"
    return pd.read_excel(excel_path)


def read_csv():
    csv_path = "data/demos.csv"
    return pd.read_csv(csv_path)


# Make State row the header
def clean_df(df):
    state_index = df[df.apply(lambda row: "State" in row.values, axis=1)].index[0]
    df.columns = df.iloc[state_index]
    df = df.drop(state_index)
    dropped_nan_columns = df.dropna(axis=1, how="all")
    cleaned_df = dropped_nan_columns.dropna(axis=0, how="all")

    return cleaned_df


def convert_dates(date_str):
    if pd.notna(date_str):
        # Convert "mm-dd-yy" to "dd.mm.yy"
        try:
            date_object = pd.to_datetime(date_str, format="%m-%d-%y")
            return date_object.strftime("%d.%m.%y")
        except ValueError:
            # Handle invalid date formats gracefully
            return date_str
    else:
        return date_str


def add_lat_long_to_dataframe(df):
    df["Latitude"], df["Longitude"] = zip(*df["City"].apply(get_coordinates_for))
    return df


df = read_csv()
# cleaned_df = clean_df(df)
df["Date"] = df["Date"].apply(convert_dates)
dataframe = add_lat_long_to_dataframe(df)
write_df_to_csv(dataframe, "demos.csv")
