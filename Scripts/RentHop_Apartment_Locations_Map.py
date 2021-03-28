"""
Author: Alan Danque
Date:   20210323
Purpose:Creates map of the locations of the apartments

References:
https://moneyinc.com/the-20-biggest-employers-in-nyc/
https://fortune.com/best-workplaces-new-york/2020/search/

"""

import folium
import pandas as pd
import json
from folium import plugins

df = pd.read_csv("C:/Alan/DSC680/Project1Data/renthopNYC_Final_OUT.csv")

with open('boroughs.geojson') as f:
    laArea = json.load(f)

#initialize the map around NYC County
laMap = folium.Map(location=[40.7078,-74.0337], zoom_start=12)

#add the shape of NYC County to the map
folium.GeoJson(laArea).add_to(laMap)

#for each row in the dataset, plot the corresponding latitude and longitude on the map
for i,row in df.iterrows():
    folium.CircleMarker((row.latitude,row.longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(laMap)

#save the map as an html
laMap.save('NYC_RentHop_ApartmentLocations_Map.html')

#initialize the LA County map
#laMap = folium.Map(location=[34.0522,-118.2437], tiles='Stamen Toner', zoom_start=9)
laMap = folium.Map(location=[40.7078,-74.0337], zoom_start=12)

#add the shape of LA County to the map
folium.GeoJson(laArea).add_to(laMap)

#for each row in the Starbucks dataset, plot the corresponding latitude and longitude on the map
for i,row in df.iterrows():
    folium.CircleMarker((row.latitude,row.longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(laMap)

#add the heatmap. The core parameters are:
#--data: a list of points of the form (latitude, longitude) indicating locations of Starbucks stores

#--radius: how big each circle will be around each Starbucks store

#--blur: the degree to which the circles blend together in the heatmap

laMap.add_child(plugins.HeatMap(data=df[['latitude', 'longitude']].to_numpy(), radius=25, blur=10))

#save the map as an html
laMap.save('NYC_RentHop_ApartmentLocations_Heatmap.html')
