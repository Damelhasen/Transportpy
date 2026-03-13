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
    data = response.json()
    print(data)

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
    mode = int(input("1. Raw METAR\n2. Decoded METAR\nSelect option (1 or 2): ").strip())



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
    url = "https://aviationweather.gov/api/data/airport"
    params = {"ids": "station_icao", "format": "json"}
    params["ids"] = station_icao 
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
    try:
        clear_terminal()
        result = urllib.request.urlopen(url).read().decode('utf-8')
        print(result)
    except urllib.error.HTTPError:
        clear_terminal()
        print("Error fetching data. Please check the ICAO code and try again.")
        result = None