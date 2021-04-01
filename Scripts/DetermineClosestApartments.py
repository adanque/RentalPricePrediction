"""
Author: Alan Danque
Date:   20210323
Purpose:Creates clostest apartment location

"""
import pandas as pd
from scipy.spatial.distance import cdist
#https://stackoverflow.com/questions/38965720/find-closest-point-in-pandas-dataframes
import pygeohash
from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None  # default='warn'  # https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas


def closest_point(point, points):
    """ Find closest point from a list of points. """
    return points[cdist([point], points).argmin()]

def match_value(df, col1, x, col2):
    """ Match value x from col1 row to value in col2. """
    return df[df[col1] == x][col2].values[0]



results_dir = Path('C:/Alan/DSC680/Project1Data/').joinpath('results')
results_dir.mkdir(parents=True, exist_ok=True)

filepath = "C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_FinalToAnalyze.csv"
data = pd.read_csv(filepath)

#data['unique_id'] = data.longstrings.map(hash)
data["id"] = data.index + 1
data['geohash'] = data.apply(lambda x: pygeohash.encode(x.latitude, x.longitude), axis=1)
data['point'] = [(x, y) for x,y in zip(data['latitude'], data['longitude'])]

data['closest'] = [closest_point(x, list(data['point'])) for x in data['point']]
data['closest_id'] = [match_value(data, 'point', x, 'id') for x in data['closest']]

mat = cdist(data[['latitude','longitude']],
                              data[['latitude','longitude']], metric='euclidean')
#scipy.spatial.distance.
data_df = pd.DataFrame(mat, index=data['id'], columns=data['id'])
print(data_df.columns)
data_df.to_csv("C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_FinalOUT_REHASHED_2.csv", index=False)

print(data.columns)
data.to_csv("C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_FinalOUT_REHASHED.csv", index=False)
"""
create unique record id
add geohash


"""

data1 = {'Lat': pd.Series([50.6373473,50.63740441,50.63744285,50.63737839,50.6376054,50.6375896,50.6374239,50.6374404]),
         'Lon': pd.Series([3.075029928,3.075068636,3.074951754,3.074913884,3.0750528,3.0751209,3.0750246,3.0749554]),
         'Zone': pd.Series(['A','A','A','A','B','B','B','B'])}

data2 = {'Lat': pd.Series([50.6375524099,50.6375714407]),
         'Lon': pd.Series([3.07507914474,3.07508201591])}


df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

df1['point'] = [(x, y) for x,y in zip(df1['Lat'], df1['Lon'])]
df2['point'] = [(x, y) for x,y in zip(df2['Lat'], df2['Lon'])]

df2['closest'] = [closest_point(x, list(df1['point'])) for x in df2['point']]
df2['zone'] = [match_value(df1, 'point', x, 'Zone') for x in df2['closest']]
print(df2)