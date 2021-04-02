
"""
Author: Alan Danque
Date:   20210323
Purpose:Modeling

"""
from pathlib import Path
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None  # default='warn'  # https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas

results_dir = Path('C:/Alan/DSC680/Project1Data/').joinpath('results')
results_dir.mkdir(parents=True, exist_ok=True)

filepath = "C:/Alan/DSC680/Project1Data/FinalLeadAnalyticsRecord.csv"  #MasterAnalyticsDataSet_FinalToAnalyze.csv"
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

#from sklearn.model_selection import train_test_split
#x_train, x_test, y_train, y_test=train_test_split(X,Y,test_size=0.2, shuffle=True, random_state=0)

## RANDOM FOREST - KFOLD AND MODEL
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
kf = KFold(n_splits=10 ,random_state=42 ,shuffle=True)
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

"""
Results:


['Unnamed: 0', 'bathrooms', 'bedrooms', 'latitude', 'longitude', 'elevator', 'cats_allowed', 'hardwood_floors', 'dogs_allowed', 'doorman', 'dishwasher', 'no_fee', 'laundry_in_building', 'fitness_center', 'pre-war', 'laundry_in_unit', 'roof_deck', 'outdoor_space', 'dining_room', 'high_speed_internet', 'balcony', 'swimming_pool', 'new_construction', 'terrace', 'exclusive', 'loft', 'garden_patio', 'wheelchair_access', 'common_outdoor_space', 'The Goldman Sachs Group, Inc. Distance', 'Adecco Group brands Distance', 'Live Nation Entertainment Distance', 'Zillow Distance', 'Blackstone Distance', 'Voya Financial Distance', 'Horizon Media Distance', 'Ernst & Young LLP Distance', 'Protiviti Distance', 'Accenture Distance', 'PricewaterhouseCoopers LLP Distance', 'Dechert LLP Distance', 'Mastercard Incorporated Distance', 'KPMG LLP Distance', 'Baker Tilly Virchow Krause, LLP Distance', 'Comcast NBCUniversal Distance', 'Atlassian Distance', 'Citizens Bank Distance', 'Capital One Financial Corporation Distance', 'Deloitte Distance', 'Adobe Distance', 'Cumberland Farms, Inc. Distance', 'Alston & Bird LLP Distance', 'DHL Express U.S. Distance', 'Workiva Inc. Distance', 'Dropbox Distance', 'Cooley LLP Distance', 'Bain & Company Distance', 'American Express Distance', 'Orrick Distance', 'Shawmut Design and Construction Distance', 'Noom, Inc. Distance', 'The Cheesecake Factory Incorporated Distance', 'Concord Hospitality Enterprises Company Distance', 'Box, Inc. Distance', 'West Monroe Partners Distance', 'Wegmans Food Markets, Inc. Distance', 'Power Home Remodeling Distance', 'Hulu Distance', 'Salesforce Distance', 'Yelp_Highest_Priced_0', 'Yelp_Highest_Priced_1', 'Yelp_Highest_Priced_2', 'Yelp_Highest_Rated_0', 'Yelp_Highest_Rated_1', 'Yelp_Highest_Rated_2', 'zipcode', '1 World Trade Center Distance', '80 South Street Distance', 'Access High Line Park Distance', 'American Icon Distance', 'Anton Kern Gallery Distance', 'Archibalds Townhouse Distance', 'Arguably the best location to see evening Manhattan Henge Distance', 'BAC Distance', 'Barthmans Sidewalk Clock Distance', 'big gay ice cream Distance', 'Bloody Angle Distance', 'Bryant Park Distance', 'California Sea Lion Distance', 'Canal Street Distance', 'Canal street market Distance', 'Carrie Bradshaw House Distance', 'Casa di Carrie Distance', 'Chelsea Distance', 'Chelsea Flea Market Distance', 'Chelsea Market Distance', 'Chinatown Distance', 'Circle line ferrys Distance', 'Classic Car Club Manhattan Distance', 'Cocktail Kingdom Distance', 'Colonnade row Distance', 'Color Factory Distance', 'Cortlandt Alley Distance', 'Couv Led Zepp 5e album Distance', 'Curry hill Distance', 'Delacorte Musical Clock Distance', 'Diamond District Distance', 'Dream house Distance', 'Dr Nevilles I Am Legend townhouse Distance', 'Empire State Building Distance', 'Explore Chinatown Information Kiosk Distance', 'Flatiron District Distance', 'Food Truck Street Distance', 'Free Kayaking with the Downtown Boathouse Distance', 'Free Public Stargazing Distance', 'Friends Building Distance', 'Gapstow bridge Distance', 'Gentoo Penguin Distance', 'Glen span arch Distance', 'Greenwich Village Distance', 'Grey houndiin bus stop Distance', 'Grizzly Bear Distance', 'Grove Court Distance', 'Hangmans Elm Distance', 'High Line Access Distance', 'High Line Park Distance', 'Huddlestone arch Distance', 'Kayak Brooklyn Distance', 'La casa de los Tenenbaums Distance', 'La de forest house Distance', 'Le Petit Versailles Distance', 'LES SKATEPARK Distance', 'Liz Christy Garden Distance', 'Low Line Park Distance', 'Mad about you building Distance', 'Mahayanna Buddhist Center Distance', 'Maison sur les toits Distance', 'Mark Twain House Distance', 'Meatpacking District Distance', 'NBC Studios Distance', 'Nicholas Roerich Museum Distance', 'Nicola Tesla corner Distance', 'NY Skyride Distance', 'Original brown stone houses Distance', 'paparazzi dogman and paparazzi rabbitgirl Distance', 'Paul Nicklen Gallery Distance', 'Point de vue 17e rue Distance', 'Puffin Distance', 'Red Panda Distance', 'Rockefeller Center Distance', 'Rowboat rentals Distance', 'Salmagundi club Distance', 'Schwartz Luggage Storage Distance', 'Seal Distance', 'Sea Lions Distance', 'Sightseeing Pass, LLC Distance', 'Site of the Beach Pneumatic Subway Distance', 'Snow Leopard Distance', 'Snow Monkey Distance', 'SoHo Distance', 'South Street Seaport Distance', 'Spyscape Distance', 'Statue of Liberty Distance', 'Stonewall Inn Distance', 'Textile building Distance', 'The High Line Distance', 'The High Line North Entrance Distance', 'The Ride Distance', 'Times Square Distance', 'Tortoise Distance', 'TriBeCa Distance', 'Tropical Zone Distance', 'Umpire rock Distance', 'description_length', 'borough_id', 'borough_val', 'interest_level_val', 'SynthesizedVar1']
[[0.0000e+00 1.0000e+00 0.0000e+00 ... 2.0000e+00 2.0000e+00 1.8530e+03]
 [1.0000e+00 1.0000e+00 2.0000e+00 ... 2.0000e+00 2.0000e+00 2.8580e+03]
 [2.0000e+00 1.0000e+00 1.0000e+00 ... 2.0000e+00 2.0000e+00 2.6050e+03]
 ...
 [3.3983e+04 1.0000e+00 0.0000e+00 ... 2.0000e+00 1.0000e+00 2.0030e+03]
 [3.3984e+04 1.0000e+00 1.0000e+00 ... 2.0000e+00 1.0000e+00 4.5050e+03]
 [3.3985e+04 1.0000e+00 2.0000e+00 ... 2.0000e+00 1.0000e+00 3.2070e+03]]
Mean Absolute Error: 1.75
Accuracy: 99.39 %.
Mean Absolute Error: 1.17
Accuracy: 99.98 %.
Mean Absolute Error: 1080.03
Accuracy: 99.94 %.
Mean Absolute Error: 2.12
Accuracy: 99.93 %.
Mean Absolute Error: 32.18
Accuracy: 99.95 %.
Mean Absolute Error: 3.31
Accuracy: 99.97 %.
Mean Absolute Error: 1.15
Accuracy: 99.97 %.
Mean Absolute Error: 2.5
Accuracy: 99.98 %.
Mean Absolute Error: 45.5
Accuracy: 99.97 %.
Mean Absolute Error: 62.63
Accuracy: 99.97 %.
Average accuracy: 99.90524288712473

Process finished with exit code 0


2nd Run 20210331

Mean Absolute Error: 1.75
Accuracy: 99.39 %.
Mean Absolute Error: 1.17
Accuracy: 99.98 %.
Mean Absolute Error: 1080.03
Accuracy: 99.94 %.
Mean Absolute Error: 2.12
Accuracy: 99.93 %.
Mean Absolute Error: 32.18
Accuracy: 99.95 %.
Mean Absolute Error: 3.31
Accuracy: 99.97 %.
Mean Absolute Error: 1.15
Accuracy: 99.97 %.
Mean Absolute Error: 2.5
Accuracy: 99.98 %.
Mean Absolute Error: 45.5
Accuracy: 99.97 %.
Mean Absolute Error: 62.63
Accuracy: 99.97 %.
Average accuracy: 99.90524288712473


# hyperparameter tuning


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
pprint(random_grid)


# RandomizedsearchCV

# Use the random grid to search for best hyperparameters
# First create the base model to tune
rf = RandomForestRegressor()
# Random search of parameters, using 3 fold cross validation,
# search across 100 different combinations, and use all available cores
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid, n_iter = 100, cv = 3, verbose=2, random_state=42, n_jobs = -1)
# Fit the random search model
rf_random.fit(data_train, target_train)

print(rf_random.best_params_)

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




# Decision Tree

## SAVING THE DECISION TREE

from sklearn.tree import export_graphviz
import pydot
tree = rf.estimators_[5]
export_graphviz(tree, out_file = 'tree.dot', feature_names = feature_list, rounded = True, precision = 1)
(graph, ) = pydot.graph_from_dot_file('tree.dot')
graph.write_png('tree.png')


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

col = []
for i in feature_list:
    col.append(i)
labels = []
for i in list_of_index:
    b = col[i]
    labels.append(b)

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

##### prediction

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