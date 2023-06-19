import requests # This is the library that is used to get data from the API.
import json # This is the library that is used to convert the data from the API to a dictionary.
import os # This is the library that is used to get the current working directory.
import sys # This is the library that is used to get the current working directory.
import time # This is the library that is used to make the program wait.
import datetime # This is the library that is used to get the current time.
from logtail import LogtailHandler # This is the library that is used to log errors.
import logging # This is the library that is used to log errors.
from discord_webhook import DiscordWebhook # This is the library that is used to send messages to discord.
from dotenv import load_dotenv
import timezonecheck
import weatherapi
import weatherstate
import asyncio
from prometheus_client import start_http_server, Summary, Gauge
async def main():
    start_http_server(8000)

asyncio.run(main())
load_dotenv()
tempcgauge = Gauge('tempc', 'Temperature in celsius')
tempfgauge = Gauge('tempf', 'Temperature in fahrenheit')
feelslikecgauge = Gauge('feelslikec', 'Feels like temperature in celsius')
windms = Gauge('windms', 'Wind speed in m/s')
windmph = Gauge('windmph', 'Wind speed in mph')


def globalconnector():
    print ("globalconnector.py has been loaded.")
    time.sleep(1)
    timezone = timezonecheck.timezonecheck()
    print("Running the weather API check...")
    temp_c = weatherapi.tempc()
    temp_f = weatherapi.tempf()
    localtime = weatherapi.localtime()
    region = weatherapi.region()
    country = weatherapi.country()
    last_updated = weatherapi.lastupdated()
    condition = weatherapi.condition()
    feelslike_c = weatherapi.feelslikec()
    wind_mph = weatherapi.windmph()
    name = weatherapi.name()
    print("Weather API check done.")
    print("Rounding and converting the wind speed...")
    wind_m_s = weatherapi.windspeed(wind_mph)
    print("Wind speed rounded and converted.")
    print("Checking the weather state...")
    weather_state = weatherstate.weatherstate(condition)
    print("Running the discord webhook...")
    tempcgauge.set(temp_c)      # Increment by 1
    tempfgauge.set(temp_f)      # Increment by 1
    feelslikecgauge.set(feelslike_c)      # Increment by 1
    windms.set(wind_m_s)      # Increment by 1
    windmph.set(wind_mph)      # Increment by 1
    message = ("**Weather **" + weather_state +"\n" +"**State of the weather in "+ name +":** " +  condition + "\n" + "**Temperature:** " + str(temp_c) + "°C" + "\n" + "**Feels like:** " + str(feelslike_c) + "°C" + "\n" + "**Wind speed:** " + str(wind_m_s) + "m/s" + "\n"  + "**Region:** " + region + "\n" + "**Country:** " + country + "\n" + "**Last updated** ("+ timezone +")** :**_ "+ last_updated+  "_\n" + "**Local time** ("+ timezone +")** :**_ " + localtime + "_")
    webhook = DiscordWebhook(url=os.getenv("DISCORD_WEBHOOK_URL"), content=message)
    response = webhook.execute()

while True:
    globalconnector()
    time.sleep(60)
    

