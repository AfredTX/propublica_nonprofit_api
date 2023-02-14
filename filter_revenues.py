import os
import urllib.parse

import pandas as pd

import requests

df = pd.read_csv(fr'{os.getcwd()}\filtered_explorer.csv')

df = df[(df['city'] == "BALTIMORE") & (df['asset_amount'] <= 3000000)]

df['full_address'] = df["address"] + ", " + df["city"] + ", " + df["state"] + ' ' + df['zipcode']


df.to_csv(fr"C:\Users\fredr\PycharmProjects\propublica_nonprofit_api\final_data_set.csv")

lats = []
lons = []
for i in list(df['full_address']):
    try:
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(str({i})) + '?format=json'
        response = requests.get(url).json()
        print(response)
        print(response[0]["lat"])
        lats.append(response[0]["lat"])
        print(response[0]["lon"])
        lons.append(response[0]["lon"])
    except IndexError:
        lats.append('N/A')
        lons.append('N/A')
        continue
df['lat'] = lats
df['lon'] = lons

df.to_csv(fr"C:\Users\fredr\PycharmProjects\propublica_nonprofit_api\final_data_set.csv")