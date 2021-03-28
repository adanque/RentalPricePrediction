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

### NYC Attractions
 | name | latitude | longitude | tourism | 
 | ------ | ------ | ------ | ------ | 
 | 1 World Trade Center | -74.0131898 | 40.7130055 | attraction | 
 | 80 South Street | -74.0043915 | 40.7056076 | attraction | 
 | Access High Line Park | -74.0018026 | 40.7523844 | attraction | 
 | American Icon | -74.0035301 | 40.7172272 | attraction | 
 | Anton Kern Gallery | -73.9739449 | 40.7611132 | attraction | 
 | Archibalds Townhouse | -73.9656246 | 40.7733291 | attraction | 
 | Arguably the best location to see evening Manhattan Henge | -73.9812647 | 40.7471958 | attraction | 
 | BAC | -73.9973055 | 40.7560503 | attraction | 
 | Barthmans Sidewalk Clock | -74.0099251 | 40.7098196 | attraction | 
 | big gay ice cream | -73.9847678 | 40.7264894 | attraction | 
 | Bloody Angle | -73.9981297 | 40.7144199 | attraction | 
 | Bryant Park | -73.9839079 | 40.7535129 | attraction | 
 | California Sea Lion | -73.9717588 | 40.7678191 | attraction | 
 | Canal Street | -73.9985965 | 40.7171153 | attraction | 
 | Canal street market | -74.0008621 | 40.718987 | attraction | 
 | Carrie Bradshaw House | -74.0038558 | 40.7353656 | attraction | 
 | Casa di Carrie | -74.0038435 | 40.735302 | attraction | 
 | Chelsea | -74.0018779 | 40.7458699 | attraction | 
 | Chelsea Flea Market | -73.9903215 | 40.7436929 | attraction | 
 | Chelsea Market | -74.0069958 | 40.7429237 | attraction | 
 | Chinatown | -73.9984718 | 40.7156258 | attraction | 
 | Circle line ferrys | -74.0015777 | 40.7628258 | attraction | 
 | Classic Car Club Manhattan | -74.0047756 | 40.7580807 | attraction | 
 | Cocktail Kingdom | -73.9907173 | 40.7436082 | attraction | 
 | Colonnade row | -73.9924535 | 40.7292801 | attraction | 
 | Color Factory | -74.0062226 | 40.7258445 | attraction | 
 | Cortlandt Alley | -74.0023028 | 40.7177394 | attraction | 
 | Couv Led Zepp 5e album | -73.9850116 | 40.7273462 | attraction | 
 | Curry hill | -73.9824692 | 40.7426274 | attraction | 
 | Delacorte Musical Clock | -73.9711748 | 40.7681148 | attraction | 
 | Diamond District | -73.9801423 | 40.7572421 | attraction | 
 | Dream house | -74.0048345 | 40.7184995 | attraction | 
 | Dr Nevilles I Am Legend townhouse | -73.9965692 | 40.7313957 | attraction | 
 | Empire State Building | -73.9849958 | 40.7481629 | attraction | 
 | Explore Chinatown Information Kiosk | -73.9992431 | 40.7173684 | attraction | 
 | Flatiron District | -73.9896534 | 40.7410723 | attraction | 
 | Food Truck Street | -73.9814247 | 40.7570048 | attraction | 
 | Free Kayaking with the Downtown Boathouse | -74.0122141 | 40.6915007 | attraction | 
 | Free Public Stargazing | -73.9835751 | 40.7725563 | attraction | 
 | Free Public Stargazing | -74.0077867 | 40.7420581 | attraction | 
 | Friends Building | -74.0052999 | 40.7323595 | attraction | 
 | Gapstow bridge | -73.9738339 | 40.7669279 | attraction | 
 | Gentoo Penguin | -73.971457 | 40.76833 | attraction | 
 | Glen span arch | -73.9591072 | 40.7947039 | attraction | 
 | Greenwich Village | -74.0028172 | 40.7335845 | attraction | 
 | Grey houndiin bus stop | -73.994485 | 40.7575015 | attraction | 
 | Grizzly Bear | -73.971913 | 40.7684112 | attraction | 
 | Grove Court | -74.0057762 | 40.7321796 | attraction | 
 | Hangmans Elm | -73.998611 | 40.7318891 | attraction | 
 | High Line Access | -74.0045942 | 40.7467802 | attraction | 
 | High Line Park | -74.0066972 | 40.7451181 | attraction | 
 | Huddlestone arch | -73.9556352 | 40.7958355 | attraction | 
 | Kayak Brooklyn | -73.997566 | 40.6995561 | attraction | 
 | La casa de los Tenenbaums | -73.9465643 | 40.8237943 | attraction | 
 | La de forest house | -73.9946773 | 40.7331991 | attraction | 
 | Le Petit Versailles | -73.9818662 | 40.7210729 | attraction | 
 | LES SKATEPARK | -73.9933152 | 40.7110791 | attraction | 
 | Liz Christy Garden | -73.9921517 | 40.7242411 | attraction | 
 | Low Line Park | -73.9871259 | 40.7203545 | attraction | 
 | Mad about you building | -73.9946122 | 40.7346862 | attraction | 
 | Mahayanna Buddhist Center | -73.995237 | 40.71641 | attraction | 
 | Maison sur les toits | -73.9883555 | 40.72332 | attraction | 
 | Mark Twain House | -73.9964593 | 40.7337058 | attraction | 
 | Meatpacking District | -74.0075113 | 40.7409503 | attraction | 
 | NBC Studios | -73.9796681 | 40.7591425 | attraction | 
 | Nicholas Roerich Museum | -73.9689522 | 40.8027945 | attraction | 
 | Nicola Tesla corner | -73.9846757 | 40.7535873 | attraction | 
 | NY Skyride | -73.9856549 | 40.7483272 | attraction | 
 | Original brown stone houses | -73.9474058 | 40.8230348 | attraction | 
 | paparazzi dogman and paparazzi rabbitgirl | -73.9806283 | 40.7599935 | attraction | 
 | Paul Nicklen Gallery | -74.0033029 | 40.7226903 | attraction | 
 | Point de vue 17e rue | -74.0069385 | 40.7440976 | attraction | 
 | Puffin | -73.9713336 | 40.768196 | attraction | 
 | Red Panda | -73.9727846 | 40.7682914 | attraction | 
 | Rockefeller Center | -73.9788005 | 40.7588448 | attraction | 
 | Rowboat rentals | -73.9690887 | 40.7749309 | attraction | 
 | Salmagundi club | -73.9945529 | 40.7343017 | attraction | 
 | Schwartz Luggage Storage | -73.9945593 | 40.7552442 | attraction | 
 | Seal | -73.9716059 | 40.7683716 | attraction | 
 | Sea Lions | -73.9717654 | 40.767841 | attraction | 
 | Sightseeing Pass, LLC | -73.9875915 | 40.7608187 | attraction | 
 | Site of the Beach Pneumatic Subway | -74.0065761 | 40.7129806 | attraction | 
 | Snow Leopard | -73.9726493 | 40.7686429 | attraction | 
 | Snow Monkey | -73.9723113 | 40.7681797 | attraction | 
 | SoHo | -73.9987505 | 40.7228801 | attraction | 
 | South Street Seaport | -74.0028376 | 40.7057753 | attraction | 
 | Spyscape | -73.9838591 | 40.7650645 | attraction | 
 | Statue of Liberty | -73.9851473 | 40.7219912 | attraction | 
 | Stonewall Inn | -74.0021484 | 40.7338008 | attraction | 
 | Textile building | -74.0056679 | 40.7174627 | attraction | 
 | The High Line | -74.0034424 | 40.753277 | attraction | 
 | The High Line North Entrance | -74.0033107 | 40.7561135 | attraction | 
 | The Ride | -73.9911128 | 40.7549545 | attraction | 
 | Times Square | -73.9856026 | 40.7579511 | attraction | 
 | Tortoise | -73.9727565 | 40.7679979 | attraction | 
 | TriBeCa | -74.0061043 | 40.7223526 | attraction | 
 | Tropical Zone | -73.9725255 | 40.7676312 | attraction | 
 | Umpire rock | -73.9777798 | 40.7693619 | attraction | 


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
| GetZipCodeLow.py | Created to get zipcodes from lat and long so to remove non NYC apartments from the NYC RentHop dataset using a list of valid Zip Codes / partitioned by interest level due to larger base recordset causing session timeout with Nominatim |
| GetZipCodeMedium.py | Created to get zipcodes from lat and long so to remove non NYC apartments from the NYC RentHop dataset using a list of valid Zip Codes / partitioned by interest level due to larger base recordset causing session timeout with Nominatim |
| GetZipCodeHigh.py | Created to get zipcodes from lat and long so to remove non NYC apartments from the NYC RentHop dataset using a list of valid Zip Codes / partitioned by interest level due to larger base recordset causing session timeout with Nominatim |

| Combine_RentHop_InterestFiles.py | Combines the resulting csv files from GetZipCodeHigh/Medium/Low.py files |
| RemoveNonNYCRecords.py | Removes Non NYC apartments from master analytics dataset |
| CalculateDistancesToNYCAttractions.py | Generates the geohash for these attractions using the Latitudes and Longitudes | 
| FinalDataWranglingEDA.py | Final Data Wrangling, strips html, punctuation and cleans up non NYC Zipcode related apartments. | 
| VariableCorrelationReview.py | Variable Correlation Analysis using the master analytics dataset | 
| RandomForest.py | Model review and testing. Features Analysis and parameter tuning. | 


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

## Data Sources
| RentHop | NYC Apartments Inventory | https://www.kaggle.com/c/two-sigma-connect-rental-listing-inquiries/data | 
| Yelp | Collection of NYC Business Ratings and Prices | https://www.yelp.com/dataset | 
| Fortune | NYC List of top 40 Employers | https://fortune.com/best-workplaces-new-york/2020/search/ | 
| Pluto | NYC Borough Location Area Information | https://www1.nyc.gov/ | 
| Mygeodata | NYC Location of Attractions | https://mygeodata.cloud/ | 
| Zip Codes | NYC Zip Codes | https://worldpostalcode.com/united-states/new-york/new-york-city | 

##References: 

Kopp, C. (November 2019). How Expensive is it to Live in New York City? Retrieved from: https://www.investopedia.com/articles/personal-finance/012315/how-expensive-new-york-city-really.asp

Riley, E. (July 2019). Cost of Living in Chicago vs. NYC: Which Big City Is Cheaper? Retrieved from: https://streeteasy.com/blog/cost-of-living-in-chicago-vs-nyc/#:~:text=Median%20rent%20for%20a%201,That's%20nothing%20to%20scoff%20at.

TIMOTHY102, (October 2020). Predicting NYC AirBnB Rental Prices with TensorFlow. Retrieved from  https://www.analyticsvidhya.com/blog/2020/10/predicting-nyc-airbnb-rental-prices-tensorflow/

Carmody, B. (February 2021). Best Rental Listing Sites. Retrieved from  https://www.investopedia.com/best-rental-listing-sites-5075293

RentCafe. (n.d.). RentCafe is a listing site that can be used for comparable pricing with my predicted values. Retrieved from https://www.rentcafe.com/

Mastroeni, T. (October 2020). How is Artificial Intelligence Used in Real Estate? Retrieved from https://www.fool.com/millionacres/real-estate-market/real-estate-innovation/how-is-artificial-intelligence-used-in-real-estate/

Barzilay, O. (March 2017). Property Management May Be The Next Frontier For AI. Retrieved from https://www.forbes.com/sites/omribarzilay/2017/03/14/property-management-may-be-the-next-frontier-for-ai/?sh=3ba8d5f66fb3

McLaughlin, K. (November 2019). Robots Are Taking Over (the Rental Screening Process). Retrieved from https://www.wsj.com/articles/robots-are-taking-over-the-rental-screening-process-11574332200

Devanesan, J. (October 2019). What happens when AI enters the rental market? Retrieved from https://techhq.com/2019/10/what-happens-when-ai-enters-the-rental-market/

Antony, V. (May 2020) Predicting Apartment Rental Prices in Germany. Retrieved from https://towardsdatascience.com/predicting-apartment-rental-prices-in-germany-d5635197ab00

Villar, B. (April 2020). Machine Learning and RealState: Predicting Rental Prices in Amsterdam. Retrieved from https://towardsdatascience.com/ai-and-real-state-renting-in-amsterdam-part-1-5fce18238dbc

Najera, C. Hunter, T. Zhan, D. Bialer, J. (March 2017). Predicting Interest for NYC Apartment Rental Listings - A Guideline For Landlors and Agents. Retrieved from https://nycdatascience.com/blog/student-works/predicting-interest-nyc-apartments-rent-guideline-landlords/



