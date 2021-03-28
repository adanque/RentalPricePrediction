"""
Author: Alan Danque
Date:   20210323
Purpose:Generates the geohash for each attraction and calculates the distances to attraction from each apartment
"""
import pandas as pd
import pygeohash
import csv
NYCAttractions = "C:/Alan/DSC680/Project1Data/NYCAttractions.csv"
NYCAttractions_Geohashed = "C:/Alan/DSC680/Project1Data/NYCAttractions_GeoHashed.csv"

RentHop = "C:/Alan/DSC680/Project1Data/MasterFinalAnalyticsDataSet.csv"
RentHop_OUT = "C:/Alan/DSC680/Project1Data/MasterFinalAnalyticsDataSet_OUT.csv"

# TOP EMPLOYERS
NYCAttractions_df = pd.read_csv(NYCAttractions,encoding='utf-8', names=["name","latitude","longitude","tourism"],sep=',',header=0,quoting=csv.QUOTE_ALL, engine='python')
NYCAttractions_df['geohash'] = NYCAttractions_df.apply(lambda x: pygeohash.encode(x.latitude, x.longitude), axis=1)
NYCAttractions_df.to_csv(NYCAttractions_Geohashed)

# RENTHOP
renthop_df = pd.read_csv(RentHop)

# Loop through NYC Attractions to create the distances between attraction to each apartment
for index, row in NYCAttractions_df.iterrows():
    fieldname = row['name']+" Distance"
    attr_geohash = row['geohash']
    renthop_df[fieldname] = renthop_df.apply(lambda x: pygeohash.geohash_approximate_distance(x.geohash, attr_geohash) / 1000, axis=1)

print(type(renthop_df))
print(renthop_df.shape) # 49,352 obs and 15 vars
print(renthop_df.columns)

renthop_df.to_csv(RentHop_OUT)
