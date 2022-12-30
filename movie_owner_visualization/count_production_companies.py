import json
import pandas as pd
import os
import sys


def generateProductionMovieList(movie_list):
    production_movie_list = []

    for movie in movie_list:
        movie_object={
            "title": movie["title"],
            "production_companies": movie["production companies"]
        }
        production_movie_list.append(movie_object)

    return production_movie_list


def makeMovieDataFrame(companies_list):
    return pd.json_normalize(production_movie_list, 'production_companies', ['title'])


def searchForCompany(df, company):
    return df.loc[df["name"].str.contains(company)]


def countProductionCompanies(production_companies, df):
    """
    Counts the production companies specified in the production_companies list.
    The df is the movie dataframe containing a list of movies.

    The last value is the otal movie count.
    """
    production_dict = {
        "movie_count": df["title"].nunique()
    }
    for company in production_companies.keys():
        studio_dict = {
            "total": 0
        }
        studio_count = 0
        for studio in production_companies[company]:
            df_studio = searchForCompany(df, studio)
            count = len(df_studio)
            studio_dict[studio] = count
            studio_dict["total"] += count
        production_dict[company] = studio_dict

    return production_dict


def exportObjectToJSON(dict_object, file_name):
    with open(file_name + '.json', 'w') as f:
        json.dump(dict_object, f)


def importMovieJSON(json_file):
    with open(json_file, 'r') as f:
        array = json.load(f)
    return array



production_companies = {
    "disney": [
        "Disney",
        "Fox",
        "Lucasfilm"
    ],
    "sony": [
        "Sony",
        "Columbia",
    ],
    "comcast": [
        "DreamWorks",
        "Universal"
    ],
    "netflix": ["Netflix"],
    "amazon": ["Amazon", "Metro-Goldwyn-Mayer"],
    "warner": ["Warner", "HBO"],
    "youtube": ["YouTube"],
    "paramount": ["Paramount"],
}

json_file = sys.argv[1]
base_name = os.path.splitext(json_file)[0]

movie_list = importMovieJSON(json_file)
production_movie_list = generateProductionMovieList(movie_list)
movie_df = makeMovieDataFrame(production_movie_list)
count_dict = countProductionCompanies(production_companies, movie_df)
exportObjectToJSON(count_dict, "production_companies_count" + base_name)
