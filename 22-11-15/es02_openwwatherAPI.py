"""OpenweatherAPI"""
# per abilitare la virtual environment occorre digitare sul terminale "virtualenv venv" per creare 
# il virtual env, mentre per attivarlo occorre digitare "venv\Scripts\activate", usato per non 
# intaccare l'ambiente locale, NB occorre prima installarlo con pip

import json
import os
import requests
import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt

#import API key
open_weather_key = '786747fbd17266909639c55958338c21'
cities=['Montegranaro','Torino','Napoli','Venezia','Bologna','Milano']

#define base and query URL
url = "https://api.openweathermap.org/data/2.5/weather?"
query_url = f"{url}appid={open_weather_key}&q={cities[0]}&units=metric"
#aggiungo i dati relativi alla query di ricerca per la call API
# print(query_url)

#get response
response = requests.get(query_url).json() #chiedo il response della API in formato JSON
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

#set counts
number = 0
sets = 1

#loop through cities in list
for item in cities:
    try:
        query_url = f"{url}appid={open_weather_key}&q={item}&units=metric"   #try della chiamata
        response =requests.get(query_url).json()                #fetch del response
        number=+1                                        #iter count +1
        print(f"Processing record {number} of Sets {sets} | {item}") #print del 
        data["City"].append(response['name'])
        data["Cloudiness"].append(response['clouds']['all'])
        data["Country"].append(response['sys']['country'])
        data["Date"].append(response['dt'])
        data["Humidity"].append(response['main']['humidity'])
        data["Lat"].append(response['coord']['lat'])
        data["Long"].append(response['coord']['lon'])
        data["Max Temp"].append(response['main']['temp_max'])
        data["Wind Speed"].append(response['wind']['speed'])
    except:
        print("City not found; Skipping...")

#limit API requests in order to not exceed sub limit
time.sleep(5) #intervallo di 5 sec tra un push call and fetch info

print(data)
city_data_df=pd.DataFrame(data) #dataframe dalla libreria pandas aka tabella strutturata per convertire il nostro csv 

#plot max temp
max_temp = city_data_df["Max Temp"]
city = city_data_df["City"]

#set date
city_data_df['Date']=pd.to_datetime(city_data_df['Date'], unit='s')
date=city_data_df["Date"][0]

#create plot
plt.scatter(city,max_temp, s=40, c="slateblue", edgecolors="black", alpha=.75)
plt.title(f"City Latitude vs Temperature({date})")
plt.xlabel("Latitude")
plt.ylabel("Max Temp (F)")
plt.grid(b=None,which='major',axis='both')
plt.show()

#plot humidity
humidity=data['Humidity'] #basta richiamare la chiave humidity
city_data_df['Date']=pd.to_datetime(city_data_df['Date'], unit='s')
date=city_data_df['Date'][0]

#create plot
plt.scatter(city,humidity, s=40, c="slateblue", edgecolors="black", alpha=.75)
plt.title(f"City Latitude vs Humidity")
plt.xlabel("City")
plt.ylabel("Humidity %")
plt.grid(b=None,which='major',axis='both')
plt.show()

#plot forecast 5 days 3h della citta' di
data2 ={
    "temp":[],
    "date":[]
}

#define base and query url for forecast
url = "https://api.openweathermap.org/data/2.5/forecast?"
query_url=f"{url}appid={open_weather_key}&q={cities[0]}&units=metric"

response=requests.get(query_url).json()
for item in response["list"]:
    data2["date"].append(item['dt'])
    data2["temp"].append(item['main']['temp'])

#plot forecast
temp = data2['temp']
dt = pd.to_datetime(data2["date"], unit='s')
plt.scatter(dt, temp, s=40, c="slateblue", edgecolors="black", alpha=.75)
plt.title(f"Forecast city temperature {cities[0]}")
plt.xlabel("Date")
plt.ylabel("Temp (°C)")
plt.grid(b=None,which='major',axis='both')
plt.show()
