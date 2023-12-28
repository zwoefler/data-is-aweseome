import imdb
import pandas as pd
import json
import sys

ia = imdb.Cinemagoer()


export_name = sys.argv[1]
list_id = sys.argv[2]



imdb_movie_list = ia.get_movie_list(list_=list_id)

def destructureCompany(company):
    company_dict = {
        "companyID": company.companyID,
        "name": company["name"]
    }
    return company_dict


def destructurePerson(person):
    person_dict = {
        "personID": person.personID,
        "name": person["name"]
    }
    return person_dict


def exportObjectToJSON(object_to_export, json_file):
    with open(json_file + ".json", "w") as outfile:
        json.dump(object_to_export, outfile)


def flattenMovieDict(movie_dict):
    for key in movie_dict.keys():
        if isinstance(movie_dict[key], list):
            newValue = []
            for value in movie_dict[key]:
                if isinstance(value, imdb.Person.Person):
                    try:
                        newValue.append(destructurePerson(value))
                    except KeyError as e:
                        print("\n +++ ERROR Person +++")
                        print(e)
                        print("+++ +++ +++ +++")
                elif isinstance(value, imdb.Company.Company):
                    try:
                        newValue.append(destructureCompany(value))
                    except KeyError as e:
                        print("\n +++ ERROR Company +++")
                        print(e)
                        print("+++ +++ +++ +++")
                else: newValue.append(value)
            movie_dict[key] = newValue
    return movie_dict


movie_list = []
for movie in imdb_movie_list:
    print(movie["title"])
    currentMovie = ia.get_movie(movie.movieID)
    dict_movie = dict(currentMovie)
    ready_dict_movie = flattenMovieDict(dict_movie)
    movie_list.append(ready_dict_movie)

exportObjectToJSON(movie_list, export_name)
