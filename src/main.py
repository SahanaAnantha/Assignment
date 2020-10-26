import json
import os
import requests
from datetime import datetime
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd
from src.models import TheatreMovies, TvMovies


# Function to insert theatre data into DB
def insert_theatre_data(data):
    theatre_movies = []
    # create new Session and commit to database
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    try:
        for i, result in enumerate(data):
            row = dict()
            flag = true
            row['id'] = i + 1
            row['title'] = result['title']
            if 'releaseYear' in result:
                row['releaseYear'] = str(result['releaseYear'])
            else:
                flag = false
            if 'genres' in result:
                s = result['genres']
                list_str = ','.join([str(elem) for elem in s])
                row['genres'] = list_str
            else:
                flag = false
            if 'shortDescription' in result:
                row['description'] = result['shortDescription']
            else:
                flag = false
            theatres_info = result['showtimes']
            theatres_names = set()
            for res in theatres_info:
                theatres_names.add(res['theatre']['name'])
            row['theatre'] = theatres_names
            if flag == true:
                theatre_movies.append(row)

        for movies in theatre_movies:
            row = TheatreMovies(**movies)
            session.add(row)

        session.commit()
        print('Theatre data inserted successfully')
    except Exception as e:
        print('Error Loaded Theatre Data into DB : ' + e)
    finally:
        session.close()


# Function to insert TV data into DB
def insert_tv_data(data):
    tv_movies = []
    # create new Session and commit to database
    session_maker = sessionmaker(bind=engine)
    session = session_maker()
    try:
        for i, result in enumerate(data):
            row = dict()
            flag = true
            row['id'] = i + 1
            row['title'] = result['program']['title']
            if 'releaseYear' in result['program']:
                row['releaseYear'] = str(result['program']['releaseYear'])
            else:
                flag = false
            if 'genres' in result['program']:
                s = result['program']['genres']
                list_str = ','.join([str(elem) for elem in s])
                row['genres'] = list_str
            else:
                flag = false
            if 'shortDescription' in result['program']:
                row['description'] = result['program']['shortDescription']
            else:
                flag = false
            tv_info = result['channels']
            info_str = ','.join([str(elem) for elem in tv_info])
            row['channel_no'] = info_str

            if flag == true:
                tv_movies.append(row)

        for movies in tv_movies:
            row = TvMovies(**movies)
            session.add(row)

        session.commit()
        print('TV data inserted successfully')
    except Exception as e:
        print('Error Loading TV Data into DB : ' + e)
    finally:
        session.close()


# Function to retrieve data from DB and perform groupby operation
def top5_genres_details():
    conn = engine.connect()
    data_theatre = conn.execute("select * from theatre_movies")
    theatre_df = pd.DataFrame(data_theatre)
    # theatre_by_genres = pd.DataFrame(columns=['id', 'title', 'releaseYear', 'genres', 'description', 'theatre'])
    theatre_list = list()
    for index, x in theatre_df.iterrows():
        genres_types = x[3].split(',')
        for i in genres_types:
            new_row = {'id': x[0], 'title': x[1], 'releaseYear': x[2], 'genres': i, 'description': x[4],
                       'theatre': x[5]}
            theatre_list.append(new_row)

    theatre_by_genres = pd.DataFrame(theatre_list)
    # theatre_group = theatre_by_genres.groupby('genres').count()

    data_tv = conn.execute("select * from tv_movies")
    tv_df = pd.DataFrame(data_tv)
    tv_list = list()
    for index, x in tv_df.iterrows():
        genres_types = x[3].split(',')
        for i in genres_types:
            new_row = {'id': x[0], 'title': x[1], 'releaseYear': x[2], 'genres': i, 'description': x[4],
                       'channel_no': x[5]}
            tv_list.append(new_row)

    tv_by_genres = pd.DataFrame(tv_list)
    # tv_group = tv_by_genres.groupby('genres').count()

    combine = [theatre_by_genres, tv_by_genres]
    combine_df = pd.concat(combine)
    genres_top = combine_df.groupby('genres', sort=False)['id'].count()
    genres_top = genres_top.sort_values(ascending=False).head(5)

    output = list()
    for i, v in genres_top.items():
        movie_details = combine_df.loc[combine_df['genres'] == i].to_json(orient="records")
        new_record = {'Genres': i, 'MovieCount': v, 'Movie_Details': movie_details}
        output.append(new_record)

    print('\nFunction 2: ')
    print('Top 5 Genres with highest movie count along with movie details: ')
    for row in output:
        print(row)


if __name__ == '__main__':
    try:
        now = datetime.now()
        secret_key = os.environ.get('ASSIGNMENT_KEY')

        # connect to sqlite database
        engine = create_engine('mysql://root:@localhost/assignment')

        # define schema
        Base = declarative_base()

        theatre_URL = 'http://data.tmsapi.com/v1.1/movies/showings'
        tvURL = 'http://data.tmsapi.com/v1.1/movies/airings'

        theatre_params = {'startDate': now.strftime("%Y-%m-%d"), 'zip': '78701', 'api_key': secret_key}
        tv_params = {'lineupId': 'USA-TX42500-X', 'startDateTime': now.strftime("%Y-%m-%dT%H:%MZ"),
                     'api_key': secret_key}

        resp_theatre = requests.get(theatre_URL, params=theatre_params).json()
        resp_tv = requests.get(tvURL, params=tv_params).json()

        # drop tables if present
        TvMovies.__table__.drop(bind=engine, checkfirst=True)
        TheatreMovies.__table__.drop(bind=engine, checkfirst=True)

        # create tables
        TvMovies.__table__.create(bind=engine, checkfirst=True)
        TheatreMovies.__table__.create(bind=engine, checkfirst=True)

        # function 1 - to load data into DB
        print('Function 1: ')
        insert_theatre_data(resp_theatre)
        insert_tv_data(resp_tv)

        # function 2 - top 5 genres with highest movie count
        top5_genres_details()
    except Exception as e:
        print('Error Accessing : ' + e)


