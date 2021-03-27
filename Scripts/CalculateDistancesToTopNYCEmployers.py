"""
Author: Alan Danque
Date:   20210323
Purpose:Creates map of the top employers

References:
https://moneyinc.com/the-20-biggest-employers-in-nyc/
https://fortune.com/best-workplaces-new-york/2020/search/

"""
import csv
import folium
import pandas as pd
import json
from folium import plugins
#import imgkit
import pygeohash

NYCEmployers = "C:/Alan/DSC680/Project1Data/NYCEmployers.csv"
RentHop = "C:/Alan/DSC680/Project1Data/renthopNYC.csv"
RentHop_OUT = "C:/Alan/DSC680/Project1Data/renthopNYC_OUT.csv"
Yelp = "C:/Alan/DSC680/Project1Data/yelp_business_data.csv"


# TOP EMPLOYERS
nycemployers_df = pd.read_csv(NYCEmployers,encoding='utf-8', names=["Rank","Name","Industry","HQ Location","Sites","Employees","World Wide Revenue","Latitude","Longitude"],sep=',',header=0,quoting=csv.QUOTE_ALL, engine='python')
nycemployers_df['geohash'] = nycemployers_df.apply(lambda x: pygeohash.encode(x.Latitude, x.Longitude), axis=1)

# RENTHOP
renthop_df = pd.read_csv(RentHop)
renthop_df['geohash'] = renthop_df.apply(lambda x: pygeohash.encode(x.latitude, x.longitude), axis=1)

for index, row in nycemployers_df.iterrows():
    fieldname = row['Name']+" Distance"
    emp_geohash = row['geohash']
    renthop_df[fieldname] = renthop_df.apply(lambda x: pygeohash.geohash_approximate_distance(x.geohash, emp_geohash) / 1000, axis=1)

    # distm_west = pygeohash.geohash_approximate_distance(srcgeoval, westval) / 1000

print(type(renthop_df))
print(renthop_df.shape) # 49,352 obs and 15 vars
print(renthop_df.columns)

renthop_df.to_csv(RentHop_OUT)
