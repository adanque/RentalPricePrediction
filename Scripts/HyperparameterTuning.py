

"""
Author: Alan Danque
Date:   20210323
Purpose:Model Training, Testing and prediction
Variables:
['Unnamed: 0', 'bathrooms', 'bedrooms', 'latitude', 'longitude', 'elevator', 'cats_allowed', 'hardwood_floors', 'dogs_allowed', 'doorman', 'dishwasher', 'no_fee', 'laundry_in_building', 'fitness_center', 'pre-war', 'laundry_in_unit', 'roof_deck', 'outdoor_space', 'dining_room', 'high_speed_internet', 'balcony', 'swimming_pool', 'new_construction', 'terrace', 'exclusive', 'loft', 'garden_patio', 'wheelchair_access', 'common_outdoor_space', 'The Goldman Sachs Group, Inc. Distance', 'Adecco Group brands Distance', 'Live Nation Entertainment Distance', 'Zillow Distance', 'Blackstone Distance', 'Voya Financial Distance', 'Horizon Media Distance', 'Ernst & Young LLP Distance', 'Protiviti Distance', 'Accenture Distance', 'PricewaterhouseCoopers LLP Distance', 'Dechert LLP Distance', 'Mastercard Incorporated Distance', 'KPMG LLP Distance', 'Baker Tilly Virchow Krause, LLP Distance', 'Comcast NBCUniversal Distance', 'Atlassian Distance', 'Citizens Bank Distance', 'Capital One Financial Corporation Distance', 'Deloitte Distance', 'Adobe Distance', 'Cumberland Farms, Inc. Distance', 'Alston & Bird LLP Distance', 'DHL Express U.S. Distance', 'Workiva Inc. Distance', 'Dropbox Distance', 'Cooley LLP Distance', 'Bain & Company Distance', 'American Express Distance', 'Orrick Distance', 'Shawmut Design and Construction Distance', 'Noom, Inc. Distance', 'The Cheesecake Factory Incorporated Distance', 'Concord Hospitality Enterprises Company Distance', 'Box, Inc. Distance', 'West Monroe Partners Distance', 'Wegmans Food Markets, Inc. Distance', 'Power Home Remodeling Distance', 'Hulu Distance', 'Salesforce Distance', 'Yelp_Highest_Priced_0', 'Yelp_Highest_Priced_1', 'Yelp_Highest_Priced_2', 'Yelp_Highest_Rated_0', 'Yelp_Highest_Rated_1', 'YelpHighRated3', 'zipcode', '1 World Trade Center Distance', '80 South Street Distance', 'Access High Line Park Distance', 'American Icon Distance', 'Anton Kern Gallery Distance', 'Archibalds Townhouse Distance', 'Arguably the best location to see evening Manhattan Henge Distance', 'BAC Distance', 'Barthmans Sidewalk Clock Distance', 'big gay ice cream Distance', 'Bloody Angle Distance', 'BryantPark_Dist', 'California Sea Lion Distance', 'Canal Street Distance', 'Canal street market Distance', 'Carrie Bradshaw House Distance', 'Casa di Carrie Distance', 'Chelsea Distance', 'Chelsea Flea Market Distance', 'Chelsea Market Distance', 'Chinatown Distance', 'Circle line ferrys Distance', 'Classic Car Club Manhattan Distance', 'Cocktail Kingdom Distance', 'Colonnade row Distance', 'Color Factory Distance', 'Cortlandt Alley Distance', 'Couv Led Zepp 5e album Distance', 'Curry hill Distance', 'Delacorte Musical Clock Distance', 'Diamond District Distance', 'Dream house Distance', 'Dr Nevilles I Am Legend townhouse Distance', 'Empire State Building Distance', 'Explore Chinatown Information Kiosk Distance', 'Flatiron District Distance', 'Food Truck Street Distance', 'Free Kayaking with the Downtown Boathouse Distance', 'Free Public Stargazing Distance', 'Friends Building Distance', 'Gapstow bridge Distance', 'Gentoo Penguin Distance', 'GlenSpanArch_Dist', 'Greenwich Village Distance', 'Grey houndiin bus stop Distance', 'Grizzly Bear Distance', 'Grove Court Distance', 'Hangmans Elm Distance', 'High Line Access Distance', 'High Line Park Distance', 'HuddlestoneArch_Dist', 'Kayak Brooklyn Distance', 'LaCasaDeLosT_Dist', 'La de forest house Distance', 'Le Petit Versailles Distance', 'LES SKATEPARK Distance', 'Liz Christy Garden Distance', 'Low Line Park Distance', 'Mad about you building Distance', 'Mahayanna Buddhist Center Distance', 'Maison sur les toits Distance', 'Mark Twain House Distance', 'Meatpacking District Distance', 'NBC Studios Distance', 'NicholasMuseum_Dist', 'Nicola Tesla corner Distance', 'NY Skyride Distance', 'OrigBrownStoneH_Dist', 'paparazzi dogman and paparazzi rabbitgirl Distance', 'Paul Nicklen Gallery Distance', 'Point de vue 17e rue Distance', 'Puffin Distance', 'Red Panda Distance', 'Rockefeller Center Distance', 'Rowboat rentals Distance', 'Salmagundi club Distance', 'Schwartz Luggage Storage Distance', 'Seal Distance', 'Sea Lions Distance', 'Sightseeing Pass, LLC Distance', 'Site of the Beach Pneumatic Subway Distance', 'Snow Leopard Distance', 'Snow Monkey Distance', 'SoHo Distance', 'South Street Seaport Distance', 'Spyscape Distance', 'Statue of Liberty Distance', 'Stonewall Inn Distance', 'Textile building Distance', 'The High Line Distance', 'The High Line North Entrance Distance', 'The Ride Distance', 'Times Square Distance', 'Tortoise Distance', 'TriBeCa Distance', 'Tropical Zone Distance', 'Umpire rock Distance', 'description_length', 'borough_id', 'borough_val', 'interest_level_val', 'SynthesizedVar1', 'SynthesizedVar4', 'SynthesizedVar2', 'SynthesizedVar3', 'SynthesizedVar5']

"""
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

filepath = "C:/Alan/DSC680/Project1Data/FinalLeadAnalyticsRecord2.csv"  #MasterAnalyticsDataSet_FinalToAnalyze.csv"
data = pd.read_csv(filepath)
amsmodel1 = data
del amsmodel1['street_address']
amsmodel1.fillna(0, inplace=True)
#amsmodel1.replace(np.nan,0)


target = np.array(amsmodel1['price'])
features = amsmodel1.drop('price', axis = 1)
feature_list = list(features.columns)
features = np.array(features)
print(feature_list)
print(features)
print("Dataframe Loaded: --- %s seconds  ---" % (time.time() - start_time))


## RANDOM FOREST - KFOLD AND MODEL
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
#kf = KFold(n_splits=10 ,random_state=42 ,shuffle=True)
kf = KFold(n_splits=5 ,random_state=42 ,shuffle=True)

accuracies = []
for train_index, test_index in kf.split(features):
    data_train = features[train_index]
    target_train = target[train_index]
    data_test = features[test_index]
    target_test = target[test_index]
    rf = RandomForestRegressor(n_estimators = 1000,
                               random_state = 42,
                               criterion = 'mse',
                               bootstrap=True)
    rf.fit(data_train, target_train)
    predictions = rf.predict(data_test)
    errors = abs(predictions - target_test)
    print('Mean Absolute Error:', round(np.mean(errors), 2))
    mape = 100 * (errors / target_test)
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')
    accuracies.append(accuracy)

average_accuracy = np.mean(accuracies)
print('Average accuracy:', average_accuracy)


# save model
model_file = results_dir.joinpath('My1stModel.pkl')
with open(model_file,'wb') as f:
    pickle.dump(rf,f)


#model_file = results_dir.joinpath('MyModel.pkl')
#with open(model_file, 'rb') as f:
#    rf = pickle.load(f)


print("1st KFold RandomForestRegressor: --- %s seconds  ---" % (time.time() - start_time))
"""
1st KFold RandomForestRegressor: --- 7063.219024181366 seconds  ---
{'n_estimators': [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000], 'max_features': ['auto', 'sqrt'], 'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, None], 'min_samples_split': [2, 5, 10], 'min_samples_leaf': [1, 2, 4], 'bootstrap': [True, False]}

"""

from sklearn.model_selection import RandomizedSearchCV
# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(10, 110, num = 11)]
max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 4]
# Method of selecting samples for training each tree
bootstrap = [True, False]
# Create the random grid
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap}
print(random_grid)
print("HyperParamater Tuning: --- %s seconds  ---" % (time.time() - start_time))

"""
HyperParamater Tuning: --- 7063.219599485397 seconds  ---
Fitting 3 folds for each of 100 candidates, totalling 300 fits
[CV] END bootstrap=True, max_depth=30, max_features=sqrt, min_samples_leaf=1, min_samples_split=5, n_estimators=400; total time= 1.1min
[CV] END bootstrap=True, max_depth=30, max_features=sqrt, min_samples_leaf=1, min_samples_split=5, n_estimators=400; total time= 1.1min

"""
# RandomizedsearchCV

# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestRegressor()
# Random search of parameters, using 3 fold cross validation,
# search across 100 different combinations, and use all available cores
# rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)

rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 10, cv = 3, verbose=2, random_state=42, n_jobs = -1)
# Fit the random search model
rf_random.fit(data_train, target_train)

# save model
model_file = results_dir.joinpath('My2ndModel.pkl')
with open(model_file,'wb') as f:
    pickle.dump(rf,f)


print(rf_random.best_params_)
print("RandomizedsearchCV: --- %s seconds  ---" % (time.time() - start_time))


"""
[CV] END bootstrap=False, max_depth=50, max_features=auto, min_samples_leaf=2, min_samples_split=2, n_estimators=2000; total time=49.0min
[CV] END bootstrap=False, max_depth=50, max_features=auto, min_samples_leaf=2, min_samples_split=2, n_estimators=2000; total time=50.7min
{'n_estimators': 1000, 'min_samples_split': 10, 'min_samples_leaf': 1, 'max_features': 'auto', 'max_depth': 80, 'bootstrap': False}
RandomizedsearchCV: --- 7901.3268892765045 seconds  ---
Mean Absolute Error: 564.65
Accuracy: 84.0 %.
Mean Absolute Error: 598.04
Accuracy: 85.71 %.
Mean Absolute Error: 2137.4
Accuracy: 88.76 %.
Mean Absolute Error: 585.32
Accuracy: 85.6 %.
Mean Absolute Error: 731.0
Accuracy: 82.88 %.
Mean Absolute Error: 711.69
Accuracy: 84.75 %.
Mean Absolute Error: 577.75
Accuracy: 85.84 %.
Mean Absolute Error: 671.26
Accuracy: 85.55 %.
Mean Absolute Error: 776.9
Accuracy: 89.12 %.
Mean Absolute Error: 887.94
Accuracy: 86.91 %.
Average accuracy: 85.91347605256752
2nd KFold RandomForestRegressor: --- 8356.327275276184 seconds  ---

"""

# Back to RandomForest

## RANDOM FOREST - KFOLD AND MODEL

from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
kf = KFold(n_splits=10, random_state=42, shuffle=True)
accuracies = []
for train_index, test_index in kf.split(features):
    data_train = features[train_index]
    target_train = target[train_index]

    data_test = features[test_index]
    target_test = target[test_index]

    rf = RandomForestRegressor(n_estimators=400,
                               random_state=42,
                               criterion='mse',
                               min_samples_leaf=1,
                               min_samples_split=2,
                               max_features='sqrt',
                               bootstrap=False,
                               max_depth=None)

    rf.fit(data_train, target_train)

    predictions = rf.predict(data_test)

    errors = abs(predictions - target_test)

    print('Mean Absolute Error:', round(np.mean(errors), 2))

    mape = 100 * (errors / target_test)
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')

    accuracies.append(accuracy)

average_accuracy = np.mean(accuracies)
print('Average accuracy:', average_accuracy)

model_file = results_dir.joinpath('My3rdModel.pkl')
with open(model_file,'wb') as f:
    pickle.dump(rf,f)


print("2nd KFold RandomForestRegressor: --- %s seconds  ---" % (time.time() - start_time))



# Decision Tree

## SAVING THE DECISION TREE

from sklearn.tree import export_graphviz
import pydot
tree = rf.estimators_[5]
tree_dot_file = results_dir.joinpath('tree.dot')
tree_png_file = results_dir.joinpath('tree.png')
export_graphviz(tree, out_file = tree_dot_file, feature_names = feature_list, rounded = True, precision = 1)
(graph, ) = pydot.graph_from_dot_file(tree_dot_file)
graph.write_png(tree_png_file)
print("DecisionTree: --- %s seconds  ---" % (time.time() - start_time))


# Feature Importance

y = rf.feature_importances_
list_y = [a for a in y if a > 0.005]
print(list_y)

list_of_index = []
for i in list_y:
    a = np.where(y==i)
    list_of_index.append(a)
print(list_of_index)

list_of_index = [0,1,2,3,4,24,97,249,280,308]

# Get the column lables
print("Feature Importance: --- %s seconds  ---" % (time.time() - start_time))

col = []
for i in feature_list:
    col.append(i)
labels = []
for i in list_of_index:
    b = col[i]
    labels.append(b)

print(labels)


# Feature Importance Plot
import matplotlib.pyplot as plt
y = list_y
fig, ax = plt.subplots()
width = 0.8
ind = np.arange(len(y))
ax.barh(ind, y,width, color="pink")
ax.set_yticks(ind+width/10)
ax.set_yticklabels(labels, minor=False)
plt.title('Feature importance in Random Forest Regression')
plt.xlabel('Relative importance')
plt.ylabel('feature')
plt.figure(figsize=(10,8.5))
fig.set_size_inches(10, 8.5, forward=True)
img_file = results_dir.joinpath('Feature_importance_in_Random_Forest_Regression.png')
plt.savefig(img_file)
plt.show()

print("Complete: --- %s seconds  ---" % (time.time() - start_time))

##### prediction

"""
# create a new dataframe that is indexed like the trained model
newdata = pd.DataFrame().reindex_like(amsmodel1)
newdata.fillna(value=0, inplace=True)

# delete the variable to be predicted
del newdata['house_price']
newdata = newdata.iloc[[1]]

# insert information about your apartment
newdata['bedrooms'] = 1
newdata['surface'] = 45
newdata['yelp_prices'] = 2.234043
newdata['yelp_ratings'] = 4.113475

# only change the number values in the postcode
# and string values after the _ for the rental agency
newdata["['p']_1018"]= 1
newdata["['ag']_JLG Real Estate"] = 1

rf.predict(newdata)
"""



"""
# load model and predict
model_file = results_dir.joinpath('My2ndModel.pkl')
with open(model_file, 'rb') as f:
    rf = pickle.load(f)
rf.predict(X[0:1])
"""