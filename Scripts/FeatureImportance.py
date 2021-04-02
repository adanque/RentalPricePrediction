"""
Author: Alan Danque
Date:   20210323
Purpose:Feature Importance Review

"""
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

# load model
model_file = results_dir.joinpath('My3rdModel.pkl')
with open(model_file, 'rb') as f:
    rf = pickle.load(f)
print("Model Loaded: --- %s seconds  ---" % (time.time() - start_time))

target = np.array(amsmodel1['price'])
features = amsmodel1.drop('price', axis = 1)
feature_list = list(features.columns)
features = np.array(features)
print(feature_list)
print(features)
print("Features Loaded: --- %s seconds  ---" % (time.time() - start_time))


# Feature Importance
y = rf.feature_importances_
print("rf.feature_importances_")
print(type(y))
print(len(y))
print(y)

# Create an iterable tuple with aggregated elements in order
idf = zip(amsmodel1.columns, rf.feature_importances_)
print("idf")
print(type(idf))
print(idf)
# Convert zip object to list
zidf = list(idf)
print(type(zidf))
print(zidf)

# Convert list of tuples to dictionary
print("didf")
didf = dict(zidf)
print(type(didf))
print(didf)
import operator
print("Sorted the dictionary based on values to identify which features had the highest scrores")
sorted_didf = dict(sorted(didf.items(), key=operator.itemgetter(1),reverse=True))
print(sorted_didf)

# Convert dictionary to dataframe
print("pd_df")
pd_df = pd.DataFrame(didf, index=[0])
print(pd_df)


# Feature Importance Plot
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})
plt.tight_layout()
topfeatures_df = pd_df.max().nlargest(15)
plt.figure()
plt.title('Top 15 Rental Prediction Features')
#plt.hist(topfeatures_df, orientation='horizontal')
topfeatures_df.plot(kind='bar')
plt.ylabel('Score')
plt.xticks(rotation = 80)
img_file = results_dir.joinpath('Top_15_Rental_Prediction_Features.png')
plt.savefig(img_file)
plt.show()
