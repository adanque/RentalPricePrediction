"""
Author: Alan Danque
Date:   20210323
Purpose:Review Pluto Data for NYC
https://www1.nyc.gov/site/planning/data-maps/open-data/dwn-pluto-mappluto.page
"""
from pandasql import sqldf
import pandas as pd
import pygeohash
filepath = "C:/Alan/DSC680/Project1Data/pluto_21v1.csv"
testfile = "C:/Alan/DSC680/Project1Data/pluto_21v1_Top10.csv"
testfile2 = "C:/Alan/DSC680/Project1Data/pluto_21v1_Top10_new.csv"
pd.set_option('mode.chained_assignment', None)

def get_borough_name(val):
    if val['borough'] == "BX":
        return "Bronx"
    elif val['borough'] == "BK":
        return "Brooklyn"
    elif val['borough'] == "MN":
        return "Manhattan"
    elif val['borough'] == "QN":
        return "Queens"
    elif val['borough'] == "SI":
        return "Staten Island"
    else:
        return "None"

data = pd.read_csv(filepath)
print(type(data))
print(data.shape) # 49,352 obs and 15 vars
print(data.columns)
print(data.head(10))
print(data.head(10).to_csv(testfile))

columns = ['borough', 'schooldist',  'zipcode', 'firecomp', 'policeprct', 'healthcenterdistrict', 'healtharea', 'sanitboro', 'sanitdistrict', 'taxmap', 'latitude', 'longitude']
df = data[columns]

# Remove NaN rows / found after performing the distinct rows validation below.
df = df[df['latitude'].notna()]
df = df[df['borough'].notna()]
df = df[df['schooldist'].notna()]
df = df[df['zipcode'].notna()]
df = df[df['firecomp'].notna()]
df = df[df['policeprct'].notna()]

# Verify we have distinct rows
pysqldf = lambda t: sqldf(t, globals())
#t = "SELECT * from df where bathrooms < 3 and price < " + str(ulimit)+ ";"
query = "SELECT count(*) cnts, borough, schooldist,  zipcode, firecomp, policeprct, healthcenterdistrict, healtharea, sanitboro, sanitdistrict, taxmap, latitude, longitude from df group by borough, schooldist,  zipcode, firecomp, policeprct, healthcenterdistrict, healtharea, sanitboro, sanitdistrict, taxmap, latitude, longitude order by count(*) desc ;"
print(query)
df_results = pysqldf(query)
print(df_results)

df = df_results
# Add geohas and full borough name
df['geohash'] = df.apply(lambda x: pygeohash.encode(x.latitude, x.longitude), axis=1)
df['borough_name'] = df.apply(get_borough_name, axis=1)
df.drop('cnts', axis=1, inplace=True)

"""
# Get the closest next 
df['dist'] = df['coord'].apply(lambda x: min([geopy.distance.distance(x, y).km for y in libs['coord']]))
"""

print(type(df))
print(df.shape) # 49,352 obs and 15 vars
print(df.columns)
print(df.head(10))
#print(df.head(10).to_csv(testfile2))
df.to_csv(testfile2, index=False)


