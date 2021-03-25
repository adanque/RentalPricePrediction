"""
Author: Alan Danque
Date:   20210323
Purpose:Extracts Yelp Business Data to JSON for NYC Zip Codes
Yelp Review File Complete Duration: --- 7847.622344970703 seconds ---
"""
import ast
import yaml
from yaml import load, dump
import requests
import json
import os
import time
import sys
from pathlib import Path
# Working on the Yelp Business Dataset
start_time = time.time()
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
        csv_filename = cfg["Get_YELP_DATA"].get("csv_filename")
        api_key = cfg["Get_YELP_DATA"].get("api_key")
        headers = eval(cfg["Get_YELP_DATA"].get("headers"))
        url = cfg["Get_YELP_DATA"].get("url")
        zipcodes = cfg["Get_YELP_DATA"].get("zipcodes")

    except yaml.YAMLError as exc:
        print(exc)

## creating global empty lists so we don't overwrite them but keep adding data to them
rating = []
zipcode = []
prices = []

# Zip Codes for NYC
# https://worldpostalcode.com/united-states/new-york/new-york-city

zips = zipcodes.split(",")
for zip in zips:
    #print(zip)
    offset = 0
    YELPDATA = appdir.joinpath('YELPDATA')
    YELPDATA.mkdir(parents=True, exist_ok=True)
    tgt_dir = YELPDATA.joinpath(zip)
    tgt_dir.mkdir(parents=True, exist_ok=True)
    print(tgt_dir)
    ## loop to iterate over 200 pages of 50 businesses each = 10000 businesses in Amsterdam
    while offset <= 200:  # 200
        # params = {'term': 'Restaurants', 'location': 'NYC', 'limit': 50, 'offset': offset}
        params = {'location': zip, 'limit': 50, 'offset': offset}
        req = requests.get(url, params=params, headers=headers)
        parsed = json.loads(req.text)
        filename = csv_filename + str(offset) + '.json'
        file_path = os.path.join(tgt_dir, filename)
        with open(file_path, 'w') as outfile:
            json.dump(parsed, outfile)
        offset += 1
       ## offset can be explained as the page number and with limit can gather max 1000 business data from Yelp every day

print("Yelp Review File Complete Duration: --- %s seconds ---" % (time.time() - start_time))