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
load_dotenv()

weatherapikey = os.getenv("WEATHER_API_KEY")

headers = {
    'Accept': 'application/json', # This is the format of the data we want to get from the API.
}
def weatherapi():
    response1 = requests.get("http://api.weatherapi.com/v1/current.json?key=" + weatherapikey + "&q=Tampere&aqi=yes", headers=headers) # This is the API request.
    response1_simple = json.loads(response1.text) # This converts the data from the API to a dictionary.
    temp_c = response1_simple['current']["temp_c"] # This gets the data we want from the dictionary. (Temperature in celsius)
    temp_f = response1_simple['current']["temp_f"] # This gets the data we want from the dictionary. (Temperature in fahrenheit)
    localtime = response1_simple['location']["localtime"] # This gets the data we want from the dictionary. (Local time)
    region = response1_simple['location']["region"] # This gets the data we want from the dictionary. (Region)
    country = response1_simple['location']["country"] # This gets the data we want from the dictionary. (Country)
    last_updated = response1_simple['current']["last_updated"] # This gets the data we want from the dictionary. (Last updated)
    condition = response1_simple['current']["condition"]["text"] # This gets the data we want from the dictionary. (Condition)
    feelslike_c = response1_simple['current']["feelslike_c"] # This gets the data we want from the dictionary. (Feelslike in celsius)
    wind_mph = response1_simple['current']["wind_mph"] # This gets the data we want from the dictionary. (Wind speed in mph)
    wind_m_s_noround = (wind_mph * 1000)/3600
    name = response1_simple['location']["name"] # This gets the data we want from the dictionary. (Name of the location)
    return response1_simple
def tempc():
    response1_simple = weatherapi()
    temp_c = response1_simple['current']["temp_c"] # This gets the data we want from the dictionary. (Temperature in celsius)
    return temp_c
def tempf():
    response1_simple = weatherapi()
    temp_f = response1_simple['current']["temp_f"] # This gets the data we want from the dictionary. (Temperature in fahrenheit)
    return temp_f
def localtime():
    response1_simple = weatherapi()
    localtime = response1_simple['location']["localtime"] # This gets the data we want from the dictionary. (Local time)
    return localtime
def region():
    response1_simple = weatherapi()
    region = response1_simple['location']["region"] # This gets the data we want from the dictionary. (Region)
    return region
def country(): 
    response1_simple = weatherapi()
    country = response1_simple['location']["country"] # This gets the data we want from the dictionary. (Country)
    return country
def lastupdated():
    response1_simple = weatherapi()
    last_updated = response1_simple['current']["last_updated"] # This gets the data we want from the dictionary. (Last updated)
    return last_updated
def condition():
    response1_simple = weatherapi()
    condition = response1_simple['current']["condition"]["text"] # This gets the data we want from the dictionary. (Condition)
    return condition
def feelslikec():
    response1_simple = weatherapi()
    feelslike_c = response1_simple['current']["feelslike_c"] # This gets the data we want from the dictionary. (Feelslike in celsius)
    return feelslike_c
def windmph():
    response1_simple = weatherapi()
    wind_mph = response1_simple['current']["wind_mph"] # This gets the data we want from the dictionary. (Wind speed in mph)
    return wind_mph
def name():
    response1_simple = weatherapi()
    name = response1_simple['location']["name"] # This gets the data we want from the dictionary. (Name of the location)
    return name

def windspeed(wind_mph):
    wind_m_s_noround = (wind_mph * 1000)/3600
    wind_m_s = round(wind_m_s_noround, 2)
    return wind_m_s