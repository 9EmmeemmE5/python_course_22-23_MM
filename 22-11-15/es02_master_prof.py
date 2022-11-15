#setup
import json
import os
import requests
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

#import API key
open_weather_key = '02858051ffc502f32c0e4788c6bfff15'

cities = ['Roma','Torino','Napoli','Venezia','Bologna','Milano']

#define base and query URL
url = "http://api.openweathermap.org/data/2.5/weather?"
query_url =f"{url}appid={open_weather_key}&q={cities[0]}"
#print(query_url)

#get response
response = requests.get(query_url).json()
print(response)

#crate summary dict
data = { 
    "City": [],
    "Cloudiness": [],
    "Country": [],
    "Date": [],
    "Humidity": [],
    "Lat": [],
    "Long": [],
    "Max Temp": [],
    "Wind Speed": []
}

#set counts for print statement in loop
number = 0
sets = 1

#loop through cities in list
for item in cities:
    try:
        #redefine query_url and response for each city in the loop
        query_url = f"{url}appid={open_weather_key}&q={item}"
        response = requests.get(query_url).json()
        #update print statement count and print
        number = number + 1
        print(f"Processing Record {number} of Set {sets} | {item}")
        #append summary dict with appropriate data
        data["City"].append(response['name'])
        data["Cloudiness"].append(response['clouds']['all'])
        data["Country"].append(response['sys']['country'])
        data["Date"].append(response['dt'])
        data["Humidity"].append(response['main']['humidity'])
        data["Lat"].append(response['coord']['lat'])
        data["Long"].append(response['coord']['lon'])
        data["Max Temp"].append(response['main']['temp_max'])
        data["Wind Speed"].append(response['wind']['speed'])
    #create exception
    except:
        print("City not found. Skipping ...")

    #limit API requests
    time.sleep(1)

print(data)

city_data_df = pd.DataFrame(data)
print(data)

city_data_df = pd.DataFrame(data)
print(data)


max_temp = city_data_df["Max Temp"]
city = city_data_df["City"]
#set date
city_data_df['Date'] = pd.to_datetime(city_data_df['Date'], unit='s')
date=city_data_df["Date"][0]

#create plot
plt.scatter(city,max_temp, s=40, c="slateblue", edgecolors="black", alpha=.75)
plt.title(f"City Latitude vs Temperature({date}")
plt.xlabel("Latitude")
plt.ylabel("Max Temp (F)")
plt.grid(b=None,which='major',axis='both')
plt.show()