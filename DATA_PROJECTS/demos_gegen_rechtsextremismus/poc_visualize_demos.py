import pandas as pd
import folium
import datetime


def get_marker_color(date):
    if pd.isna(date):
        return "red"

    today = datetime.datetime.today().date()
    event_date = datetime.datetime.strptime(date, "%d.%m.%y").date()

    if today > event_date:
        return "red"

    return "blue"


def create_hessen_map(df):
    hessen_map = folium.Map(location=[50.652778, 9.162778], zoom_start=8)
    # Add markers for each city
    for index, row in df.iterrows():
        color = get_marker_color(row["Date"])
        folium.Marker(
            [row["Latitude"], row["Longitude"]],
            popup=f"{row['City']}\n{row['Participants']}\n{row['Date']}",
            icon=folium.Icon(color=color),
        ).add_to(hessen_map)

    return hessen_map


# If date is nan --> steht noch aus
# If participants is nan --> -

df = pd.read_csv("data/demos.csv")
hessen_df = df[df["State"] == "Hessen"]
hessen_map = create_hessen_map(hessen_df)
hessen_map.save("hessen_protests_map.html")
