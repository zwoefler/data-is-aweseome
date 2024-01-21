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


# Load API for geoocation
def data_cleanup_filtering():
    load_dotenv()
    api_key = os.getenv("OPENCAGE_API_KEY")
    geocoder = OpenCageGeocode(api_key)

    # 1. Read Excel
    excel_path = "data/Demos gegen Rechtsextremismus.xlsx"
    df = pd.read_excel(excel_path)

    # Make State row the header
    state_index = df[df.apply(lambda row: "State" in row.values, axis=1)].index[0]
    df.columns = df.iloc[state_index]
    df = df.drop(state_index)

    # 2. Get cities from Hessen
    dropped_nan_columns = df.dropna(axis=1, how="all")
    cleaned_df = dropped_nan_columns.dropna(axis=0, how="all")
    hessen_df = cleaned_df[cleaned_df["State"] == "Hessen"]

    hessen_df["Latitude"], hessen_df["Longitude"] = zip(
        *hessen_df["City"].apply(get_coordinates_for)
    )

    write_df_to_csv(hessen_df, "hessen_df.csv")


def create_hessen_map(df):
    hessen_map = folium.Map(location=[50.652778, 9.162778], zoom_start=8)
    # Add markers for each city
    for index, row in df.iterrows():
        folium.Marker(
            [row["Latitude"], row["Longitude"]],
            popup=f"{row['City']} - {row['Participants']} participants",
        ).add_to(hessen_map)

    return hessen_map


# 1. Read Dataframe
hessen_df = pd.read_csv("data/hessen_df.csv")
hessen_map = create_hessen_map(hessen_df)
hessen_map.save("hessen_protests_map.html")
