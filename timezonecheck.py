import requests # This is the library that is used to get data from the API.
import json # This is the library that is used to convert the data from the API to a dictionary.
import os # This is the library that is used to get the current working directory.
import sys # This is the library that is used to get the current working directory.
import time # This is the library that is used to make the program wait.
import datetime # This is the library that is used to get the current time.
from dotenv import load_dotenv
load_dotenv()
def timezonecheck():
    print ("timezonecheck.py has been loaded.")
    time.sleep(0.5)
    print("Checking the timezone...")
    response1 = requests.get("http://worldtimeapi.org/api/timezone/Europe/Helsinki") # This is the API request.
    response1_simple = json.loads(response1.text) # This converts the data from the API to a dictionary.
    utc_offset = response1_simple["utc_offset"]
    global utc_offset_global_timezone_finland
    utc_offset_global_timezone_finland = utc_offset
    print ("The timezone is " + utc_offset_global_timezone_finland + ".")
    return utc_offset_global_timezone_finland

