"""
Author: Alan Danque
Date:   20210323
Purpose:Reads very large 23GB csv
Complete: 
Read csv with dask:  1.6846699714660645 sec
"""


from pathlib import Path
import pandas as pd
from pandasql import sqldf
from dask import dataframe as dd
import time
filepath = "C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_FinalOUT_REHASHED_2.csv"
"""
chunksize = 10 ** 6
with pd.read_csv(filename, chunksize=chunksize) as reader:
    for chunk in reader:
        process(chunk)
"""
start = time.time()
data = dd.read_csv(filepath)
end = time.time()
data["id"] = data.index + 1
print("Read csv with dask: ",(end-start),"sec")

#print(data.nsmallest(5, ['1']))
df = data.idxmin(axis=0, skipna=True)
#df[numeric_cols] += 1
#print(df.head())
df.to_csv("C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_IDOFMINVALUES.csv", index=False)

df.iloc[[2]]

"""
filepath = "C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_FinalToAnalyze.csv"
df = pd.read_csv(filepath)
df["id"] = df.index + 1
"""




"""
a = data.shape
print(a[0].compute(),a[1])

#print(data.columns)
print(len(data.columns))

"""

#data = pd.read_csv(filepath)

#data["id"] = data.index + 1

#df = data[['id','1']]
#print(df.head())


"""
# Remove the rows with excessive bathrooms outliers
pysqldf = lambda t: sqldf(t, globals())
## t = "SELECT distinct interest_level from t_df ;"
t = "SELECT top '5' * from data order by '5' ;"
qrt_df = pysqldf(t)
print(qrt_df)
#qrt_df.to_csv("C:/Alan/DSC680/Project1Data/MasterAnalyticsDataSet_FinalOUT_TOP5_IDS.csv", index=False)
"""