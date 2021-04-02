"""
Author: Alan Danque
Date:   20210323
Purpose:Final Data Wrangling, strips html and punctuation.

"""
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None  # default='warn'  # https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas

results_dir = Path('C:/Alan/DSC680/Project1Data/').joinpath('results')
results_dir.mkdir(parents=True, exist_ok=True)

filepath = "C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_FinalToAnalyze.csv"
data = pd.read_csv(filepath)
#data = data[['price','bathrooms','bedrooms','latitude','longitude','elevator','cats_allowed','hardwood_floors','dogs_allowed','doorman','dishwasher','no_fee','laundry_in_building','fitness_center','pre-war','laundry_in_unit','roof_deck','outdoor_space','dining_room','high_speed_internet','balcony','swimming_pool','new_construction','terrace','exclusive','loft','garden_patio','wheelchair_access','common_outdoor_space','The Goldman Sachs Group, Inc. Distance','Adecco Group brands Distance','Live Nation Entertainment Distance','Zillow Distance','Blackstone Distance','Voya Financial Distance','Horizon Media Distance','Ernst & Young LLP Distance','Protiviti Distance','Accenture Distance','PricewaterhouseCoopers LLP Distance','Dechert LLP Distance','Mastercard Incorporated Distance','KPMG LLP Distance','Baker Tilly Virchow Krause, LLP Distance','Comcast NBCUniversal Distance','Atlassian Distance','Citizens Bank Distance','Capital One Financial Corporation Distance','Deloitte Distance','Adobe Distance','Cumberland Farms, Inc. Distance','Alston & Bird LLP Distance','DHL Express U.S. Distance','Workiva Inc. Distance','Dropbox Distance','Cooley LLP Distance','Bain & Company Distance','American Express Distance','Orrick Distance','Shawmut Design and Construction Distance','Noom, Inc. Distance','The Cheesecake Factory Incorporated Distance','Concord Hospitality Enterprises Company Distance','Box, Inc. Distance','West Monroe Partners Distance','Wegmans Food Markets, Inc. Distance','Power Home Remodeling Distance','Hulu Distance','Salesforce Distance','Yelp_Highest_Priced_0','Yelp_Highest_Priced_1','Yelp_Highest_Priced_2','Yelp_Highest_Rated_0','Yelp_Highest_Rated_1','Yelp_Highest_Rated_2','zipcode','1 World Trade Center Distance','80 South Street Distance','Access High Line Park Distance','American Icon Distance','Anton Kern Gallery Distance','Archibalds Townhouse Distance','Arguably the best location to see evening Manhattan Henge Distance','BAC Distance','Barthmans Sidewalk Clock Distance','big gay ice cream Distance','Bloody Angle Distance','Bryant Park Distance','California Sea Lion Distance','Canal Street Distance','Canal street market Distance','Carrie Bradshaw House Distance','Casa di Carrie Distance','Chelsea Distance','Chelsea Flea Market Distance','Chelsea Market Distance','Chinatown Distance','Circle line ferrys Distance','Classic Car Club Manhattan Distance','Cocktail Kingdom Distance','Colonnade row Distance','Color Factory Distance','Cortlandt Alley Distance','Couv Led Zepp 5e album Distance','Curry hill Distance','Delacorte Musical Clock Distance','Diamond District Distance','Dream house Distance','Dr Nevilles I Am Legend townhouse Distance','Empire State Building Distance','Explore Chinatown Information Kiosk Distance','Flatiron District Distance','Food Truck Street Distance','Free Kayaking with the Downtown Boathouse Distance','Free Public Stargazing Distance','Friends Building Distance','Gapstow bridge Distance','Gentoo Penguin Distance','Glen span arch Distance','Greenwich Village Distance','Grey houndiin bus stop Distance','Grizzly Bear Distance','Grove Court Distance','Hangmans Elm Distance','High Line Access Distance','High Line Park Distance','Huddlestone arch Distance','Kayak Brooklyn Distance','La casa de los Tenenbaums Distance','La de forest house Distance','Le Petit Versailles Distance','LES SKATEPARK Distance','Liz Christy Garden Distance','Low Line Park Distance','Mad about you building Distance','Mahayanna Buddhist Center Distance','Maison sur les toits Distance','Mark Twain House Distance','Meatpacking District Distance','NBC Studios Distance','Nicholas Roerich Museum Distance','Nicola Tesla corner Distance','NY Skyride Distance','Original brown stone houses Distance','paparazzi dogman and paparazzi rabbitgirl Distance','Paul Nicklen Gallery Distance','Point de vue 17e rue Distance','Puffin Distance','Red Panda Distance','Rockefeller Center Distance','Rowboat rentals Distance','Salmagundi club Distance','Schwartz Luggage Storage Distance','Seal Distance','Sea Lions Distance','Sightseeing Pass, LLC Distance','Site of the Beach Pneumatic Subway Distance','Snow Leopard Distance','Snow Monkey Distance','SoHo Distance','South Street Seaport Distance','Spyscape Distance','Statue of Liberty Distance','Stonewall Inn Distance','Textile building Distance','The High Line Distance','The High Line North Entrance Distance','The Ride Distance','Times Square Distance','Tortoise Distance','TriBeCa Distance','Tropical Zone Distance','Umpire rock Distance','description_length','borough_id','borough_val','interest_level_val']]

"""
plt.figure(figsize=(10,10))
df1 = data[['price','bathrooms','bedrooms','latitude','longitude','elevator','cats_allowed','hardwood_floors','dogs_allowed','doorman','dishwasher','no_fee','laundry_in_building','fitness_center','pre-war','laundry_in_unit','roof_deck','outdoor_space','dining_room','high_speed_internet']]
print(df1.columns)
corr = df1.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Review 1')
img_file = results_dir.joinpath('Variable_Relationship_Review_1.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review_1.csv')
corr.to_csv(img_file)


plt.figure(figsize=(10,10))
df2 = data[['price','balcony','swimming_pool','new_construction','terrace','exclusive','loft','garden_patio','wheelchair_access','common_outdoor_space','The Goldman Sachs Group, Inc. Distance',	'Adecco Group brands Distance',	'Live Nation Entertainment Distance',	'Zillow Distance',	'Blackstone Distance',	'Voya Financial Distance',	'Horizon Media Distance',	'Ernst & Young LLP Distance',	'Protiviti Distance',	'Accenture Distance']]
df2.rename(columns={'The Goldman Sachs Group, Inc. Distance': 'GoldSachs_Dist','Adecco Group brands Distance':'AdeccoGroup_Dist','Live Nation Entertainment Distance':'LiveNation_Dist', 'Zillow Distance':'Zillow_Dist',	'Blackstone Distance':'BlackStone_Dist','Voya Financial Distance':'VoyaFinancial_Dist',	'Horizon Media Distance':'HorizonMedia_Dist','Ernst & Young LLP Distance':'ErnstYoung_Dist','Protiviti Distance':'Protiviti_Dist',	'Accenture Distance':'Accenture_Dist'}, inplace=True)
print(df2.columns)
corr = df2.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Review 2')
img_file = results_dir.joinpath('Variable_Relationship_Review_2.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review_2.csv')
corr.to_csv(img_file)


plt.figure(figsize=(10,10))
df3 = data[['price','PricewaterhouseCoopers LLP Distance',	'Dechert LLP Distance',	'Mastercard Incorporated Distance',	'KPMG LLP Distance',	'Baker Tilly Virchow Krause, LLP Distance',	'Comcast NBCUniversal Distance',	'Atlassian Distance',	'Citizens Bank Distance',	'Capital One Financial Corporation Distance',	'Deloitte Distance',	'Adobe Distance',	'Cumberland Farms, Inc. Distance',	'Alston & Bird LLP Distance',	'DHL Express U.S. Distance',	'Workiva Inc. Distance',	'Dropbox Distance',	'Cooley LLP Distance',	'Bain & Company Distance',	'American Express Distance']]
df3.rename(columns={'PricewaterhouseCoopers LLP Distance':'PriceWaterHC_Dist','Dechert LLP Distance':'Dechert_Dist','Mastercard Incorporated Distance':'MasterCard_Dist','KPMG LLP Distance':'KPMG_Dist','Baker Tilly Virchow Krause, LLP Distance':'BakerTillyVK_Dist',	'Comcast NBCUniversal Distance':'ComcastNBC_Dist',	'Atlassian Distance':'Atlassian_Dist',	'Citizens Bank Distance':'CitzensBank_Dist','Capital One Financial Corporation Distance':'CapitalOne_Dist',	'Deloitte Distance':'Deloitte_Dist',	'Adobe Distance':'Adobe_Dist',	'Cumberland Farms, Inc. Distance':'CumberlandF_Dist',	'Alston & Bird LLP Distance':'AlstonBird_Dist',	'DHL Express U.S. Distance':'DHLExpress_Dist',	'Workiva Inc. Distance':'Workiva_Dist',	'Dropbox Distance':'DropBox_Dist',	'Cooley LLP Distance':'Cooley_Dist',	'Bain & Company Distance':'BainCo_Dist',	'American Express Distance':'AmericanExp_Dist'}, inplace=True)
print(df3.columns)
corr = df3.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Review 3')
img_file = results_dir.joinpath('Variable_Relationship_Review_3.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review_3.csv')
corr.to_csv(img_file)


plt.figure(figsize=(10,10))
df4 = data[['price','zipcode','Orrick Distance',	'Shawmut Design and Construction Distance',	'Noom, Inc. Distance',	'The Cheesecake Factory Incorporated Distance',	'Concord Hospitality Enterprises Company Distance',	'Box, Inc. Distance',	'West Monroe Partners Distance',	'Wegmans Food Markets, Inc. Distance',	'Power Home Remodeling Distance',	'Hulu Distance',	'Salesforce Distance',	'Yelp_Highest_Priced_0',	'Yelp_Highest_Priced_1',	'Yelp_Highest_Priced_2',	'Yelp_Highest_Rated_0',	'Yelp_Highest_Rated_1',	'Yelp_Highest_Rated_2',	'zipcode',	'1 World Trade Center Distance']]
df4.rename(columns={'Orrick Distance':'Orrick_Dist',	'Shawmut Design and Construction Distance':'ShawmutDesign_Dist',	'Noom, Inc. Distance':'Noom_Dist',	'The Cheesecake Factory Incorporated Distance':'CheesecakeFact_Dist',	'Concord Hospitality Enterprises Company Distance':'ConcordHospital_Dist',	'Box, Inc. Distance':'BoxInc_Dist',	'West Monroe Partners Distance':'WestMonroe_Dist',	'Wegmans Food Markets, Inc. Distance':'WegmansFoods_Dist',	'Power Home Remodeling Distance':'PowerHome_Dist',	'Hulu Distance':'Hulu_Dist',	'Salesforce Distance':'SalesForce_Dist',	'Yelp_Highest_Priced_0':'YelpHighPrice1',	'Yelp_Highest_Priced_1':'YelpHighPrice2',	'Yelp_Highest_Priced_2':'YelpHighPrice3',	'Yelp_Highest_Rated_0':'YelpHighRated1',	'Yelp_Highest_Rated_1':'YelpHighRated2',	'Yelp_Highest_Rated_2':'YelpHighRated3',		'1 World Trade Center Distance':'WorldTradeCntr_Dist'}, inplace=True)
print(df4.columns)
corr = df4.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Review 4')
img_file = results_dir.joinpath('Variable_Relationship_Review_4.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review_4.csv')
corr.to_csv(img_file)


plt.figure(figsize=(10,10))
df5 = data[['price','80 South Street Distance',	'Access High Line Park Distance',	'American Icon Distance',	'Anton Kern Gallery Distance',	'Archibalds Townhouse Distance',	'Arguably the best location to see evening Manhattan Henge Distance',	'BAC Distance',	'Barthmans Sidewalk Clock Distance',	'big gay ice cream Distance',	'Bloody Angle Distance',	'Bryant Park Distance',	'California Sea Lion Distance',	'Canal Street Distance',	'Canal street market Distance',	'Carrie Bradshaw House Distance',	'Casa di Carrie Distance',	'Chelsea Distance',	'Chelsea Flea Market Distance',	'Chelsea Market Distance']]
df5.rename(columns={'80 South Street Distance':'80SouthSt_Dist',	'Access High Line Park Distance':'AccessHLPark_Dist',	'American Icon Distance':'AmericanIcon_Dist',	'Anton Kern Gallery Distance':'AntonKernGallery_Dist',	'Archibalds Townhouse Distance':'ArchibaldsTown_dist',	'Arguably the best location to see evening Manhattan Henge Distance':'ArguablyBestLoc_dist',	'BAC Distance':'BAC_Dist',	'Barthmans Sidewalk Clock Distance':'BarthmansSidewalk_Dist',	'big gay ice cream Distance':'BGIceCream_Dist',	'Bloody Angle Distance':'BloodyAngle_Dist',	'Bryant Park Distance':'ByrantPark_Dist',	'California Sea Lion Distance':'CaliforniaSeaLion_Dist',	'Canal Street Distance':'CanalSt_Dist',	'Canal street market Distance':'CanalStMkt_Dist',	'Carrie Bradshaw House Distance':'CarrieBradshaw_Dist',	'Casa di Carrie Distance':'CasaDiCarrie_Dist',	'Chelsea Distance':'Chelsea_Dist',	'Chelsea Flea Market Distance':'ChelseaFleaMkt_Dist',	'Chelsea Market Distance':'ChelseaMkt_Dist'}, inplace=True)
print(df5.columns)
corr = df5.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Review 5')
img_file = results_dir.joinpath('Variable_Relationship_Review_5.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review_5.csv')
corr.to_csv(img_file)


plt.figure(figsize=(10,10))
df6 = data[['price','Chinatown Distance',	'Circle line ferrys Distance',	'Classic Car Club Manhattan Distance',	'Cocktail Kingdom Distance',	'Colonnade row Distance',	'Color Factory Distance',	'Cortlandt Alley Distance',	'Couv Led Zepp 5e album Distance',	'Curry hill Distance',	'Delacorte Musical Clock Distance',	'Diamond District Distance',	'Dream house Distance',	'Dr Nevilles I Am Legend townhouse Distance',	'Empire State Building Distance',	'Explore Chinatown Information Kiosk Distance',	'Flatiron District Distance',	'Food Truck Street Distance',	'Free Kayaking with the Downtown Boathouse Distance',	'Free Public Stargazing Distance']]
df6.rename(columns={'Chinatown Distance':'ChinaTown_Dist',	'Circle line ferrys Distance':'CircleLnFerry_Dist',	'Classic Car Club Manhattan Distance':'ClassicCarClub_Dist',	'Cocktail Kingdom Distance':'CocktailK_dist',	'Colonnade row Distance':'Colonnade_Dist',	'Color Factory Distance':'ColorFactory_Dist',	'Cortlandt Alley Distance':'CortlandtAlley_Dist',	'Couv Led Zepp 5e album Distance':'CoveLedZepp_Dist',	'Curry hill Distance':'CurryHill_Dist',	'Delacorte Musical Clock Distance':'DelacorteMusic_Dist',	'Diamond District Distance':'DiamondDistrict_Dist',	'Dream house Distance':'DreamHouse_Dist',	'Dr Nevilles I Am Legend townhouse Distance':'DrNevilles_Dist',	'Empire State Building Distance':'EmpireStateBldg_Dist',	'Explore Chinatown Information Kiosk Distance':'ExploreChinaTKiosk_Dist',	'Flatiron District Distance':'Flatiron_Dist',	'Food Truck Street Distance':'FoodTruckStreet_Dist',	'Free Kayaking with the Downtown Boathouse Distance':'FreeKayaking_Dist',	'Free Public Stargazing Distance':'FreePublicStarG_Dist'}, inplace=True)
print(df6.columns)
corr = df6.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Review 6')
img_file = results_dir.joinpath('Variable_Relationship_Review_6.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review_6.csv')
corr.to_csv(img_file)


plt.figure(figsize=(10,10))
df7 = data[['price','Friends Building Distance',	'Gapstow bridge Distance',	'Gentoo Penguin Distance',	'Glen span arch Distance',	'Greenwich Village Distance',	'Grey houndiin bus stop Distance',	'Grizzly Bear Distance',	'Grove Court Distance',	'Hangmans Elm Distance',	'High Line Access Distance',	'High Line Park Distance',	'Huddlestone arch Distance',	'Kayak Brooklyn Distance',	'La casa de los Tenenbaums Distance',	'La de forest house Distance',	'Le Petit Versailles Distance',	'LES SKATEPARK Distance',	'Liz Christy Garden Distance',	'Low Line Park Distance']]
df7.rename(columns={'Friends Building Distance':'FriendsBldg_Dist',	'Gapstow bridge Distance':'GapstowBridge_Dist',	'Gentoo Penguin Distance':'GentooPenguin_Dist',	'Glen span arch Distance':'GlenSpanArch_Dist',	'Greenwich Village Distance':'GreenwichVlg_Dist',	'Grey houndiin bus stop Distance':'GreyHoudiinBus_Dist',	'Grizzly Bear Distance':'GrizzlyBear_Dist',	'Grove Court Distance':'GroveCt_Dist',	'Hangmans Elm Distance':'HangmansElm_Dist',	'High Line Access Distance':'HighLineAcc_Dist',	'High Line Park Distance':'HighLinePk_Dist',	'Huddlestone arch Distance':'HuddlestoneArch_Dist',	'Kayak Brooklyn Distance':'KayakBrooklin_Dist',	'La casa de los Tenenbaums Distance':'LaCasaDeLosT_Dist',	'La de forest house Distance':'LaDeForestHouse_Dist',	'Le Petit Versailles Distance':'LePetitV_Dist',	'LES SKATEPARK Distance':'LesSkatePark_Dist',	'Liz Christy Garden Distance':'LizChristyGarden_Dist',	'Low Line Park Distance':'LowLinePark_Dist'}, inplace=True)
print(df7.columns)
corr = df7.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Review 7')
img_file = results_dir.joinpath('Variable_Relationship_Review_7.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review_7.csv')
corr.to_csv(img_file)


plt.figure(figsize=(10,10))
df8 = data[['price','Mad about you building Distance',	'Mahayanna Buddhist Center Distance',	'Maison sur les toits Distance',	'Mark Twain House Distance',	'Meatpacking District Distance',	'NBC Studios Distance',	'Nicholas Roerich Museum Distance',	'Nicola Tesla corner Distance',	'NY Skyride Distance',	'Original brown stone houses Distance',	'paparazzi dogman and paparazzi rabbitgirl Distance',	'Paul Nicklen Gallery Distance',	'Point de vue 17e rue Distance',	'Puffin Distance',	'Red Panda Distance',	'Rockefeller Center Distance',	'Rowboat rentals Distance',	'Salmagundi club Distance',	'Schwartz Luggage Storage Distance']]
df8.rename(columns={'Mad about you building Distance':'MadAboutYou_Dist',	'Mahayanna Buddhist Center Distance':'MahayannaBuddhist_dist',	'Maison sur les toits Distance':'MaisonSurLes_Dist',	'Mark Twain House Distance':'MarkTwainH_Dist',	'Meatpacking District Distance':'MeatPacking_Dist',	'NBC Studios Distance':'NBCStudios_Dist',	'Nicholas Roerich Museum Distance':'NicholasMuseum_Dist',	'Nicola Tesla corner Distance':'NicolaTesla_Dist',	'NY Skyride Distance':'NYSkyride_Dist',	'Original brown stone houses Distance':'OrigBrownStoneH_Dist',	'paparazzi dogman and paparazzi rabbitgirl Distance':'PaparazziDogman_Dist',	'Paul Nicklen Gallery Distance':'PaulNicklenG_Dist',	'Point de vue 17e rue Distance':'PointDeVue17_Dist',	'Puffin Distance':'Puffin_Dist',	'Red Panda Distance':'RedPanda_Dist',	'Rockefeller Center Distance':'RockefellerCtr_Dist',	'Rowboat rentals Distance':'RowboatRental_Dist',	'Salmagundi club Distance':'Salmagundi_Dist',	'Schwartz Luggage Storage Distance':'SchwartzLuggage_Dist'}, inplace=True)
print(df8.columns)
corr = df8.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Review 8')
img_file = results_dir.joinpath('Variable_Relationship_Review_8.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review_8.csv')
corr.to_csv(img_file)


plt.figure(figsize=(10,10))
df9 = data[['price','Seal Distance',	'Sea Lions Distance',	'Sightseeing Pass, LLC Distance',	'Site of the Beach Pneumatic Subway Distance',	'Snow Leopard Distance',	'Snow Monkey Distance',	'SoHo Distance',	'South Street Seaport Distance',	'Spyscape Distance',	'Statue of Liberty Distance',	'Stonewall Inn Distance',	'Textile building Distance',	'The High Line Distance',	'The High Line North Entrance Distance',	'The Ride Distance',	'Times Square Distance',	'Tortoise Distance',	'TriBeCa Distance',	'Tropical Zone Distance',	'Umpire rock Distance',	'description_length',	'borough_id',	'borough_val',	'interest_level_val']]
df9.rename(columns={'Seal Distance':'Seal_Dist',	'Sea Lions Distance':'SeaLions_Dist',	'Sightseeing Pass, LLC Distance':'SightSeeingPass_Dist',	'Site of the Beach Pneumatic Subway Distance':'BeachPneumaticSub_Dist',	'Snow Leopard Distance':'SnowLepard_Dist',	'Snow Monkey Distance':'SnowMonkey_Dist',	'SoHo Distance':'SoHo_Dist',	'South Street Seaport Distance':'SouthStSeaport_Dist',	'Spyscape Distance':'Spyscape_Dist',	'Statue of Liberty Distance':'StatueOfLiberty_Dist',	'Stonewall Inn Distance':'StonewallInn_Dist',	'Textile building Distance':'TextileBldg_Dist',	'The High Line Distance':'HighLine_Dist',	'The High Line North Entrance Distance':'HighLineN_Dist',	'The Ride Distance':'TheRide_Dist',	'Times Square Distance':'TimesSquare_Dist',	'Tortoise Distance':'Tortoise_Dist',	'TriBeCa Distance':'TriBeCa_Dist',	'Tropical Zone Distance':'TropicalZone_Dist',	'Umpire rock Distance':'UmpireRock_Dist'}, inplace=True)
print(df9.columns)
corr = df9.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Review 9')
img_file = results_dir.joinpath('Variable_Relationship_Review_9.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review_9.csv')
corr.to_csv(img_file)


plt.figure(figsize=(10,10))
df10 = data[['price','bathrooms','bedrooms','description_length','borough_id','interest_level_val','Nicholas Roerich Museum Distance','Original brown stone houses Distance','Glen span arch Distance','Huddlestone arch Distance','La casa de los Tenenbaums Distance','Yelp_Highest_Rated_2']]
df10.rename(columns={'Yelp_Highest_Rated_2':'YelpHighRated3','Nicholas Roerich Museum Distance':'NicholasMuseum_Dist','Original brown stone houses Distance':'OrigBrownStoneH_Dist','Glen span arch Distance':'GlenSpanArch_Dist','Huddlestone arch Distance':'HuddlestoneArch_Dist','La casa de los Tenenbaums Distance':'LaCasaDeLosT_Dist'}, inplace=True)
# Convert these fields to numeric
df10[['NicholasMuseum_Dist','OrigBrownStoneH_Dist','LaCasaDeLosT_Dist','YelpHighRated3','GlenSpanArch_Dist','HuddlestoneArch_Dist']] = df10[['NicholasMuseum_Dist','OrigBrownStoneH_Dist','LaCasaDeLosT_Dist','YelpHighRated3','GlenSpanArch_Dist','HuddlestoneArch_Dist']].apply(pd.to_numeric)

###df10['D1'] = df10['NicholasMuseum_Dist']+df10['OrigBrownStoneH_Dist']+df10['GlenSpanArch_Dist']+df10['HuddlestoneArch_Dist']+df10['LaCasaDeLosT_Dist']+df10['YelpHighRated3']
print(df10.columns)
corr = df10.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Final')
img_file = results_dir.joinpath('Variable_Relationship_Review_10.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review_10.csv')
corr.to_csv(img_file)
"""

#Optimize Here
plt.figure(figsize=(10,10))
# GOOD df11 = data[['price','bedrooms','bathrooms','doorman','fitness_center','laundry_in_unit','dishwasher','elevator','dining_room','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','garden_patio','hardwood_floors','new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space']]
#df11 = data[['price','bedrooms','bathrooms','doorman','fitness_center','laundry_in_unit','dishwasher','elevator','dining_room','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','garden_patio','hardwood_floors','new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space']]

##TEST df11 = data[['price','bedrooms','bathrooms','doorman','fitness_center','laundry_in_unit','dishwasher','elevator','dining_room','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','garden_patio','hardwood_floors','new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space','no_fee','outdoor_space','description_length','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','garden_patio','hardwood_floors','new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space','exclusive','laundry_in_building','loft','Nicholas Roerich Museum Distance','Original brown stone houses Distance','Glen span arch Distance','Huddlestone arch Distance','La casa de los Tenenbaums Distance','Yelp_Highest_Rated_2']]

# WORKS
# df11 = data[['price','bedrooms','bathrooms','doorman','fitness_center','laundry_in_unit','dishwasher','elevator','dining_room','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','garden_patio','hardwood_floors','new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space']]
df11 = data[['price','bedrooms','bathrooms','doorman','fitness_center','laundry_in_unit','dishwasher','elevator'
    ,'dining_room','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','garden_patio','hardwood_floors'
    ,'new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space'
    ,'no_fee','outdoor_space','Yelp_Highest_Rated_2','La casa de los Tenenbaums Distance','Huddlestone arch Distance'
    ,'Glen span arch Distance','Original brown stone houses Distance','Nicholas Roerich Museum Distance','Bryant Park Distance'
    ]]

# 'Nicholas Roerich Museum Distance'
# ,'Original brown stone houses Distance'
# ,'Glen span arch Distance'
# ,'Huddlestone arch Distance'
# ,'La casa de los Tenenbaums Distance'
# ,'Yelp_Highest_Rated_2'
#     ,'no_fee','outdoor_space','description_length','balcony'
#,'roof_deck','terrace','swimming_pool','high_speed_internet'
# 'no_fee','outdoor_space','description_length','balcony','roof_deck','terrace','swimming_pool','high_speed_internet'
# #,'garden_patio','hardwood_floors','new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space','exclusive','laundry_in_building','loft','Nicholas Roerich Museum Distance','Original brown stone houses Distance','Glen span arch Distance','Huddlestone arch Distance','La casa de los Tenenbaums Distance','Yelp_Highest_Rated_2'

# BAD 'description_length','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','balcony'
# WORK ON THIS LATER df11 = data[['price','bedrooms','bathrooms','doorman','fitness_center','laundry_in_unit','dishwasher','elevator','dining_room','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','garden_patio','hardwood_floors','new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space','no_fee','outdoor_space','description_length','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','garden_patio','hardwood_floors','new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space','exclusive','laundry_in_building','loft']] # ,'Nicholas Roerich Museum Distance','Original brown stone houses Distance','Glen span arch Distance','Huddlestone arch Distance','La casa de los Tenenbaums Distance','Yelp_Highest_Rated_2'

# WHY THIS FAILS df11 = data[['price','bedrooms','bathrooms','doorman','fitness_center','laundry_in_unit','dishwasher','elevator','dining_room','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','garden_patio','hardwood_floors','new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space','no_fee','outdoor_space','description_length','balcony','roof_deck','terrace','swimming_pool','high_speed_internet','garden_patio','hardwood_floors','new_construction','wheelchair_access','dogs_allowed','cats_allowed','common_outdoor_space','exclusive','laundry_in_building','loft','Nicholas Roerich Museum Distance','Original brown stone houses Distance','Glen span arch Distance','Huddlestone arch Distance','La casa de los Tenenbaums Distance','Yelp_Highest_Rated_2']]
#df11['SynthesizedVar1'] = df11['price']+df11['bedrooms']+df11['bathrooms']+df11['doorman']+df11['fitness_center']+df11['laundry_in_unit']+df11['dishwasher']+df11['elevator']+df11['dining_room']+df11['balcony']+df11['roof_deck']+df11['terrace']+df11['swimming_pool']+df11['high_speed_internet']+df11['garden_patio']+df11['hardwood_floors']+df11['new_construction']+df11['wheelchair_access']+df11['dogs_allowed']+df11['cats_allowed']+df11['common_outdoor_space']
df11['SynthesizedVar1'] = df11['bedrooms']+df11['bathrooms']+df11['doorman']+df11['fitness_center']+df11['laundry_in_unit']+df11['dishwasher']+df11['elevator']+df11['dining_room']+df11['balcony']+df11['roof_deck']+df11['terrace']+df11['swimming_pool']+df11['high_speed_internet']+df11['garden_patio']+df11['hardwood_floors']+df11['new_construction']+df11['wheelchair_access']+df11['dogs_allowed']+df11['cats_allowed']+df11['common_outdoor_space']

df11['SynthesizedVar4'] = (df11['bedrooms']*.50)+(df11['bathrooms']*.496)+(df11['doorman']*.259)+(df11['fitness_center']*.227)+(df11['laundry_in_unit']*.216)+(df11['dishwasher']*.209)+(df11['elevator']*.208)+(df11['dining_room']*.197)+(df11['balcony']*.127)+(df11['roof_deck']*.126)+(df11['terrace']*.116)+df11['swimming_pool']+(df11['high_speed_internet']*.09)+(df11['garden_patio']*.087)+(df11['hardwood_floors']*.076)+(df11['new_construction']*.073)+(df11['wheelchair_access']*.069)+(df11['dogs_allowed']*.067)+(df11['cats_allowed']*.06)+(df11['common_outdoor_space']*.03)

df11.rename(columns={'Bryant Park Distance':'BryantPark_Dist','Nicholas Roerich Museum Distance':'NicholasMuseum_Dist','Original brown stone houses Distance':'OrigBrownStoneH_Dist','Glen span arch Distance':'GlenSpanArch_Dist','Huddlestone arch Distance':'HuddlestoneArch_Dist','La casa de los Tenenbaums Distance':'LaCasaDeLosT_Dist','Yelp_Highest_Rated_2':'YelpHighRated3'}, inplace=True)
#df11['SynthesizedVar2'] = df11['NicholasMuseum_Dist']+df11['OrigBrownStoneH_Dist']+df11['LaCasaDeLosT_Dist']+df11['YelpHighRated3']+df11['GlenSpanArch_Dist']+df11['HuddlestoneArch_Dist']
df11['SynthesizedVar2'] = df11['YelpHighRated3']+df11['OrigBrownStoneH_Dist']+df11['OrigBrownStoneH_Dist']
df11['SynthesizedVar3'] = df11['NicholasMuseum_Dist']-df11['OrigBrownStoneH_Dist']-df11['LaCasaDeLosT_Dist']-df11['GlenSpanArch_Dist']-df11['HuddlestoneArch_Dist']

df11['SynthesizedVar5'] = df11['SynthesizedVar1']* df11['SynthesizedVar4']

print(df11.columns)
corr = df11.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.title('Variable Relationship Final')
img_file = results_dir.joinpath('Final_Variable_Relationship_Review.png')
plt.savefig(img_file)
plt.show()
img_file = results_dir.joinpath('Variable_Relationship_Review__Final.csv')
corr.to_csv(img_file)


#df10['D1'] = df10['NicholasMuseum_Dist']*df10['OrigBrownStoneH_Dist']*df10['GlenSpanArch_Dist']*df10['HuddlestoneArch_Dist']*df10['LaCasaDeLosT_Dist']*df10['YelpHighRated3']
# GOOOD df11['SynthesizedVar1'] = df11['price']+df11['bedrooms']+df11['bathrooms']+df11['doorman']+df11['fitness_center']+df11['laundry_in_unit']+df11['dishwasher']+df11['elevator']+df11['dining_room']+df11['balcony']+df11['roof_deck']+df11['terrace']+df11['swimming_pool']+df11['high_speed_internet']+df11['garden_patio']+df11['hardwood_floors']+df11['new_construction']+df11['wheelchair_access']+df11['dogs_allowed']+df11['cats_allowed']+df11['common_outdoor_space']

###df11.rename(columns={'Nicholas Roerich Museum Distance':'NicholasMuseum_Dist','Original brown stone houses Distance':'OrigBrownStoneH_Dist','Glen span arch Distance':'GlenSpanArch_Dist','Huddlestone arch Distance':'HuddlestoneArch_Dist','La casa de los Tenenbaums Distance':'LaCasaDeLosT_Dist','Yelp_Highest_Rated_2':'YelpHighRated3'}, inplace=True)
###df11['SynthesizedVar2'] = df11['NicholasMuseum_Dist']+df11['OrigBrownStoneH_Dist']+df11['LaCasaDeLosT_Dist']+df11['YelpHighRated3']+df11['GlenSpanArch_Dist']+df11['HuddlestoneArch_Dist']

"""                              
'NicholasMuseum_Dist'
'OrigBrownStoneH_Dist'
'LaCasaDeLosT_Dist'
'YelpHighRated3'
'GlenSpanArch_Dist'
'HuddlestoneArch_Dist'

'no_fee',
'outdoor_space',
'description_length',
'balcony',
'roof_deck',
'terrace',
'swimming_pool',
'high_speed_internet',
'garden_patio',
'hardwood_floors',
'new_construction',
'wheelchair_access',
'dogs_allowed',
'cats_allowed',
'common_outdoor_space',
'exclusive',
'laundry_in_building',
'loft'

"""


#Yelp Ratings vs. House Price
import matplotlib.pyplot as plt
plt.figure()
plt.scatter(df11['price'],df11['SynthesizedVar1'], s=20, edgecolor="black",c="darkorange", label = "Synthesized Predictor Variable")
plt.xlabel("Synthesized Predictor Variable")
plt.ylabel("Apartment Price")
plt.title("Apartment Price vs. Synthesized Predictor Variable")
plt.legend()
img_file = results_dir.joinpath('NYC_Price_Vs_SynthesizedPredictorVariable.png')
plt.savefig(img_file)
plt.show()


# Seaborn correlation matrix
#corr = data.corr(method='kendall')
#plt.figure(figsize=(8,8))
#sns.heatmap(corr, annot=True)
#plt.show()

# Reorder the columns

"""
df1 = data.iloc[:,0:1]
print(df1.columns)
df2 = data.iloc[:,1:20]
print(df2.columns)
df = pd.concat([df1, df2], ignore_index=True, sort=False)
print(type(df))
print(df.shape) # 49,352 obs and 15 vars
print(df.columns)
corr = df.corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.show()

"""


#corr = data.iloc[:,20:39].corr(method='kendall')
#sns.heatmap(corr, annot=True)
#plt.show()

"""
corr = data.iloc[:,:50].corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.show()

corr = data.iloc[:,50:].corr(method='kendall')
sns.heatmap(corr, annot=True)
plt.show()
"""


"""

X = amsmodel1.drop(['house_price','rental_agency','postcode','postcode2'], axis=1)
## correlation matrix
corrMatrix = X.corr()
## visualize it in a heatmap
sn.heatmap(corrMatrix, annot=True)
plt.title('NYC Highest Priced Yelp Businesses KMeans Cluster')
plt.legend()
img_file = results_dir.joinpath('NYC_VariableCorrelationsReview_1.png')
plt.savefig(img_file)
plt.show()


amsmodel1['surface_per_bedroom'] = amsmodel1['surface']/amsmodel1['bedrooms']


X = amsmodel1.drop(['house_price','rental_agency','postcode','postcode2'], axis=1)
## correlation matrix
corrMatrix = X.corr()
## visualize it in a heatmap
sn.heatmap(corrMatrix, annot=True)
plt.title('NYC Highest Priced Yelp Businesses KMeans Cluster')
plt.legend()
img_file = results_dir.joinpath('NYC_VariableCorrelationsReview_2.png')
plt.savefig(img_file)
plt.show()



#Yelp Ratings vs. House Price
import matplotlib.pyplot as plt
plt.figure()
plt.scatter(amsmodel1['yelp_ratings'],amsmodel1['house_price'], s=20, edgecolor="black",c="darkorange", label = "yelp")
plt.xlabel("Yelp Ratings")
plt.ylabel("House Price")
plt.title("Yelp Ratings vs. House Price")
plt.legend()
plt.show()

#Yelp Prices vs. House Price
import matplotlib.pyplot as plt
plt.figure()
plt.scatter(amsmodel1['yelp_prices'],amsmodel1['house_price'], s=20, edgecolor="black",c="darkorange", label="yelp")
plt.xlabel("Yelp Prices")
plt.ylabel("House Price")
plt.title("Yelp Prices vs. House Price")
plt.legend()
plt.show()

"""