"""
Author: Alan Danque
Date:   20210323
Purpose:Recreates the dataset using only NYC Zip Codes.

Total Rows
Before
    33988
After
    25798
"""
import pandas as pd
import yaml
import os
import time
from pathlib import Path

# Working on the RentHop Dataset
start_time = time.time()
mypath = "C:/alan/DSC680/Project1Data/YELPDATA/"
yaml_filename = "config.yaml"
base_dir = Path(mypath)
appdir = Path(os.path.dirname(base_dir))
backdir = Path(os.path.dirname(appdir))
config_path = backdir.joinpath('Config')
ymlfile = config_path.joinpath(yaml_filename)

filepath = "C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_Final.csv"
filepath_out = "C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_FinalOUT.csv"
data = pd.read_csv(filepath)
data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)

with open(ymlfile, 'r') as stream:
    try:
        cfg = yaml.safe_load(stream)
        zipcodes = cfg["Get_YELP_DATA"].get("zipcodes")
    except yaml.YAMLError as exc:
        print(exc)

print(" Remove Non NYC Apartments ")
zips = zipcodes.split(",")
print(zips)
print(len(zips))

print("Before")
print(len(data))
data_final = data[~data['zipcode'].isin(zips)]
print("After")
print(len(data_final))

data_final.to_csv(filepath_out, index=False)
