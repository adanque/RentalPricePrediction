"""
Author: Alan Danque
Date:   20210323
Purpose:Gets zip codes using the latitude and longitude. Then removes those rows that are not in NYC.
Complete: --- 1926.4805009365082 seconds has passed ---
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

# Working on the Yelp Business Dataset
mypath = "C:/alan/DSC680/Project1Data/YELPDATA/"
yaml_filename = "config.yaml" # sys.argv[2]
base_dir = Path(mypath)
appdir = Path(os.path.dirname(base_dir))
backdir = Path(os.path.dirname(appdir))
config_path = backdir.joinpath('Config')
ymlfile = config_path.joinpath(yaml_filename)


def parse_zipcode(df, geolocator, lat_field, lon_field):
    # Gets the full address using the lat and long then parse to get the zipcode
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    val = re.search(r'(\d{5}\-?\d{0,4})', str(location))
    try:
        retval = val.group()
    except:
        print("None")
        return "None"
    print(retval)
    return retval
"""
    print(retval)
    if type(retval) == int:
        return "None"
    else:
        return retval
"""

with open(ymlfile, 'r') as stream:
    try:
        cfg = yaml.safe_load(stream)
        zipcodes = cfg["Get_YELP_DATA"].get("zipcodes")
    except yaml.YAMLError as exc:
        print(exc)

filepath = "C:/Alan/DSC680/Project1Data/renthopNYC_Final_OUT.csv"
filepath_final_out = "C:/Alan/DSC680/Project1Data/MasterDataset_high.csv"
data = pd.read_csv(filepath)

pysqldf = lambda t: sqldf(t, globals())
# t = """SELECT distinct interest_level from t_df ;"""
t = "SELECT * from data where interest_level = 'high';"
print(t)
qrt_df = pysqldf(t)

geolocator = geopy.Nominatim(user_agent="http")
qrt_df['zipcode'] = qrt_df.apply(parse_zipcode, axis=1, geolocator=geolocator, lat_field='latitude', lon_field='longitude')

# Remove non NYC records
zips = zipcodes.split(",")
data_df = qrt_df[qrt_df.zipcode.isin(zips)]
data_df.to_csv(filepath_final_out)

print("Complete: --- %s seconds has passed ---" % (time.time() - start_time))

