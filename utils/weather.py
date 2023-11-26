import os, sys
import requests
from bs4 import BeautifulSoup

base_url = "https://www.wunderground.com/history/monthly/us/me/portland/KPWM/date/"

for year in range(2014, 2023):
    for month in range(11, 13):
        # Format the month and year as 'yyyy-mm'
        formatted_date = f"{year}-{month:02d}"
        url = f"{base_url}{formatted_date}"

        # Make a request to the URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract temperature, precipitation, and wind information using BeautifulSoup
        # You'll need to inspect the HTML structure of the website to identify the relevant elements.
        # Use soup.select or soup.find to locate the elements and extract the data.
        # Update the following lines based on the HTML structure of the website.

        temperature = soup.find("span", class_="temperature-class").text
        precipitation = soup.find("span", class_="precipitation-class").text
        wind = soup.find("span", class_="wind-class").text

        # Print or store the extracted information as needed
        print(f"Date: {formatted_date}, Temperature: {temperature}, Precipitation: {precipitation}, Wind: {wind}")
