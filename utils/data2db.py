"""
Python script that takes an excel file or a city name as input and writes the data to a database.
If the input is an excel file, the script will write the data in the excel to a database.
If the input is a city name, the script will pull the weather data from the internet and write it to a database.
"""

import sqlite3
import pandas as pd
import requests
import argparse

def xls_to_sqlite(xls_name, db_name):
  conn = sqlite3.connect(db_name)
  cur = conn.cursor()
  df = pd.read_excel(xls_name)
  df.to_sql("dummy", conn, if_exists="replace")
  conn.close()

# import climate data from internet for portland, maine
def weather_to_sqlite(api_key, city_name, db_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
    }

    weather = ""
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            # Print or process the weather data here
            print("Weather in {}: {}".format(city_name, data['weather'][0]['description']))
            date = data['dt']
            weather = data['main']['temp']

            # create the database if doesn't exist with date and weather columns and db_name as name
            conn = sqlite3.connect(db_name)
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS weather (date, weather)")

            # add weather and date to table
            cur.execute("INSERT INTO weather (date, weather) VALUES (?, ?)", (date, weather))

        else:
            print("Error {}: {}".format(data['cod'], data['message']))

    except Exception as e:
        print("An error occurred:", e)

parser = argparse.ArgumentParser("Writes excel data or a city's weather info pulled from internet to a database")
parser.add_argument("--path", type=str, help="path to excel file or city name")
parser.add_argument("--db_name", type=str, help="name of database")
args = parser.parse_args()

if args.path.endswith(".xls") or args.path.endswith(".xlsx") or args.path.endswith(".csv") or args.path.endswith(".txt"):
    xls_to_sqlite(args.path, args.db_name)
    print("Excel file successfully written to database")
else:
    weather_to_sqlite("43e68679727ed6f586bbc8d96e79b92b", args.path, args.db_name )