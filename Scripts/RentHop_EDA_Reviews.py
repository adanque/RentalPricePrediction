
"""
https://www.gps-coordinates.net/
https://moneyinc.com/the-20-biggest-employers-in-nyc/
https://fortune.com/best-workplaces-new-york/2020/search/
"""


from pandasql import sqldf
from pathlib import Path
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import pygeohash
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
color = sns.color_palette()
import time
start_time = time.time()

NYCEmployers = "C:/Alan/DSC680/Project1Data/NYCEmployers.csv"
RentHop = "C:/Alan/DSC680/Project1Data/renthopNYC.csv"
Yelp = "C:/Alan/DSC680/Project1Data/yelp_business_data.csv"
results_dir = Path('C:/Alan/DSC680/Project1Data/').joinpath('results')
results_dir.mkdir(parents=True, exist_ok=True)

# TOP EMPLOYERS
nycemployers_df = pd.read_csv(NYCEmployers,encoding='utf-8', names=["Rank","Name","Industry","HQ Location","Sites","Employees","World Wide Revenue","Latitude","Longitude"],sep=',',header=0,quoting=csv.QUOTE_ALL, engine='python')
nycemployers_df['geohash'] = nycemployers_df.apply(lambda x: pygeohash.encode(x.Latitude, x.Longitude), axis=1)

# RENTHOP
t_df = pd.read_csv(RentHop)
t_df['geohash'] = t_df.apply(lambda x: pygeohash.encode(x.latitude, x.longitude), axis=1)

# YELP DATA
yt_df = pd.read_csv(Yelp)
yt_df.rename(columns={'coordinates.latitude': 'coordinates.longitude', 'latitude': 'longitude'}, inplace=True)
yt_df['geohash'] = t_df.apply(lambda x: pygeohash.encode(x.latitude, x.longitude), axis=1)

print(type(t_df))
print(t_df.shape) # 49,352 obs and 15 vars
print(t_df.columns)

"""
<class 'pandas.core.frame.DataFrame'>
(4996, 24)
Index(['id', 'alias', 'name', 'image_url', 'is_closed', 'url', 'review_count',
       'categories', 'rating', 'transactions', 'price', 'phone',
       'display_phone', 'distance', 'coordinates.latitude',
       'coordinates.longitude', 'location.address1', 'location.address2',
       'location.address3', 'location.city', 'location.zip_code',
       'location.country', 'location.state', 'location.display_address'],
      dtype='object')
"""


#pq.apply(lambda x: get_data_center_val(x.latitude, x.longitude, westval, centralval, eastval), axis=1)
#srcgeoval = pygeohash.encode(lat, long)
#distm_west = pygeohash.geohash_approximate_distance(srcgeoval, westval) / 1000


print(type(t_df))
print(t_df.shape) # 49,352 obs and 15 vars
print(t_df.columns)

"""
<class 'pandas.core.frame.DataFrame'>
(49352, 34)
Index(['bathrooms', 'bedrooms', 'created', 'description', 'display_address',
       'latitude', 'longitude', 'price', 'street_address', 'interest_level',
       'elevator', 'cats_allowed', 'hardwood_floors', 'dogs_allowed',
       'doorman', 'dishwasher', 'no_fee', 'laundry_in_building',
       'fitness_center', 'pre-war', 'laundry_in_unit', 'roof_deck',
       'outdoor_space', 'dining_room', 'high_speed_internet', 'balcony',
       'swimming_pool', 'new_construction', 'terrace', 'exclusive', 'loft',
       'garden_patio', 'wheelchair_access', 'common_outdoor_space'],
      dtype='object')
"""


int_level = t_df['interest_level'].value_counts()

plt.figure(figsize=(8,4))
sns.barplot(int_level.index, int_level.values, alpha=0.8)
plt.ylabel('Frequency', fontsize=12)
plt.xlabel('interest_level', fontsize=12)
plt.title('NYC Apartment Interest Levels')
plt.legend()
img_file = results_dir.joinpath('NYC_RentHop_Interest_Level_Review.png')
plt.savefig(img_file)
plt.show()

plt.pie(int_level, labels=['low', 'medium', 'high'], autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')
plt.title('NYC Apartment Interest Levels')
plt.legend()
img_file = results_dir.joinpath('NYC_RentHop_Interest_Level_Pie.png')
plt.savefig(img_file)
plt.show()

# cont variables analysis
img_file = results_dir.joinpath('NYC_RentHop_Interest_Level.csv')
t_df.describe().to_csv(img_file)

# Write describe results to CSV
img_file = results_dir.joinpath('NYC_RentHop_Interest_Level_Groupings.csv')
t_df.groupby('interest_level').describe().to_csv(img_file)

pysqldf = lambda t: sqldf(t, globals())
# t = """SELECT distinct interest_level from t_df ;"""
t = """SELECT count(*) from t_df where interest_level = 'high';"""
qresults = pysqldf(t)
print(qresults)
#dfs1_sorted = dfs1.sort_values('Date', ascending=True)
#dfs1_sorted.to_csv('.\\datasets\\2015-2020-DataSet.csv')


# There are outliers in the data per max bathrooms in the low interest group.
# May Need to remove the outlier rows
print(t_df.groupby('interest_level').agg(['mean','median','std','max','min'])[['bathrooms']])


cnt_srs = t_df['bathrooms'].value_counts()
plt.figure(figsize=(8,4))
sns.barplot(cnt_srs.index, cnt_srs.values, alpha=0.8, color=color[0])
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('bathrooms', fontsize=12)
plt.title('Bathrooms Occurences')
plt.legend()
img_file = results_dir.joinpath('NYC_RentHop_Bathrooms_Occurences_Histogram.png')
plt.savefig(img_file)
plt.show()

# Remove the rows with excessive bathrooms outliers
pysqldf = lambda t: sqldf(t, globals())
# t = """SELECT distinct interest_level from t_df ;"""
t = """SELECT * from t_df where bathrooms < 3;"""
qrt_df = pysqldf(t)


plt.figure(figsize=(8,4))
sns.violinplot(x='interest_level', y='bathrooms', data=qrt_df)
plt.xlabel('Interest level', fontsize=12)
plt.ylabel('bathrooms', fontsize=12)
plt.title('Bathrooms Occurences')
plt.legend()
img_file = results_dir.joinpath('NYC_RentHop_Bathrooms_Occurences_Violin_Chart.png')
plt.savefig(img_file)
plt.show()

cnt_srs = qrt_df['bedrooms'].value_counts()
plt.figure(figsize=(8,4))
sns.barplot(cnt_srs.index, cnt_srs.values, alpha=0.8, color=color[0])
plt.ylabel('Number of Bedrooms', fontsize=12)
plt.xlabel('Bedrooms', fontsize=12)
plt.title('Bedrooms Occurences')
plt.legend()
img_file = results_dir.joinpath('NYC_RentHop_Bedrooms_Occurences_Histogram.png')
plt.savefig(img_file)
plt.show()

plt.figure(figsize=(8,6))
sns.countplot(x='bedrooms', hue='interest_level', data=qrt_df)
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('bedrooms', fontsize=12)
plt.title('Bedrooms Count by Interest')
plt.legend()
img_file = results_dir.joinpath('NYC_RentHop_Bedrooms_Breakdown_by_Interest.png')
plt.savefig(img_file)
plt.show()

qrt_df.hist(column="bedrooms", by='interest_level')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('bedrooms', fontsize=12)
plt.title('Bedrooms Breakdown by Interest')
plt.legend()
img_file = results_dir.joinpath('NYC_RentHop_Bedrooms_Breakdown_by_Interest_Frequency.png')
plt.savefig(img_file)
plt.show()



img_file = results_dir.joinpath('NYC_RentHop_Price_by_Interest_Level.csv')
qrt_df.groupby('interest_level').agg(['mean','median','std','max','min'])[['price']].to_csv(img_file)

plt.figure(figsize=(8,6))
plt.scatter(range(qrt_df.shape[0]), np.sort(qrt_df.price.values))
plt.xlabel('index', fontsize=12)
plt.ylabel('price', fontsize=12)
plt.title('Price Outlier Detection Review')
plt.legend()
img_file = results_dir.joinpath('NYC_RentHop_Price_Outlier_Detection_Review.png')
plt.savefig(img_file)
plt.show()


# removing outliers:
ulimit = np.percentile(qrt_df.price.values, 99)
print(ulimit)
pysqldf = lambda t: sqldf(t, globals())
# t = """SELECT distinct interest_level from t_df ;"""
t = "SELECT * from qrt_df where bathrooms < 3 and price < " + str(ulimit)+ ";"
print(t)
qrt_df = pysqldf(t)

plt.figure(figsize=(8,6))
sns.distplot(qrt_df.price.values, bins=50, kde=True)
plt.xlabel('price', fontsize=12)
plt.title('Price with 90pct Max Price Excluded')
plt.legend()
img_file = results_dir.joinpath('NYC_RentHop_Price_w90_pct_Max_Price_Excluded.png')
plt.savefig(img_file)
plt.show()

img_file = results_dir.joinpath('NYC_RentHop_Price_And_Interest_Level_After_90pct_Price_Exclusion.csv')
p_int_df = t_df.groupby(['interest_level'])['price']
p_int_df.describe().to_csv(img_file)


#img_file = results_dir.joinpath('NYC RentHop Price by Interest Level.csv')
#qrt_df.groupby('interest_level').agg(['mean','median','std','max','min'])[['price']].to_csv(img_file)



# Remove the rows with excessive bathrooms outliers
pysqldf = lambda t: sqldf(t, globals())
llimit = np.percentile(qrt_df.latitude.values, 1)
ulimit = np.percentile(qrt_df.latitude.values, 99.95)

# t = """SELECT distinct interest_level from t_df ;"""
t = "SELECT * from qrt_df where latitude  < " + str(llimit)+ " and latitude > " + str(ulimit)+ ";"
print(t)
qrt_df2 = pysqldf(t)

plt.figure(figsize=(8,6))
sns.histplot(data=qrt_df2, x="latitude",binwidth=3)
plt.xlabel('latitude', fontsize=12)
plt.title('NYC Renthop Latitude Distribution')
plt.legend()
img_file = results_dir.joinpath('NYC_Renthop_Latitude_Distribution.png')
plt.savefig(img_file)
plt.show()


from mpl_toolkits.basemap import Basemap
from matplotlib import cm
west, south, east, north = -74.02, 40.64, -73.85, 40.86
fig = plt.figure(figsize=(14,10))
ax = fig.add_subplot(111)
m = Basemap(projection='merc', llcrnrlat=south, urcrnrlat=north,
            llcrnrlon=west, urcrnrlon=east, lat_ts=south, resolution='i')
x, y = m(qrt_df2['longitude'].values, qrt_df2['latitude'].values)
m.hexbin(x, y, gridsize=200, bins='log', cmap=cm.YlOrRd_r);





print("Complete: --- %s seconds has passed ---" % (time.time() - start_time))

