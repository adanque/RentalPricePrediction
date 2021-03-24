"""
Author: Alan Danque
Date:   20210323
Purpose:Loads all json files from all zip named subfolders into one csv

"""
import os
import json
import pandas as pd
import glob
import time

start_time = time.time()
dataout = []

csv_filename = "C:/alan/DSC680/Project1Data/YELPDATA/yelp_business_data.csv"
if os.path.exists(csv_filename):
    os.remove(csv_filename)

folder = "C:/alan/DSC680/Project1Data/YELPDATA/"
subfolders = [ f.path for f in os.scandir(folder) if f.is_dir() ]
print(subfolders)
for fpath in subfolders:
    folderpath = fpath+"/*.json"
    for filename in glob.glob(folderpath):
        print('Processing file: ' + filename)
        f = open(filename)
        data = json.load(f)
        print(data)
        print(data["businesses"][0].keys())
        d = data["businesses"][0]
        dataout.append(d)
        #with open(filename, encoding="utf8", errors='ignore') as f:
        #    for line in f:
        #        data = json.loads(line)
        #        dataout.append(data)

#print(d)
#df = pd.DataFrame(d)
df = pd.json_normalize(dataout)
df.to_csv(csv_filename, encoding='utf-8', index=False)

# json_struct = json.loads(df.to_json(orient="records"))
#df_flat = pd.json_normalize(json_struct)
#df_flat.to_csv(csv_filename, encoding='utf-8', index=False)
#df.to_csv(csv_filename, encoding='utf-8', index=False)

print("Yelp Review File Complete Duration: --- %s seconds ---" % (time.time() - start_time))