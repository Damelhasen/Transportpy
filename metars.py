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

# Example usage
print("This will be cleared in 2 seconds...")
import time
time.sleep(2)
clear_terminal()
print("Screen cleared!")
while True :
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

    print(result)
