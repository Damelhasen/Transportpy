import requests
station_icao = input("Enter the ICAO code of the station: ").strip().upper() 
url = "https://aviationweather.gov/api/data/airport"
params = {"ids": "station_icao", "format": "json"}
params["ids"] = station_icao 
response = requests.get(url, params=params)
data = response.json()
print(data)