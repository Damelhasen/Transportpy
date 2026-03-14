from time import time
import urllib.request
import requests
import json
import os
import platform

def clear_terminal():
    """
    Clears the terminal screen for Windows, macOS, and Linux.
    """
    try:
        current_os = platform.system()
        
        if current_os == "Windows":
            os.system('cls') 
        else:
            os.system('clear')  
    except Exception as e:
        print(f"Error clearing terminal: {e}")

def airport_info(station_icao):
    url = "https://aviationweather.gov/api/data/airport"
    params = {"ids": station_icao, "format": "json"}
    response = requests.get(url, params=params)
    global data
    data = response.json()
    return data[0]
    

def intro():
    print(r"""
      __|__
      \___/
       | |
       | |
      _|_|_
        /|\
       */ | \*
       / -+- \
   ---o--(_)--o---
      /  0 " 0  \
     */     |     \*
     /      |      \
    */       |       \*""")

    print("Welcome To Johan's NavBuddy")
    global mode
    mode = int(input("1. Raw METAR\n2. Decoded METAR\n3.Full Airport Information\nSelect option (1,2 or 3): ").strip())



clear_terminal
intro()
while mode == 1 :
    clear_terminal()
    station_icao = input("Enter the ICAO code of the station: ").strip().upper() 
    url = f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{station_icao}.TXT"
      
    try:
        clear_terminal()
        result = urllib.request.urlopen(url).read().decode('utf-8')
        print(result)
    except urllib.error.HTTPError:
        clear_terminal()
        print("Error fetching data. Please check the ICAO code and try again.")
        result = None

    
    print(url)

while mode == 2 :
    station_icao = input("Enter the ICAO code of the station: ").strip().upper() 
    url = f"https://tgftp.nws.noaa.gov/data/observations/metar/decoded/{station_icao}.TXT"
      
    try:
        clear_terminal()
        result = urllib.request.urlopen(url).read().decode('utf-8')
        print(result)
    except urllib.error.HTTPError:
        clear_terminal()
        print("Error fetching data. Please check the ICAO code and try again.")
        result = None

    
while mode == 3 :
    station_icao = input("Enter the ICAO code of the station: ").strip().upper() 
    airport = airport_info(station_icao)
    elevation = airport["elev"]
    name      = airport["name"]
    icao      = airport["icaoId"]
    lat       = airport["lat"]
    lon       = airport["lon"]
    tower     = airport["tower"]
    freqs     = airport["freqs"]
    
    try:
        clear_terminal()
        print(f"Airport: {name}")
        print(f"ICAO: {icao}")
        print(f"Latitude: {lat}")
        print(f"Longitude: {lon}")
        print(f"Elevation: {elevation}")
        print(f"Tower: {tower}")
        print(f"Frequencies: {freqs}")
        print()
        for runway in airport['runways']:
            print(f"  {runway['id']}  —  {runway['dimension']} ft  —  Surface: {runway['surface']}")
        print()
        print()
        result = urllib.request.urlopen(f"https://tgftp.nws.noaa.gov/data/observations/metar/decoded/{station_icao}.TXT").read().decode('utf-8')
        print(result)
    except urllib.error.HTTPError:
        
        print("Error fetching data. Please check the ICAO code and try again.")
        result = None
    