import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from lxml import etree as et
import numpy as np
import requests
import pandas as pd
import os
from xml.etree import ElementTree

##use to conver FAA csv into just long, lat, and Iaco with dtype
def pd_convert():
    df = pd.read_csv(
        "db/all-airport-data.csv",
        dtype={"Icao Id": str, "ARP Latitude Sec": str, "ARP Longitude Sec": str},
    )
    df2 = df[["Icao Id", "ARP Latitude Sec", "ARP Longitude Sec"]].copy()
    df2.dropna()
    df2.to_csv("db/airport_data_long_lat")


# Known Drone Database
m300 = {
    "Name": "Matrice 300 RTK",
    "Operating Frequency": "2.4000-2.4835; 5.725-5.850GHz",
    "User Manual": "",
    "Weight": 13.9,  # lbs
    "Payload": 6,  # lbs
    "MTOW": 19.8,  # lbs
    "Max Wind Resistance": 23.3261,  # knots
    "Max Altitude": 5000,  # meters
    "Max Flight Time": 55,  # minutes
    "IP Rating": "IP45",
    "Min Operating Tempreture": -20,  # celsius
    "Max Operating Tempreture": 40,  # celsius
}

# Airports for the test. Eventually tie to GIS coordinates from User Map
def airport_selector():
    print("Nalaquq is fetching most recent airport data")
    db = "db"
    os.chdir(db)
    df = pd.read_csv(
        "airport_data_long_lat",
        dtype={"Icao Id": str, "ARP Latitude Sec": str, "ARP Longitude Sec": str},
    )
    x = input(
        "Please select where you would like to fly using a four digit Airport code: "
    )
    global station
    station = x.upper()
    print(f"The airport you have selected is: {station}.")
    return station


airport_selector()

# stream and download taf data from closest airport (bethel)
def taf():
    headers = requests.utils.default_headers()
    url = "https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=tafs&requestType=retrieve&format=xml&stationString=PABE&hoursBeforeNow=4"
    headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Xll; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
        }
    )
    page = requests.get(url, headers=headers)
    xml = page.content
    root = et.fromstring(xml)
    print(f"The airport you have selected is: {kwn}.")
    print("The following Tafs were generated in the last four hours:")
    for raw in root.iter("raw_text"):
        print(raw.text)


# Stream Metars Data as xml
def metar():
    global page
    global xml
    global root
    url = f"https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=Metars&requestType=retrieve&format=xml&stationString={station}&HoursBeforeNow=1"
    headers = requests.utils.default_headers()
    headers.update(
        {
            "User-Agent": "Mozilla/5.0 (Xll; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0"
        }
    )
    page = requests.get(url, headers=headers)
    # The weatherdata.gov server times out near the hour. The if statment resolves this
    xml = page.content
    root = et.fromstring(xml)
    error_check = root.find("num_results")
    print(error_check)


def raw_text():
    for raw in root.iter("raw_text"):
        return raw.text


def wind():
    for wind in root.iter("wind_speed_kt"):
        return float(wind.text)


def visibility():
    for x in root.iter("visibility_statute_mi"):
        return float(x.text)


def tempreture():
    for x in root.iter("temp_c"):
        return float(x.text)


def metar_decoded():
    global metar_list
    metar_list = (wind(), raw_text(), visibility())
    print(f"The metar information for this airport is: {raw_text()}")
    print(f"The current visibility is {visibility()} statute miles")
    print(f"Winds are steady at {wind()} knots")


def flight_checks():
    metar()
    metar_decoded()

    def wind_check():
        if m300["Max Wind Resistance"] >= wind():
            print(f"Checking Wind Conditions at {station}")
            print(f"Wind Check at {station} passed")
        else:
            print("Checking Wind Conditions")
            print(f"The winds at {station} are too strong")
            print("You should not fly")

    def temp_check():
        if m300["Min Operating Tempreture"] >= tempreture():
            print(f"Checking temp at {station}")
            print(f"It is too cold at {station}. Do not fly")
        elif m300["Max Operating Tempreture"] <= tempreture():
            print(f"Checking Temp at {station}")
            print(f"It is too hot at {station}. You should not fly.")

    wind_check()
    temp_check()


flight_checks()
