"""
Author: Alan Danque
Date:   20210323
Purpose:Gets zip codes using the latitude and longitude. Then removes those rows that are not in NYC.
Complete: --- 6.707104444503784 seconds has passed ---
"""
import geopy
import pandas as pd
import yaml
import os
import re
from pathlib import Path
import time
from pandasql import sqldf
start_time = time.time()

def borough_id(val):
    if val['borough_area_name'] == "Bronx - Central Bronx":
        return 0
    elif val['borough_area_name'] == "Bronx - Bronx Park and Fordham":
        return 1
    elif val['borough_area_name'] == "Bronx - High Bridge and Morrisania":
        return 2
    elif val['borough_area_name'] == "Bronx - Hunts Point and Mott Haven":
        return 3
    elif val['borough_area_name'] == "Bronx - Kingsbridge and Riverdale":
        return 4
    elif val['borough_area_name'] == "Bronx - Northeast Bronx ":
        return 5
    elif val['borough_area_name'] == "Bronx - Southeast Bronx":
        return 6
    elif val['borough_area_name'] == "Brooklyn - Central Brooklyn":
        return 7
    elif val['borough_area_name'] == "Brooklyn - Southwest Brooklyn":
        return 8
    elif val['borough_area_name'] == "Brooklyn - Borough Park":
        return 9
    elif val['borough_area_name'] == "Brooklyn - Canarsie and Flatlands":
        return 10
    elif val['borough_area_name'] == "Brooklyn - Southern Brooklyn":
        return 11
    elif val['borough_area_name'] == "Brooklyn - Northwest Brooklyn":
        return 12
    elif val['borough_area_name'] == "Brooklyn - Flatbush":
        return 13
    elif val['borough_area_name'] == "Brooklyn - East New York and New Lots":
        return 14
    elif val['borough_area_name'] == "Brooklyn - Greenpoint":
        return 15
    elif val['borough_area_name'] == "Brooklyn - Sunset Park":
        return 16
    elif val['borough_area_name'] == "Brooklyn - Bushwick and Williamsburg":
        return 17
    elif val['borough_area_name'] == "Manhattan - Central Harlem":
        return 18
    elif val['borough_area_name'] == "Manhattan - Chelsea and Clinton":
        return 19
    elif val['borough_area_name'] == "Manhattan - East Harlem":
        return 20
    elif val['borough_area_name'] == "Manhattan - Gramercy Park and Murray Hill":
        return 21
    elif val['borough_area_name'] == "Manhattan - Greenwich Village and Soho":
        return 22
    elif val['borough_area_name'] == "Manhattan - Lower Manhattan":
        return 23
    elif val['borough_area_name'] == "Manhattan - Lower East Side":
        return 24
    elif val['borough_area_name'] == "Manhattan - Upper East Side":
        return 25
    elif val['borough_area_name'] == "Manhattan - Upper West Side":
        return 26
    elif val['borough_area_name'] == "Manhattan - Inwood and Washington Heights":
        return 27
    elif val['borough_area_name'] == "Queens - Northeast Queens":
        return 28
    elif val['borough_area_name'] == "Queens - North Queens":
        return 29
    elif val['borough_area_name'] == "Queens - Central Queens":
        return 30
    elif val['borough_area_name'] == "Queens - Jamaica":
        return 31
    elif val['borough_area_name'] == "Queens - Northwest Queens":
        return 32
    elif val['borough_area_name'] == "Queens - West Central Queens":
        return 33
    elif val['borough_area_name'] == "Queens - Rockaways":
        return 34
    elif val['borough_area_name'] == "Queens - Southeast Queens":
        return 35
    elif val['borough_area_name'] == "Queens - Southwest Queens":
        return 36
    elif val['borough_area_name'] == "Queens - West Queens":
        return 37
    elif val['borough_area_name'] == "Staten Island - Port Richmond":
        return 38
    elif val['borough_area_name'] == "Staten Island - South Shore":
        return 39
    elif val['borough_area_name'] == "Staten Island - Stapleton and St. George":
        return 40
    elif val['borough_area_name'] == "Staten Island - Mid-Island":
        return 41

# Working on the Yelp Business Dataset
mypath = "C:/alan/DSC680/Project1Data/YELPDATA/"
yaml_filename = "config.yaml" # sys.argv[2]
base_dir = Path(mypath)
appdir = Path(os.path.dirname(base_dir))
backdir = Path(os.path.dirname(appdir))
config_path = backdir.joinpath('Config')
ymlfile = config_path.joinpath(yaml_filename)

with open(ymlfile, 'r') as stream:
    try:
        cfg = yaml.safe_load(stream)
        zipcodes = cfg["Get_YELP_DATA"].get("zipcodes")
    except yaml.YAMLError as exc:
        print(exc)
zips = zipcodes.split(",")

boroughs_file = "C:/Alan/DSC680/Project1Data/BoroughAreaZipCodes.csv"
dataset_file = "C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_FinalOUT.csv"
dataset_final_out = "C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_Final_OUT.csv"

boroughs_df = pd.read_csv(boroughs_file)
dataset_df = pd.read_csv(dataset_file)
# Strip leading and trailing spaces.
# dataset_df = dataset_df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

mapping1 = dict(boroughs_df[['zipcode', 'borough']].values)
mapping2 = dict(boroughs_df[['zipcode', 'borough_area_name']].values)
dataset_df['borough'] = dataset_df.zipcode.map(mapping1)
dataset_df['borough_area_name'] = dataset_df.zipcode.map(mapping2)

dataset_df['borough_id'] = dataset_df.apply(borough_id, axis=1)

dataset_df.to_csv(dataset_final_out, index=False)
print("Complete: --- %s seconds has passed ---" % (time.time() - start_time))


"""
pysqldf = lambda t: sqldf(t, globals())
# t = "SELECT distinct interest_level from t_df ;"
t = "SELECT * from data where interest_level = 'medium';"
print(t)
qrt_df = pysqldf(t)

"""