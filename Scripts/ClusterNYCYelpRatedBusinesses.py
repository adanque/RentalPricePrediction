"""
Author: Alan Danque
Date:   20210323
Purpose:Cluster the coordinates

References:
https://moneyinc.com/the-20-biggest-employers-in-nyc/
https://fortune.com/best-workplaces-new-york/2020/search/

"""
from pathlib import Path
from pandasql import sqldf
import csv
import folium
import pandas as pd
import json
from folium import plugins
#import imgkit
import pygeohash
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns; sns.set()
import csv
results_dir = Path('C:/Alan/DSC680/Project1Data/').joinpath('results')
results_dir.mkdir(parents=True, exist_ok=True)

# TOP EMPLOYERS
# YELP DATA
Yelp = "C:/Alan/DSC680/Project1Data/yelp_business_data.csv"
t_df = pd.read_csv(Yelp)
t_df.rename(columns={'coordinates.latitude':'latitude', 'coordinates.longitude':'longitude', 'location.address1':'address', 'location.city':'city', 'location.zip_code':'zip_code', 'location.country':'country', 'location.state':'state', 'location.display_address':'display_address' }, inplace=True)
t_df['geohash'] = t_df.apply(lambda x: pygeohash.encode(x.latitude, x.longitude), axis=1)
t_df['rated_price'] = t_df['price'].str.len()
#print(t_df['rated_price'].head(10))
#print(type(t_df))
#print(t_df.shape) # 49,352 obs and 15 vars
#print(t_df.columns)
#print(yt_df.head(10))
# Drop any null lat and longs
t_df.dropna(axis=0,how='any',subset=['latitude','longitude'],inplace=True)
#t_df.head(10)

#print("this type")
#print(type(t_df))
pysqldf = lambda t: sqldf(t, globals())
# t = """SELECT distinct interest_level from t_df ;"""
vt_df = """SELECT max(rated_price) as max_rated_price from t_df ;"""
max_rated_price = pysqldf(vt_df)
max_rated_price_val = max_rated_price['max_rated_price'].values[0]
print(max_rated_price_val)

yt_df = f"SELECT * from t_df where rated_price = ({max_rated_price_val});"
qresults = pysqldf(yt_df)


print(qresults.shape) # 49,352 obs and 15 vars
print(qresults.columns)
print(type(qresults))
print(qresults)
print(qresults.head(10))

X=qresults.loc[:,['name','latitude','longitude']]
Y_axis = qresults[['latitude']]
X_axis = qresults[['longitude']]

# Clustering using K-Means and Assigning Clusters to our Data
kmeans = KMeans(n_clusters = 3, init ='k-means++')
kmeans.fit(X[X.columns[1:3]]) # Compute k-means clustering. # Compute k-means clustering.
X['cluster_label'] = kmeans.fit_predict(X[X.columns[1:3]])
#print("X['cluster_label']")
#print(X['cluster_label'])
centers = kmeans.cluster_centers_ # Coordinates of cluster centers.
labels = kmeans.predict(X[X.columns[1:3]]) # Labels of each point
#print(X.head(10))

X.plot.scatter(x = 'latitude', y = 'longitude', c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.title('NYC Highest Priced Yelp Businesses KMeans Cluster')
plt.legend()
img_file = results_dir.joinpath('NYC_Highest_Priced_Yelp_Businesses_KMeans_Cluster.png')
plt.savefig(img_file)
plt.show()

print("Cluster Centers NYC_Highest_Priced_Yelp_Businesses_KMeans_Cluster")
print(labels)
print(centers)
print(type(centers))
df = pd.DataFrame(centers, columns = ['Latitude','Longitude'])
HighestPriced_df = df

"""
Our Cluster Centers
[[ 40.71360594 -74.00834961]
 [ 40.76068284 -73.97826484]
 [ 40.73287131 -73.99541715]]
"""

with open('boroughs.geojson') as f:
    laArea = json.load(f)
#initialize the map around LA County
laMap = folium.Map(location=[40.7078,-74.0337], zoom_start=12)
#add the shape of LA County to the map
folium.GeoJson(laArea).add_to(laMap)
#for each row in the Starbucks dataset, plot the corresponding latitude and longitude on the map
for i,row in df.iterrows():
    folium.CircleMarker((row.Latitude,row.Longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(laMap)
#save the map as an html
laMap.save('NYC_Highest_Priced_Yelp_Businesses_KMeans_Cluster_Centers.html')
#imgkit.from_file('C:\\Users\\aland\\PycharmProjects\\RentalPricePrediction\\NYC_Top_Employers_Point_Map.html', 'C:\\Users\\aland\\PycharmProjects\\RentalPricePrediction\\NYC_Top_Employers_Point_Map.jpg')

################################### ################################### ###################################



pysqldf = lambda t: sqldf(t, globals())
# t = """SELECT distinct interest_level from t_df ;"""
vt_df = """SELECT max(rating) as max_rating from t_df ;"""
max_rating = pysqldf(vt_df)
max_rating_val = max_rating['max_rating'].values[0]
print(max_rated_price_val)

yt_df = f"SELECT * from t_df where rating = ({max_rating_val});"
qresults = pysqldf(yt_df)


print(qresults.shape) # 49,352 obs and 15 vars
print(qresults.columns)
print(type(qresults))
print(qresults)
print(qresults.head(10))

X=qresults.loc[:,['name','latitude','longitude']]
Y_axis = qresults[['latitude']]
X_axis = qresults[['longitude']]

# Clustering using K-Means and Assigning Clusters to our Data
kmeans = KMeans(n_clusters = 3, init ='k-means++')
kmeans.fit(X[X.columns[1:3]]) # Compute k-means clustering. # Compute k-means clustering.
X['cluster_label'] = kmeans.fit_predict(X[X.columns[1:3]])
#print("X['cluster_label']")
#print(X['cluster_label'])
centers = kmeans.cluster_centers_ # Coordinates of cluster centers.
labels = kmeans.predict(X[X.columns[1:3]]) # Labels of each point
#print(X.head(10))

X.plot.scatter(x = 'latitude', y = 'longitude', c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.title('NYC Highest Rated Yelp Businesses KMeans Cluster')
plt.legend()
img_file = results_dir.joinpath('NYC_Highest_Rated_Yelp_Businesses_KMeans_Cluster.png')
plt.savefig(img_file)
plt.show()

print("Cluster Centers NYC_Highest_Rated_Yelp_Businesses_KMeans_Cluster")
print(labels)
print(centers)
print(type(centers))
df = pd.DataFrame(centers, columns = ['Latitude','Longitude'])
HighestRated_df = df
"""
Our Cluster Centers
[[ 40.71570017 -74.00162143]
 [ 40.80175434 -73.94419938]
 [ 40.76213922 -73.98069774]]
"""

with open('boroughs.geojson') as f:
    laArea = json.load(f)
#initialize the map around LA County
laMap = folium.Map(location=[40.7078,-74.0337], zoom_start=12)
#add the shape of LA County to the map
folium.GeoJson(laArea).add_to(laMap)
#for each row in the Starbucks dataset, plot the corresponding latitude and longitude on the map
for i,row in df.iterrows():
    folium.CircleMarker((row.Latitude,row.Longitude), radius=3, weight=2, color='red', fill_color='red', fill_opacity=.5).add_to(laMap)
#save the map as an html
laMap.save('NYC_Highest_Rated_Yelp_Businesses_KMeans_Cluster_Centers.html')
#imgkit.from_file('C:\\Users\\aland\\PycharmProjects\\RentalPricePrediction\\NYC_Top_Employers_Point_Map.html', 'C:\\Users\\aland\\PycharmProjects\\RentalPricePrediction\\NYC_Top_Employers_Point_Map.jpg')

RentHopData = "C:/Alan/DSC680/Project1Data/renthopNYC_OUT.csv"
RentHop_Out = "C:/Alan/DSC680/Project1Data/renthopNYC_Final.csv"
renthop_df = pd.read_csv(RentHopData)

HighestPriced_df['geohash'] = HighestPriced_df.apply(lambda x: pygeohash.encode(x.Latitude, x.Longitude), axis=1)
for i,row in HighestPriced_df.iterrows():
    fieldname = "Yelp_Highest_Priced_"+str(i)
    Y_geohash = row['geohash']
    renthop_df[fieldname] = renthop_df.apply(lambda x: pygeohash.geohash_approximate_distance(x.geohash, Y_geohash) / 1000, axis=1)

HighestRated_df['geohash'] = HighestRated_df.apply(lambda x: pygeohash.encode(x.Latitude, x.Longitude), axis=1)
for i,row in HighestRated_df.iterrows():
    fieldname = "Yelp_Highest_Rated_"+str(i)
    Y_geohash = row['geohash']
    renthop_df[fieldname] = renthop_df.apply(lambda x: pygeohash.geohash_approximate_distance(x.geohash, Y_geohash) / 1000, axis=1)

renthop_df.to_csv(RentHop_Out)