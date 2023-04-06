################## working with API ###############
import requests
import json


# welcome message
print("""welcome to my weather app
Enter your city, town name to get weather info""")


# API parsing
url = "https://weatherapi-com.p.rapidapi.com/current.json"


# location info 
location = input("Location(city name, village name): ")
querystring = {"q": location}


# providing it my API password (key)
headers = {
    "X-RapidAPI-Key": "c6465ddbafmshca2403892bb3b5cp1ec56cjsn8b25c1cc4cfc",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

try:
	# response from the API
	response = requests.request("GET", url, headers=headers, params=querystring)

	data = json.loads(response.text)

	# Extracting data from Dataframe
	location = data['location']
	current = data['current']


	# printing final weather on screen
	print(f"\n\nLocation: {location['name']}, {location['region']}, {location['country']}")
	print(f"Current time: {location['localtime']}")
	print(f"Temperature: {current['temp_c']}°C ({current['temp_f']}°F)")
	print(f"Condition: {current['condition']['text']}")
	print(f"Humidity: {current['humidity']}%")
	print(f"Wind: {current['wind_kph']} km/h ({current['wind_dir']})")
except KeyError as e:
	print("""\ncheck your location spelling and if its correct. Sorry, weather available for your place""")