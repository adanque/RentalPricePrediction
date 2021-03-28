# New York Apartment Rental Price Prediction

## _Predicting Rental Prices in NYC - Evaluating Price Factors !!!Under Construction - Currently in progress!!!_

<a href="https://www.linkedin.com/in/alandanque"> Author: Alan Danque </a>

<a href="https://adanque.github.io/">Click here to go back to Portfolio Website </a>

![A remote image](https://adanque.github.io/assets/img/work-analytics.jpg)

Abstract: 

Everyone likes to have a place of their own that they can call home. A place where one can rest, recharge, and relax. A place where a person can safely store their possessions. Finding such a place can be an ordeal no matter if you are a renter, a homeowner, or a landlord. As the price of any type of home is affected by many different factors. The confusing caveats are trying to understand which factors affect the value or rental price. And if the value is credible or just overly bloated to line someone’s pockets. For example, according to investopia.com there are many locations in New York where the price of a 700 square foot apartment can be between $2,900 and $3,500. (Kopp 2019). However, in Chicago, a similar sized apartment can run about $1,708. (Riley 2019). There are many factors to why the rents are so incredulously different. These include location and proximity to a desired destination. Destinations like work, Ivy league schools, or popular and highly rated clustered locations for food, drink, and entertainment. Other factors also include square footage of the space, how many bedrooms, how many bathrooms and more. As a former landlord, and apartment renter who owns his own home and works for a real estate investment trust – which is a large landlord, I hope to reveal which factors are the more directly influencing factors and predict what the rental price should be close to. I believe this will help those looking for apartments or apartment buildings to have a better sense of the cost and value before they commit to signing.

## Included Project Variables
### Amenities
- bathrooms
- bedrooms
- latitude
- longitude
- price
- interest_level
- elevator
- cats_allowed
- hardwood_floors
- dogs_allowed
- doorman
- dishwasher
- no_fee
- laundry_in_building
- fitness_center
- laundry_in_unit
- roof_deck
- outdoor_space
- dining_room
- high_speed_internet
- balcony
- swimming_pool
- new_construction
- terrace
- exclusive
- loft
- garden_patio
- wheelchair_access
- common_outdoor_space

### Top 40 NYC Employers by Distance according to Fortune Magazine - https://fortune.com/best-workplaces-new-york/2020/search/
| Rank | Name | Industry | Employees | World Wide Revenue | 
| ------ | ------ | ------ | ------ | ------ | 
| 40 | The Goldman Sachs Group, Inc. | Financial Services & Insurance | - | $36,616,000,000 | 
| 39 | Adecco Group brands | Professional Services | - | - | 
| 38 | Live Nation Entertainment | Entertainment | 11,277 | $10,787,800,000 | 
| 37 | Zillow | Information Technology | 5,150 | $1,300,000,000 | 
| 36 | Blackstone | Financial Services & Insurance | - | - | 
| 35 | Voya Financial | Financial Services & Insurance | 5,835 | $8,514,000,000 | 
| 34 | Horizon Media | Advertising & Marketing | 1,908 | - | 
| 33 | Ernst & Young LLP | Professional Services | 260,569 | $34,800,000,000 | 
| 32 | Protiviti | Professional Services | 3,520 | $957,716,000 | 
| 31 | Accenture | Professional Services | 477,000 | $39,573,450,000 | 
| 30 | PricewaterhouseCoopers LLP | Professional Services | 250,000 | $41,300,000,000 | 
| 29 | Dechert LLP | Professional Services | 1,966 | $1,021,751,932 | 
| 28 | Mastercard Incorporated | Financial Services & Insurance | 14,800 | $14,950,000,000 | 
| 27 | KPMG LLP | Professional Services | 207,000 | $28,960,000,000 | 
| 26 | Baker Tilly Virchow Krause, LLP | Professional Services | 3,558 | $630,000,000 | 
| 25 | Comcast NBCUniversal | Telecommunications | 184,000 | $94,507,000,000 | 
| 24 | Atlassian | Information Technology | - | $1,210,126,855 | 
| 23 | Citizens Bank | Financial Services & Insurance | - | $160,000,000,000 | 
| 22 | Capital One Financial Corporation | Financial Services & Insurance | 47,500 | $28,100,000,000 | 
| 21 | Deloitte | Professional Services | 109,778 | $43,200,000,000 | 
| 20 | Adobe | Information Technology | 21,163 | $9,030,000,000 | 
| 19 | Cumberland Farms, Inc. | Retail | - | $3,700,000,000 | 
| 18 | Alston & Bird LLP | Professional Services | 1,610 | $816,473,083 | 
| 17 | DHL Express U.S. | Transportation | 102,540 | $18,197,669,000 | 
| 16 | Workiva Inc. | Information Technology | 1,393 | $244,344,000 | 
| 15 | Dropbox | Information Technology | - | $1,391,700,000 | 
| 14 | Cooley LLP | Professional Services | 2,311 | $1,226,149,000 | 
| 13 | Bain & Company | Professional Services | 10,131 | - | 
| 12 | American Express | Financial Services & Insurance | - | $40,338,000 | 
| 11 | Orrick | Professional Services | 2,400 | $1,046,000,000 | 
| 10 | Shawmut Design and Construction | Construction | - | $1,440,600,000 | 
| 9 | Noom, Inc. | Information Technology | 1,323 | $61,000,000 | 
| 8 | The Cheesecake Factory Incorporated | Hospitality | 38,009 | $2,332,331,000 | 
| 7 | Concord Hospitality Enterprises Company | Hospitality | 5,251 | $41,577,989 | 
| 6 | Box, Inc. | Information Technology | 2,053 | $608,400,000 | 
| 5 | West Monroe Partners | Professional Services | 850 | - | 
| 4 | Wegmans Food Markets, Inc. | Retail | - | $9,217,331,000 | 
| 3 | Power Home Remodeling | Construction | - | $695,000,000 | 
| 2 | Hulu | Media | 2,261 | - | 
| 1 | Salesforce | Information Technology | 40,152 | $13,280,000,000 | 




### Yelp Distance
- Yelp_Highest_Priced_0 -Cluster Center
- Yelp_Highest_Priced_1 -Cluster Center
- Yelp_Highest_Priced_2 -Cluster Center
- Yelp_Highest_Rated_0 -Cluster Center
- Yelp_Highest_Rated_1 -Cluster Center
- Yelp_Highest_Rated_2 -Cluster Center



## Pythonic Libraries Used in this project
Package               Version
--------------------- ---------
- async-generator       1.10
- asyncio               3.4.3
- certifi               2020.12.5
- decorator             4.4.2
- defusedxml            0.7.1
- folium                0.12.1
- geojson               2.5.0
- geopy                 2.1.0
- gmaps                 0.9.0
- gmplot                1.4.1
- greenlet              1.0.0
- htmlmin               0.1.12
- html-parser           0.2
- ImageHash             4.2.0
- imgkit                1.1.0
- importlib-metadata    2.1.1
- joblib                1.0.1
- jsonschema            3.2.0
- MarkupSafe            1.1.1
- matplotlib            3.3.4
- mplleaflet            0.0.5
- networkx              2.5
- notebook              6.3.0
- numpy                 1.20.1
- packaging             20.9
- pandas                1.2.3
- pandas-profiling      2.11.0
- pandasql              0.7.3
- piianalyzer           0.1.0
- pygeohash             1.2.0
- pyodbc                4.0.30
- PyYAML                5.4.1
- requests              2.25.1
- scikit-learn          0.24.1
- scipy                 1.6.1
- seaborn               0.11.1
- Shapely               1.7.1
- simplejson            3.17.2
- sklearn               0.0
- SQLAlchemy            1.4.2
- threadpoolctl         2.1.0
- typing-extensions     3.7.4.3
- urllib3               1.26.4
- websockets            8.1

## Repo Folder Structure

└───Datasets

└───Scripts

└───Results

## Python Files 

| File Name  | Description |
| ------ | ------ |
| JsonYelpDatay.py | Yelp Data Extraction |
| LoopJson.py | Json Data Conversion to Central CSV |
| LoopJsonFiles.py | Loop through JSON files, transform and create consolidated CSV | 
| Pandas_Profiling_Generate_EDA_Reports.py | Quick Descriptive Statistics | 
| RentHop_EDA_Reviews.py | Preliminary Data Wrangling and EDA review | 
| TopNYCEmployerMap.py | Map Top NYC Employers | 
| DistancesToTopNYCEmployers.py | Updates Renthop Apartments with geohashes of the Latitudes and Longitudes | 
| CalculateDistancesToTopNYCEmployers.py | Updates Distances from the Renthop Apartments to the top employers | 
| ClusterNYCYelpRatedBusinesses.py | Creates clusters and gets the centers for these kmeans clusters. Using Yelp Highest Ratings and Yelp Most Expensive Restaurants | 
| NYC_RentHop_ApartmentLocations_Map | Create Map of the locations of the apartments in my master dataset |
| GetZipCode.py | Created to get zipcodes from lat and long so to remove non NYC apartments from the NYC RentHop dataset using a list of valid Zip Codes |
| FinalDataWranglingEDA.py | Final Data Wrangling, strips html, punctuation and cleans up non NYC Zipcode related apartments. | 



| NYCEmployers.csv | NYC Top Employers - https://fortune.com/best-workplaces-new-york/2020/search/ | 
| yelp_business_data.csv | NYC Yelp Businesses  | 
| renthopNYC_Final.csv | FinalDataSet |  


## Results
Under construction

## Maps

### Top NYC Employers - https://fortune.com/best-workplaces-new-york/2020/search
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Top_Employers_Heatmap.png?raw=true)
Heatmap Location for Top Employers In NYC

### RentHop Inventoried Apartments
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_ApartmentLocations_Map.png?raw=true)
Apartment locations contained in my NYC RentHop dataset. Note: the outliers outside of NYC - these will be removed from my final cleaned dataset.
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_ApartmentLocations_Heatmap.png?raw=true)
Above is a heatmap of the apartments located in NYC

### Yelp Top Pricing and Highest Rating
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Highest_Priced_Yelp_Businesses_KMeans_Cluster.png?raw=true)
Plot of the KMeans clusters of Yelp Rated High Priced Businesses

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Top_Rated_Yelp_Businesses_KMeans_Cluster_Centers.png?raw=true)
Map of the centers of each of the KMeans clusters of Yelp Rated High Priced Businesses

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Highest_Priced_Yelp_Businesses_KMeans_Cluster_Centers.png?raw=true)
Plot of the KMeans clusters of the Highest Yelp Rated Businesses 

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Highest_Rated_Yelp_Businesses_KMeans_Cluster.png?raw=true)
Plot of the KMeans clusters of the Highest Yelp Rated Businesses 

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Map_Highest_Priced_Yelp_Businesses_KMeans_Cluster_Centers.png?raw=true)
Map of the centers of each of the KMeans clusters of the Yelp Rated Highest Priced Businesses 

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_Map_Highest_Rated_Yelp_Businesses_KMeans_Cluster_Centers.png?raw=true)
Map of the centers of each of the KMeans clusters of the Highest Yelp Rated Businesses 

## Amenities Review
Interest Levels
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Interest_Level_Pie.png?raw=true)
RentHop Apartment Review Level Breakdown

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Interest_Level_Review.png?raw=true)
RentHop Apartment Review Level Distribution

### Bedrooms
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Bedrooms_Breakdown_by_Interest.png?raw=true)
RentHop Apartment Bedroom Distribution Breakdown

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Bedrooms_Breakdown_by_Interest_Frequency.png?raw=true)
RentHop Apartment Bedroom Distribution Frequency

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Bedrooms_Occurences_Histogram.png?raw=true)
RentHop Apartment Bedroom Distribution by Interest Level

### Bathrooms
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Bathrooms_Occurences_Histogram.png?raw=true)
RentHop Apartment Bathroom Distribution 

![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Bathrooms_Occurences_Violin_Chart.png?raw=true)
RentHop Apartment Violin plot of bathroom by Interest Level

### Pricing Reviews
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Price_Outlier_Detection_Review.png?raw=true)
Pricing Outlier Detection
![A remote image](https://github.com/adanque/RentalPricePrediction/blob/main/results/NYC_RentHop_Price_w90_pct_Max_Price_Excluded.png?raw=true)
Apartment Pricing Distribution

References: 

Kopp, C. (November 2019). How Expensive is it to Live in New York City? Retrieved from: https://www.investopedia.com/articles/personal-finance/012315/how-expensive-new-york-city-really.asp

Riley, E. (July 2019). Cost of Living in Chicago vs. NYC: Which Big City Is Cheaper? Retrieved from: https://streeteasy.com/blog/cost-of-living-in-chicago-vs-nyc/#:~:text=Median%20rent%20for%20a%201,That's%20nothing%20to%20scoff%20at.

