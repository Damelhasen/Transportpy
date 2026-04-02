import urllib.request
import urllib.error
import requests
import os
import platform
import time

def clear_terminal():
    """Clears the terminal screen for Windows, macOS, and Linux."""
    try:
        os.system('cls' if platform.system() == "Windows" else 'clear')
    except Exception as e:
        print(f"Error clearing terminal: {e}")


def airport_info(station_icao):
    url = "https://aviationweather.gov/api/data/airport"
    params = {"ids": station_icao, "format": "json"}
    response = requests.get(url, params=params)
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
    mode = int(input("1. Raw METAR\n2. Decoded METAR\n3. Full Airport Information\nSelect option (1, 2 or 3): ").strip())
    return mode


def raw_metar(station_icao):
    url = f"https://tgftp.nws.noaa.gov/data/observations/metar/stations/{station_icao}.TXT"
    try:
        result = urllib.request.urlopen(url).read().decode('utf-8')
        print(result)
        print(url)
    except urllib.error.HTTPError:
        print("Error fetching data. Please check the ICAO code and try again.")


def decoded_metar(station_icao):
    url = f"https://tgftp.nws.noaa.gov/data/observations/metar/decoded/{station_icao}.TXT"
    try:
        result = urllib.request.urlopen(url).read().decode('utf-8')
        print(result)
    except urllib.error.HTTPError:
        print("Error fetching data. Please check the ICAO code and try again.")


def full_airport_info(station_icao):
    try:
        airport = airport_info(station_icao)
        print(f"Airport: {airport['name']}")
        print(f"ICAO: {airport['icaoId']}")
        print(f"Latitude: {airport['lat']}")
        print(f"Longitude: {airport['lon']}")
        print(f"Elevation: {airport['elev']}")
        print(f"Tower: {airport['tower']}")
        print(f"Frequencies: {airport['freqs']}")
        print()
        for runway in airport['runways']:
            print(f"  {runway['id']}  —  {runway['dimension']} ft  —  Surface: {runway['surface']}")
        print()
        decoded_metar(station_icao)
    except (IndexError, KeyError):
        print("Error fetching airport data. Please check the ICAO code and try again.")


def main():
    clear_terminal()
    mode = intro()

    handlers = {
        1: raw_metar,
        2: decoded_metar,
        3: full_airport_info,
    }

    handler = handlers.get(mode)
    if not handler:
        print("Invalid option selected.")
        return

    while True:
        
        station_icao = input("Enter the ICAO code of the station: ").strip().upper()
        handler(station_icao)
        input("\nPress Enter to look up another station...")
        time.sleep(5)
        clear_terminal()


if __name__ == "__main__":
    main()