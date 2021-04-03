"""
Author: Alan Danque
Date:   20210323
Purpose:Final Data Wrangling, strips html and punctuation.

"""
import pandas as pd
import pygeohash
import csv
from sklearn.tree import export_graphviz
import pydot
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import time
start_time = time.time()
pd.options.mode.chained_assignment = None  # default='warn'  # https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas

results_dir = Path('C:/Alan/DSC680/Project1Data/').joinpath('results')
results_dir.mkdir(parents=True, exist_ok=True)

filepath = "C:/Alan/DSC680/Project1Data/FinalLeadAnalyticsRecord2.csv"
data = pd.read_csv(filepath)
print(data.shape)
shape = data.shape
print('\nDataFrame Shape :', shape)
print('\nNumber of rows :', shape[0])
print('\nNumber of columns :', shape[1])

amsmodel1 = data
del amsmodel1['street_address']
amsmodel1.fillna(0, inplace=True)
#amsmodel1.replace(np.nan,0)

print("Dataframe Loaded: --- %s seconds  ---" % (time.time() - start_time))


# load model and predict
model_file = results_dir.joinpath('My3rdModel.pkl')
with open(model_file, 'rb') as f:
    rf = pickle.load(f)
#rf.predict(X[0:1])
print("Model Loaded: --- %s seconds  ---" % (time.time() - start_time))


target = np.array(amsmodel1['price'])
features = amsmodel1.drop('price', axis = 1)
feature_list = list(features.columns)
features = np.array(features)
print(feature_list)
print(features)
print("Features Loaded: --- %s seconds  ---" % (time.time() - start_time))

import csv
import folium
import pandas as pd
import json
from folium import plugins
#import imgkit
import pygeohash


def borough_val(val):
    if val['borough'] == "Bronx":
        return 0
    elif val['borough'] == "Brooklyn":
        return 1
    elif val['borough'] == "Manhattan":
        return 2
    elif val['borough'] == "Queens":
        return 3
    elif val['borough'] == "Staten Island":
        return 4

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

NYCEmployers = "C:/Alan/DSC680/Project1Data/NYCEmployers.csv"
NYCAttractions = "C:/Alan/DSC680/Project1Data/NYCAttractions.csv"
#Yelp = "C:/Alan/DSC680/Project1Data/yelp_business_data.csv"
YELP_HighestPriced = "C:/Alan/DSC680/Project1Data/YELP_HighestPriced_df.csv"
YELP_HighestRated = "C:/Alan/DSC680/Project1Data/YELP_HighestRated_df.csv"

boroughs_file = "C:/Alan/DSC680/Project1Data/BoroughAreaZipCodes.csv"
boroughs_df = pd.read_csv(boroughs_file)

HighestPriced_df = pd.read_csv(YELP_HighestPriced)
HighestRated_df = pd.read_csv(YELP_HighestRated)

NYCAttractions_df = pd.read_csv(NYCAttractions,encoding='utf-8', names=["name","latitude","longitude","tourism"],sep=',',header=0,quoting=csv.QUOTE_ALL, engine='python')
NYCAttractions_df['geohash'] = NYCAttractions_df.apply(lambda x: pygeohash.encode(x.latitude, x.longitude), axis=1)

nycemployers_df = pd.read_csv(NYCEmployers,encoding='utf-8', names=["Rank","Name","Industry","HQ Location","Sites","Employees","World Wide Revenue","Latitude","Longitude"],sep=',',header=0,quoting=csv.QUOTE_ALL, engine='python')
nycemployers_df['geohash'] = nycemployers_df.apply(lambda x: pygeohash.encode(x.Latitude, x.Longitude), axis=1)


# create a new dataframe that is indexed like the trained model
newdata = pd.DataFrame().reindex_like(amsmodel1)
newdata.fillna(value=0, inplace=True)

# delete the variable to be predicted
del newdata['price']
newdata = newdata.iloc[[1]]

#newdata.to_csv("C:/Alan/DSC680/Project1Data/PredictTestREVIEW.csv")

"""
# Using https://www.renthop.com/listings/808-columbus-ave/09d/60799883

808 Columbus Avenue #09D
Manhattan Valley, Upper West Side, Upper Manhattan, Manhattan
Building: 808 Columbus Avenue
$3,482
Posted 1 hour ago
Studio	1 Bath	442 Sqft
No Fee
"""
# insert information about your apartment

newdata['RandomUnique'] = 0
newdata['bathrooms'] = 1
newdata['bedrooms'] = 0
newdata['latitude'] = 40.7947
newdata['longitude'] = -73.9667
# newdata['price'] = 3482
# newdata['street_address'] = '255 East 61st Street'
newdata['elevator'] = 1
newdata['cats_allowed'] = 1
newdata['hardwood_floors'] = 0
newdata['dogs_allowed'] = 1
newdata['doorman'] = 1
newdata['dishwasher'] = 0
newdata['no_fee'] = 0
newdata['laundry_in_building'] = 1
newdata['fitness_center'] = 1
newdata['pre-war'] = 0
newdata['laundry_in_unit'] = 0
newdata['roof_deck'] = 1
newdata['outdoor_space'] = 0
newdata['dining_room'] = 0
newdata['high_speed_internet'] = 1
newdata['balcony'] = 0
newdata['swimming_pool'] = 0
newdata['new_construction'] = 0
newdata['terrace'] = 0
newdata['exclusive'] = 0
newdata['loft'] = 0
newdata['garden_patio'] = 0
newdata['wheelchair_access'] = 0
newdata['common_outdoor_space'] = 0
newdata['interest_level_val'] = 2
newdata['zipcode'] = 10025
"""
newdata['RandomUnique'] = 0
newdata['bathrooms'] = 1
newdata['bedrooms'] = 0
newdata['latitude'] = 40.7621
newdata['longitude'] = -73.9638
#newdata['price'] = 1850
newdata['elevator'] = 0
newdata['cats_allowed'] = 1
newdata['hardwood_floors'] = 0
newdata['dogs_allowed'] = 1
newdata['doorman'] = 0
newdata['dishwasher'] = 0
newdata['no_fee'] = 0
newdata['laundry_in_building'] = 1
newdata['fitness_center'] = 0
newdata['pre-war'] = 0
newdata['laundry_in_unit'] = 0
newdata['roof_deck'] = 0
newdata['outdoor_space'] = 0
newdata['dining_room'] = 0
newdata['high_speed_internet'] = 0
newdata['balcony'] = 0
newdata['swimming_pool'] = 0
newdata['new_construction'] = 0
newdata['terrace'] = 0
newdata['exclusive'] = 0
newdata['loft'] = 0
newdata['garden_patio'] = 0
newdata['wheelchair_access'] = 0
newdata['common_outdoor_space'] = 0
newdata['interest_level_val'] = 2
newdata['zipcode'] = 10065
"""

newdata['geohash'] = newdata.apply(lambda x: pygeohash.encode(x.latitude, x.longitude), axis=1)
mapping1 = dict(boroughs_df[['zipcode', 'borough']].values)
print(mapping1)
mapping2 = dict(boroughs_df[['zipcode', 'borough_area_name']].values)
print(mapping2)

newdata['borough'] = newdata["zipcode"].map(mapping1)
newdata['borough_area_name'] = newdata.zipcode.map(mapping2)
newdata['borough_id'] = newdata.apply(borough_id, axis=1)
newdata['borough_val'] = newdata.apply(borough_val, axis=1)

# Loop through NYC Attractions to create the distances between attraction to each apartment
NYCAttractions_df['geohash'] = NYCAttractions_df.apply(lambda x: pygeohash.encode(x.latitude, x.longitude), axis=1)
for index, row in NYCAttractions_df.iterrows():
    fieldname = row['name']+" Distance"
    attr_geohash = row['geohash']
    newdata[fieldname] = newdata.apply(lambda x: pygeohash.geohash_approximate_distance(x.geohash, attr_geohash) / 1000, axis=1)

nycemployers_df['geohash'] = nycemployers_df.apply(lambda x: pygeohash.encode(x.Latitude, x.Longitude), axis=1)
for index, row in nycemployers_df.iterrows():
    fieldname = row['Name']+" Distance"
    emp_geohash = row['geohash']
    newdata[fieldname] = newdata.apply(lambda x: pygeohash.geohash_approximate_distance(x.geohash, emp_geohash) / 1000, axis=1)

del newdata['BryantPark_Dist']
del newdata['NicholasMuseum_Dist']
del newdata['OrigBrownStoneH_Dist']
del newdata['GlenSpanArch_Dist']
del newdata['HuddlestoneArch_Dist']
del newdata['LaCasaDeLosT_Dist']
del newdata['YelpHighRated3']

newdata.rename(columns={'Bryant Park Distance':'BryantPark_Dist','Nicholas Roerich Museum Distance':'NicholasMuseum_Dist','Original brown stone houses Distance':'OrigBrownStoneH_Dist','Glen span arch Distance':'GlenSpanArch_Dist','Huddlestone arch Distance':'HuddlestoneArch_Dist','La casa de los Tenenbaums Distance':'LaCasaDeLosT_Dist'}, inplace=True)

#HighestPriced_df['geohash'] = HighestPriced_df.apply(lambda x: pygeohash.encode(x.Latitude, x.Longitude), axis=1)
for i,row in HighestPriced_df.iterrows():
    fieldname = "Yelp_Highest_Priced_"+str(i)
    Y_geohash = row['geohash']
    newdata[fieldname] = newdata.apply(lambda x: pygeohash.geohash_approximate_distance(x.geohash, Y_geohash) / 1000, axis=1)

#HighestRated_df['geohash'] = HighestRated_df.apply(lambda x: pygeohash.encode(x.Latitude, x.Longitude), axis=1)
for i,row in HighestRated_df.iterrows():
    fieldname = "Yelp_Highest_Rated_"+str(i)
    Y_geohash = row['geohash']
    newdata[fieldname] = newdata.apply(lambda x: pygeohash.geohash_approximate_distance(x.geohash, Y_geohash) / 1000, axis=1)

newdata.rename(columns={'Yelp_Highest_Rated_2':'YelpHighRated3'}, inplace=True)

newdata['SynthesizedVar1'] = newdata['bedrooms']+newdata['bathrooms']+newdata['doorman']+newdata['fitness_center']+newdata['laundry_in_unit']+newdata['dishwasher']+newdata['elevator']+newdata['dining_room']+newdata['balcony']+newdata['roof_deck']+newdata['terrace']+newdata['swimming_pool']+newdata['high_speed_internet']+newdata['garden_patio']+newdata['hardwood_floors']+newdata['new_construction']+newdata['wheelchair_access']+newdata['dogs_allowed']+newdata['cats_allowed']+newdata['common_outdoor_space']
newdata['SynthesizedVar4'] = (newdata['bedrooms']*.50)+(newdata['bathrooms']*.496)+(newdata['doorman']*.259)+(newdata['fitness_center']*.227)+(newdata['laundry_in_unit']*.216)+(newdata['dishwasher']*.209)+(newdata['elevator']*.208)+(newdata['dining_room']*.197)+(newdata['balcony']*.127)+(newdata['roof_deck']*.126)+(newdata['terrace']*.116)+newdata['swimming_pool']+(newdata['high_speed_internet']*.09)+(newdata['garden_patio']*.087)+(newdata['hardwood_floors']*.076)+(newdata['new_construction']*.073)+(newdata['wheelchair_access']*.069)+(newdata['dogs_allowed']*.067)+(newdata['cats_allowed']*.06)+(newdata['common_outdoor_space']*.03)
newdata['SynthesizedVar2'] = newdata['YelpHighRated3']+newdata['OrigBrownStoneH_Dist']+newdata['OrigBrownStoneH_Dist']
newdata['SynthesizedVar3'] = newdata['NicholasMuseum_Dist']-newdata['OrigBrownStoneH_Dist']-newdata['LaCasaDeLosT_Dist']-newdata['GlenSpanArch_Dist']-newdata['HuddlestoneArch_Dist']
newdata['SynthesizedVar5'] = newdata['SynthesizedVar1']* newdata['SynthesizedVar4']
newdata['description_length'] = 721
# drop geohash, borough_area_name, borough
del newdata['geohash']
del newdata['borough']
del newdata['borough_area_name']
newdata.fillna(0, inplace=True)
# Reorder the fields
newdata = newdata[['RandomUnique','bathrooms','bedrooms','latitude','longitude','elevator','cats_allowed','hardwood_floors','dogs_allowed','doorman','dishwasher','no_fee','laundry_in_building','fitness_center','pre-war','laundry_in_unit','roof_deck','outdoor_space','dining_room','high_speed_internet','balcony','swimming_pool','new_construction','terrace','exclusive','loft','garden_patio','wheelchair_access','common_outdoor_space','The Goldman Sachs Group, Inc. Distance','Adecco Group brands Distance','Live Nation Entertainment Distance','Zillow Distance','Blackstone Distance','Voya Financial Distance','Horizon Media Distance','Ernst & Young LLP Distance','Protiviti Distance','Accenture Distance','PricewaterhouseCoopers LLP Distance','Dechert LLP Distance','Mastercard Incorporated Distance','KPMG LLP Distance','Baker Tilly Virchow Krause, LLP Distance','Comcast NBCUniversal Distance','Atlassian Distance','Citizens Bank Distance','Capital One Financial Corporation Distance','Deloitte Distance','Adobe Distance','Cumberland Farms, Inc. Distance','Alston & Bird LLP Distance','DHL Express U.S. Distance','Workiva Inc. Distance','Dropbox Distance','Cooley LLP Distance','Bain & Company Distance','American Express Distance','Orrick Distance','Shawmut Design and Construction Distance','Noom, Inc. Distance','The Cheesecake Factory Incorporated Distance','Concord Hospitality Enterprises Company Distance','Box, Inc. Distance','West Monroe Partners Distance','Wegmans Food Markets, Inc. Distance','Power Home Remodeling Distance','Hulu Distance','Salesforce Distance','Yelp_Highest_Priced_0','Yelp_Highest_Priced_1','Yelp_Highest_Priced_2','Yelp_Highest_Rated_0','Yelp_Highest_Rated_1','YelpHighRated3','zipcode','1 World Trade Center Distance','80 South Street Distance','Access High Line Park Distance','American Icon Distance','Anton Kern Gallery Distance','Archibalds Townhouse Distance','Arguably the best location to see evening Manhattan Henge Distance','BAC Distance','Barthmans Sidewalk Clock Distance','big gay ice cream Distance','Bloody Angle Distance','BryantPark_Dist','California Sea Lion Distance','Canal Street Distance','Canal street market Distance','Carrie Bradshaw House Distance','Casa di Carrie Distance','Chelsea Distance','Chelsea Flea Market Distance','Chelsea Market Distance','Chinatown Distance','Circle line ferrys Distance','Classic Car Club Manhattan Distance','Cocktail Kingdom Distance','Colonnade row Distance','Color Factory Distance','Cortlandt Alley Distance','Couv Led Zepp 5e album Distance','Curry hill Distance','Delacorte Musical Clock Distance','Diamond District Distance','Dream house Distance','Dr Nevilles I Am Legend townhouse Distance','Empire State Building Distance','Explore Chinatown Information Kiosk Distance','Flatiron District Distance','Food Truck Street Distance','Free Kayaking with the Downtown Boathouse Distance','Free Public Stargazing Distance','Friends Building Distance','Gapstow bridge Distance','Gentoo Penguin Distance','GlenSpanArch_Dist','Greenwich Village Distance','Grey houndiin bus stop Distance','Grizzly Bear Distance','Grove Court Distance','Hangmans Elm Distance','High Line Access Distance','High Line Park Distance','HuddlestoneArch_Dist','Kayak Brooklyn Distance','LaCasaDeLosT_Dist','La de forest house Distance','Le Petit Versailles Distance','LES SKATEPARK Distance','Liz Christy Garden Distance','Low Line Park Distance','Mad about you building Distance','Mahayanna Buddhist Center Distance','Maison sur les toits Distance','Mark Twain House Distance','Meatpacking District Distance','NBC Studios Distance','NicholasMuseum_Dist','Nicola Tesla corner Distance','NY Skyride Distance','OrigBrownStoneH_Dist','paparazzi dogman and paparazzi rabbitgirl Distance','Paul Nicklen Gallery Distance','Point de vue 17e rue Distance','Puffin Distance','Red Panda Distance','Rockefeller Center Distance','Rowboat rentals Distance','Salmagundi club Distance','Schwartz Luggage Storage Distance','Seal Distance','Sea Lions Distance','Sightseeing Pass, LLC Distance','Site of the Beach Pneumatic Subway Distance','Snow Leopard Distance','Snow Monkey Distance','SoHo Distance','South Street Seaport Distance','Spyscape Distance','Statue of Liberty Distance','Stonewall Inn Distance','Textile building Distance','The High Line Distance','The High Line North Entrance Distance','The Ride Distance','Times Square Distance','Tortoise Distance','TriBeCa Distance','Tropical Zone Distance','Umpire rock Distance','description_length','borough_id','borough_val','interest_level_val','SynthesizedVar1','SynthesizedVar4','SynthesizedVar2','SynthesizedVar3','SynthesizedVar5']]
newdata.to_csv("C:/Alan/DSC680/Project1Data/PredictTestRec.csv")

print(newdata.columns)
print(newdata.shape)
print(newdata)


result = rf.predict(newdata)
print(type(result))
print(result)

print("Prediction Complete: --- %s seconds  ---" % (time.time() - start_time))


"""

<class 'numpy.ndarray'>
[1850.125]
Prediction Complete: --- 3.287870168685913 seconds  ---

newdata['RandomUnique'] = 0
newdata['bathrooms'] = 1
newdata['bedrooms'] = 0
newdata['latitude'] = 40.7621
newdata['longitude'] = -73.9638
#newdata['price'] = 1850
newdata['elevator'] = 0
newdata['cats_allowed'] = 1
newdata['hardwood_floors'] = 0
newdata['dogs_allowed'] = 1
newdata['doorman'] = 0
newdata['dishwasher'] = 0
newdata['no_fee'] = 0
newdata['laundry_in_building'] = 1
newdata['fitness_center'] = 0
newdata['pre-war'] = 0
newdata['laundry_in_unit'] = 0
newdata['roof_deck'] = 0
newdata['outdoor_space'] = 0
newdata['dining_room'] = 0
newdata['high_speed_internet'] = 0
newdata['balcony'] = 0
newdata['swimming_pool'] = 0
newdata['new_construction'] = 0
newdata['terrace'] = 0
newdata['exclusive'] = 0
newdata['loft'] = 0
newdata['garden_patio'] = 0
newdata['wheelchair_access'] = 0
newdata['common_outdoor_space'] = 0
newdata['The Goldman Sachs Group, Inc. Distance'] = 19.545
newdata['Adecco Group brands Distance'] = 3.803
newdata['Live Nation Entertainment Distance'] = 19.545
newdata['Zillow Distance'] = 625.441
newdata['Blackstone Distance'] = 19.545
newdata['Voya Financial Distance'] = 19.545
newdata['Horizon Media Distance'] = 19.545
newdata['Ernst & Young LLP Distance'] = 3.803
newdata['Protiviti Distance'] = 3.803
newdata['Accenture Distance'] = 19.545
newdata['PricewaterhouseCoopers LLP Distance'] = 3.803
newdata['Dechert LLP Distance'] = 3.803
newdata['Mastercard Incorporated Distance'] = 3.803
newdata['KPMG LLP Distance'] = 3.803
newdata['Baker Tilly Virchow Krause, LLP Distance'] = 3.803
newdata['Comcast NBCUniversal Distance'] = 3.803
newdata['Atlassian Distance'] = 19.545
newdata['Citizens Bank Distance'] = 3.803
newdata['Capital One Financial Corporation Distance'] = 19.545
newdata['Deloitte Distance'] = 3.803
newdata['Adobe Distance'] = 3.803
newdata['Cumberland Farms, Inc. Distance'] = 123.264
newdata['Alston & Bird LLP Distance'] = 3.803
newdata['DHL Express U.S. Distance'] = 19.545
newdata['Workiva Inc. Distance'] = 3.803
newdata['Dropbox Distance'] = 3.803
newdata['Cooley LLP Distance'] = 3.803
newdata['Bain & Company Distance'] = 3.803
newdata['American Express Distance'] = 19.545
newdata['Orrick Distance'] = 3.803
newdata['Shawmut Design and Construction Distance'] = 3.803
newdata['Noom, Inc. Distance'] = 3.803
newdata['The Cheesecake Factory Incorporated Distance'] = 19.545
newdata['Concord Hospitality Enterprises Company Distance'] = 19.545
newdata['Box, Inc. Distance'] = 3.803
newdata['West Monroe Partners Distance'] = 3.803
newdata['Wegmans Food Markets, Inc. Distance'] = 19.545
newdata['Power Home Remodeling Distance'] = 123.264
newdata['Hulu Distance'] = 19.545
newdata['Salesforce Distance'] = 3.803
newdata['Yelp_Highest_Priced_0'] = 19.545
newdata['Yelp_Highest_Priced_1'] = 3.803
newdata['Yelp_Highest_Priced_2'] = 19.545
newdata['Yelp_Highest_Rated_0'] = 3.803
newdata['Yelp_Highest_Rated_1'] = 19.545
newdata['YelpHighRated3'] = 625.441
newdata['zipcode'] = 10065
newdata['1 World Trade Center Distance'] = 19.545
newdata['80 South Street Distance'] = 19.545
newdata['Access High Line Park Distance'] = 3.803
newdata['American Icon Distance'] = 19.545
newdata['Anton Kern Gallery Distance'] = 3.803
newdata['Archibalds Townhouse Distance'] = 3.803
newdata['Arguably the best location to see evening Manhattan Henge Distance'] = 3.803
newdata['BAC Distance'] = 3.803
newdata['Barthmans Sidewalk Clock Distance'] = 19.545
newdata['big gay ice cream Distance'] = 19.545
newdata['Bloody Angle Distance'] = 19.545
newdata['BryantPark_Dist'] = 3.803
newdata['California Sea Lion Distance'] = 3.803
newdata['Canal Street Distance'] = 19.545
newdata['Canal street market Distance'] = 19.545
newdata['Carrie Bradshaw House Distance'] = 19.545
newdata['Casa di Carrie Distance'] = 19.545
newdata['Chelsea Distance'] = 3.803
newdata['Chelsea Flea Market Distance'] = 3.803
newdata['Chelsea Market Distance'] = 19.545
newdata['Chinatown Distance'] = 19.545
newdata['Circle line ferrys Distance'] = 3.803
newdata['Classic Car Club Manhattan Distance'] = 19.545
newdata['Cocktail Kingdom Distance'] = 3.803
newdata['Colonnade row Distance'] = 19.545
newdata['Color Factory Distance'] = 19.545
newdata['Cortlandt Alley Distance'] = 19.545
newdata['Couv Led Zepp 5e album Distance'] = 19.545
newdata['Curry hill Distance'] = 3.803
newdata['Delacorte Musical Clock Distance'] = 3.803
newdata['Diamond District Distance'] = 3.803
newdata['Dream house Distance'] = 19.545
newdata['Dr Nevilles I Am Legend townhouse Distance'] = 19.545
newdata['Empire State Building Distance'] = 3.803
newdata['Explore Chinatown Information Kiosk Distance'] = 19.545
newdata['Flatiron District Distance'] = 3.803
newdata['Food Truck Street Distance'] = 3.803
newdata['Free Kayaking with the Downtown Boathouse Distance'] = 19.545
newdata['Free Public Stargazing Distance'] = 19.545
newdata['Friends Building Distance'] = 19.545
newdata['Gapstow bridge Distance'] = 3.803
newdata['Gentoo Penguin Distance'] = 3.803
newdata['GlenSpanArch_Dist'] = 625.441
newdata['Greenwich Village Distance'] = 19.545
newdata['Grey houndiin bus stop Distance'] = 3.803
newdata['Grizzly Bear Distance'] = 3.803
newdata['Grove Court Distance'] = 19.545
newdata['Hangmans Elm Distance'] = 19.545
newdata['High Line Access Distance'] = 19.545
newdata['High Line Park Distance'] = 19.545
newdata['HuddlestoneArch_Dist'] = 625.441
newdata['Kayak Brooklyn Distance'] = 19.545
newdata['LaCasaDeLosT_Dist'] = 625.441
newdata['La de forest house Distance'] = 19.545
newdata['Le Petit Versailles Distance'] = 19.545
newdata['LES SKATEPARK Distance'] = 19.545
newdata['Liz Christy Garden Distance'] = 19.545
newdata['Low Line Park Distance'] = 19.545
newdata['Mad about you building Distance'] = 19.545
newdata['Mahayanna Buddhist Center Distance'] = 19.545
newdata['Maison sur les toits Distance'] = 19.545
newdata['Mark Twain House Distance'] = 19.545
newdata['Meatpacking District Distance'] = 19.545
newdata['NBC Studios Distance'] = 3.803
newdata['NicholasMuseum_Dist'] = 625.441
newdata['Nicola Tesla corner Distance'] = 3.803
newdata['NY Skyride Distance'] = 3.803
newdata['OrigBrownStoneH_Dist'] = 625.441
newdata['paparazzi dogman and paparazzi rabbitgirl Distance'] = 3.803
newdata['Paul Nicklen Gallery Distance'] = 19.545
newdata['Point de vue 17e rue Distance'] = 19.545
newdata['Puffin Distance'] = 3.803
newdata['Red Panda Distance'] = 3.803
newdata['Rockefeller Center Distance'] = 3.803
newdata['Rowboat rentals Distance'] = 3.803
newdata['Salmagundi club Distance'] = 19.545
newdata['Schwartz Luggage Storage Distance'] = 3.803
newdata['Seal Distance'] = 3.803
newdata['Sea Lions Distance'] = 3.803
newdata['Sightseeing Pass, LLC Distance'] = 3.803
newdata['Site of the Beach Pneumatic Subway Distance'] = 19.545
newdata['Snow Leopard Distance'] = 3.803
newdata['Snow Monkey Distance'] = 3.803
newdata['SoHo Distance'] = 19.545
newdata['South Street Seaport Distance'] = 19.545
newdata['Spyscape Distance'] = 3.803
newdata['Statue of Liberty Distance'] = 19.545
newdata['Stonewall Inn Distance'] = 19.545
newdata['Textile building Distance'] = 19.545
newdata['The High Line Distance'] = 3.803
newdata['The High Line North Entrance Distance'] = 3.803
newdata['The Ride Distance'] = 3.803
newdata['Times Square Distance'] = 3.803
newdata['Tortoise Distance'] = 3.803
newdata['TriBeCa Distance'] = 19.545
newdata['Tropical Zone Distance'] = 3.803
newdata['Umpire rock Distance'] = 3.803
newdata['description_length'] = 721
newdata['borough_id'] = 25
newdata['borough_val'] = 2
newdata['interest_level_val'] = 2
newdata['SynthesizedVar1'] = 3
newdata['SynthesizedVar4'] = 0.623
newdata['SynthesizedVar2'] = 1876.323
newdata['SynthesizedVar3'] = -1876.323
newdata['SynthesizedVar5'] = 1.869


"""
