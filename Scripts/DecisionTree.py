"""
Author: Alan Danque
Date:   20210323
Purpose:Final Data Wrangling, strips html and punctuation.

"""
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
print("Estimators Loaded: --- %s seconds  ---" % (time.time() - start_time))
"""


# Decision Tree

## SAVING THE DECISION TREE
tree = rf.estimators_[5]
tree_dot_file = results_dir.joinpath('tree.dot')
tree_png_file = results_dir.joinpath('tree.png')
dotfile = open(tree_dot_file, 'w')
export_graphviz(tree, out_file = dotfile, feature_names = feature_list, rounded = True, precision = 1)

# Install https://graphviz.org/download/#windows
#(graph, ) = pydot.graph_from_dot_file(tree_dot_file)
#graph.write_png(tree_png_file)
# C:\Program Files\Graphviz\bin
# having issues with pydot.graph_from_dot_file. Since my dot file is getting created using subprocess.
##  from subprocess import check_call
##  check_call(['dot','-Tpng',dotfile,'-o',tree_png_file])

(graph,) = pydot.graph_from_dot_file(tree_dot_file)
graph.write_png(tree_png_file)

print("DecisionTree: --- %s seconds  ---" % (time.time() - start_time))
"""
PyDot Conversion Complete: --- 3804.3111951351166 seconds  ---
"""
