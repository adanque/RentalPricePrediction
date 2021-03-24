"""
Author: Alan Danque
Date:   20210323
Purpose:Extracts Yelp Business Data to JSON for NYC Zip Codes
"""
import requests
import json
import os
import time
from pathlib import Path
# Working on the Yelp Business Dataset
start_time = time.time()
base_dir = "C:/alan/DSC680/Project1Data/YELPDATA/"
appdir = Path(os.path.dirname(base_dir))

csv_filename = "yelp_data_business_"
api_key = 'KEY_REMOVED'
headers = {'Authorization': 'Bearer %s' % api_key}
url = 'https://api.yelp.com/v3/businesses/search'


## creating global empty lists so we don't overwrite them but keep adding data to them
rating = []
zipcode = []
prices = []

# Zip Codes for NYC
# https://worldpostalcode.com/united-states/new-york/new-york-city

zips = ['10001','10002','10003','10004','10005','10006','10007','10008','10009','10010','10011','10012','10013','10014','10016','10017','10018','10019','10020','10021','10022','10023','10024','10025','10026','10027','10028','10029','10030','10031','10032','10033','10034','10035','10036','10037','10038','10039','10040','10041','10043','10044','10045','10055','10060','10065','10069','10075','10080','10081','10087','10090','10101','10102','10103','10104','10105','10106','10107','10108','10109','10110','10111','10112','10113','10114','10115','10116','10117','10118','10119','10120','10121','10122','10123','10124','10125','10126','10128','10129','10130','10131','10132','10133','10138','10150','10151','10152','10153','10154','10155','10156','10157','10158','10159','10160','10161','10162','10163','10164','10165','10166','10167','10168','10169','10170','10171','10172','10173','10174','10175','10176','10177','10178','10179','10185','10199','10203','10211','10212','10213','10242','10249','10256','10258','10259','10260','10261','10265','10268','10269','10270','10271','10272','10273','10274','10275','10276','10277','10278','10279','10280','10281','10282','10285','10286']
for zip in zips:
    #print(zip)
    offset = 0
    tgt_dir = appdir.joinpath(zip)
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