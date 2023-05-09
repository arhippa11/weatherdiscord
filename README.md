# weatherdiscord
Remember to add a weather api key (weatherapi.com)
Run globalconnector.py for the start script.
To change the town change the line 19 in weatherapi.py:
  response1 = requests.get("http://api.weatherapi.com/v1/current.json?key=" + weatherapikey + "&q=Your town&aqi=yes", headers=headers)

To change the timezone change the line 13 in timezonecheck.py
  response1 = requests.get("http://worldtimeapi.org/api/timezone/YourCountryInEurope/HelsinkiFormat") # This is the API request.
