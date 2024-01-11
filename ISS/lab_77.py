#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()
    
    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]
    epoch_time= resp["timestamp"]
    datetime_obj= datetime.datetime.fromtimestamp(epoch_time)
    results= rg.search((lat, lon))
    city= locator_resp[0]["name"]
    country= locator_resp[0]["cc"]

    print(f"CURRENT LOCATION OF THE ISS:\nTimestamp: {datetime_obj}\nLon: {lon}\nLat: {lat}\nCity/Country: {city}, {country}")

if __name__ == "__main__":
    main()

