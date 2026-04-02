
# NAVBUDDY

NAVBUDDY is a simple nvigation tool that helps pilots quickly look up METARs and full
Airport info (Currently only works in the U.S and Canada)

## Demo

```      __|__
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
    */       |       \*
Welcome To Johan's NavBuddy
1. Raw METAR
2. Decoded METAR
3. Full Airport Information
Select option (1, 2 or 3): 3
Enter the ICAO code of the station: KJFK 
Airport: NEW YORK/JOHN F KENNEDY INTL 
ICAO: KJFK
Latitude: 40.6399
Longitude: -73.7787
Elevation: 4
Tower: T
Frequencies: D-ATIS,115.4;D-ATIS,117.7;LCL/P,119.1;LCL/P,123.9;D-ATIS,128.725

  04L/22R  —  12079x200 ft  —  Surface: C
  04R/22L  —  8400x200 ft  —  Surface: A
  13L/31R  —  10000x200 ft  —  Surface: C
  13R/31L  —  14511x200 ft  —  Surface: C

KENNEDY INTERNATIONAL AIRPORT , NY, United States (KJFK) 40-38N 073-46W 9M
Apr 01, 2026 - 11:51 PM EDT / 2026.04.02 0351 UTC
Wind: from the E (100 degrees) at 9 MPH (8 KT):0
Visibility: 10 mile(s):0
Sky conditions: overcast
Weather: light rain
Precipitation last hour: A trace
Temperature: 55.9 F (13.3 C)
Dew Point: 48.9 F (9.4 C)
Relative Humidity: 77%
Pressure (altimeter): 30.25 in. Hg (1024 hPa)
ob: KJFK 020351Z 10008KT 10SM -RA OVC020 13/09 A3025 RMK AO2 RAB04 SLP242 P0000 T01330094
cycle: 4 
```

## Documentation

``` #to install run
pip install navbuddyinfo==0.1.5
navbuddyinfo
```
more info at 
https://pypi.org/project/navbuddyinfo/0.1.5/
**NOTE PLEASE USE FULL ICAO CODE EX.(KJFK NOT JFK)
## Acknowledgements

AI used for folder organization , .toml and minor debugging