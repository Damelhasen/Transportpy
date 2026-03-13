from time import time
import urllib.request
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



mode = int(input("1. Raw METAR\n2. Decoded METAR\nSelect option (1 or 2): ").strip())

clear_terminal()
while mode == 1 :
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

    
    