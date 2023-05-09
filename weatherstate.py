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

def weatherstate(weather_state):
    condition = weather_state
    if condition == "Sunny": # 0
        weather_state = ":sunny:" 
    elif condition == "Clear": # 0
        weather_state = ":crescent_moon:"
    elif condition == "Partly cloudy": # 1
        weather_state = ":partly_sunny:"
    elif condition == "Cloudly": # 2
        weather_state = ":white_sun_cloud:"
    elif condition == "Overcast": # 3
        weather_state = ":cloud:"
    elif condition == "Mist": # 4
        weather_state = ":fog:"
    elif condition == "Patchy rain nearby": # 5 
        weather_state = ":white_sun_rain_cloud:"
    elif condition == "Patchy snow nearby": # 6
        weather_state = ":cloud_snow:"
    elif condition == "Patchy sleet nearby": # 7
        weather_state = ":Weatherhailscattered:"
    elif condition == "Patchy freezing drizzle nearby": # 8
        weather_state = ":Patchy freezing drizzle nearby:"
    elif condition == "Thundery outbreaks nearby": # 9
        weather_state = ":cloud_lightning:"
    elif condition == "Blowing snow": # 10
        weather_state = ":cloud_snow:"
    elif condition == "Blizzard": # 11
        weather_state = ":cloud_snow:"
    elif condition == "Fog": # 12
        weather_state = ":fog:"
    elif condition == "Freezing fog": # 13
        weather_state = ":fog:"
    elif condition == "Patchy light drizzle": # 14
        weather_state = ":cloud_rain:"
    elif condition == "Light drizzle": # 15
        weather_state = ":cloud_rain:"
    elif condition == "Freezing drizzle": # 16
        weather_state = ":cloud_rain:"
    elif condition == "Heavy freezing drizzle": # 17
        weather_state = ":cloud_rain:"
    elif condition == "Patchy light rain": # 18
        weather_state = ":cloud_rain:"
    elif condition == "Light rain": # 19
        weather_state = ":cloud_rain:"
    elif condition == "Moderate rain at times": # 20
        weather_state = ":droplet:"
    elif condition == "Moderate rain": # 21
        weather_state = ":droplet:"
    elif condition == "Heavy rain at times": # 22
        weather_state = ":cloud_rain:"
    elif condition == "Heavy rain": # 23
        weather_state = ":cloud_rain:"
    elif condition == "Light freezing rain": # 24
        weather_state = ":cloud_rain:"
    elif condition == "Moderate or heavy freezing rain": # 25
        weather_state = ":cloud_rain:"
    elif condition == "Light sleet": # 26
        weather_state = ":sleeticon:"
    elif condition == "Moderate or heavy sleet": # 27
        weather_state = ":cloud_snow:"
    elif condition == "Patchy light snow": # 28
        weather_state = ":cloud_snow:"
    elif condition == "Light snow": # 29
        weather_state = ":cloud_snow:"
    elif condition == "Patchy moderate snow": # 30
        weather_state = ":cloud_snow:"
    elif condition == "Moderate snow": # 31
        weather_state = ":cloud_snow:"
    elif condition == "Patchy heavy snow": # 32
        weather_state = ":cloud_snow:"
    elif condition == "Heavy snow": # 33
        weather_state = ":cloud_snow:"
    elif condition == "Ice pellets": # 34
        weather_state = ":icepellets:"
    elif condition == "Light rain shower": # 35
        weather_state = ":sweat_drops:"
    elif condition == "Moderate or heavy rain shower": # 36
        weather_state = ":sweat_drops:"
    elif condition == "Torrential rain shower": # 37
        weather_state = ":sweat_drops:"
    elif condition == "Light sleet showers": # 38
        weather_state = ":sleeticon:"
    elif condition == "Moderate or heavy sleet showers": # 39
        weather_state = ":sleeticon:"
    elif condition == "Light snow showers": # 40
        weather_state = ":cloud_snow:"
    elif condition == "Moderate or heavy snow showers": # 41
        weather_state = ":cloud_snow:"
    elif condition == "Light showers of ice pellets": # 42
        weather_state = ":icepellets:"
    elif condition == "Moderate or heavy showers of ice pellets": # 43
        weather_state = ":icepellets:"
    elif condition == "Patchy light rain with thunder": # 44
        weather_state = ":thunder_cloud_rain:"
    elif condition == "Moderate or heavy rain with thunder": # 45
        weather_state = ":thunder_cloud_rain:"
    elif condition == "Patchy light snow with thunder": # 46
        weather_state = ":thunder_cloud_snow:"
    elif condition == "Moderate or heavy snow with thunder": # 47
        weather_state = ":thunder_cloud_snow:"
    else:
        weather_state = ":question:"
    return weather_state