"""
Author:     Alan Danque
Date:   20210323
Project:
Step:       Exploratory Data Analysis
Purpose:    Wrangle the two datasets to be used for my exploratory data analysis.
"""

import os
import json
import pandas as pd
import glob
import time
start_time = time.time()
#from textblob import TextBlob
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandasql import sqldf
from pandas.api.types import is_datetime64_any_dtype as is_datetime
from numpy.core.defchararray import find
import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
"""
Generate Pandas Profile for RentHop and Yelp Data
Summarize dataset: 100%|██████████| 47/47 [00:29<00:00,  1.60it/s, Completed]
Generate report structure: 100%|██████████| 1/1 [00:09<00:00,  9.18s/it]
Render HTML: 100%|██████████| 1/1 [00:01<00:00,  1.84s/it]
Export report to file: 100%|██████████| 1/1 [00:00<00:00, 77.07it/s]
Summarize dataset: 100%|██████████| 27/27 [00:04<00:00,  5.68it/s, Completed]
Generate report structure: 100%|██████████| 1/1 [00:04<00:00,  4.05s/it]
Render HTML: 100%|██████████| 1/1 [00:01<00:00,  1.27s/it]
Export report to file: 100%|██████████| 1/1 [00:00<00:00, 100.52it/s]
Yelp Review File Complete Duration: --- 57.6655592918396 seconds ---
"""
print("Generate Pandas Profile for RentHop and Yelp Data")
from pandas_profiling import ProfileReport

# Read in the Renthop Data
adf = pd.read_csv("C:/Alan/DSC680/Project1Data/renthopNYC.csv")
bprof = ProfileReport(adf)
bprof.to_file(output_file='C:/Alan/DSC680/Project1Data/EDA/EDA_RentHop_PandasProfileReport_output.html')

#print(adf)
#for col in adf.columns:
#    print(col)
# Read in the Yelp Business Ratings
adf = pd.read_csv("C:/Alan/DSC680/Project1Data/yelp_business_data.csv")
adfnew = adf[['name', 'review_count', 'rating', 'transactions', 'distance', 'coordinates.latitude', 'coordinates.longitude', 'location.address1', 'location.city', 'location.zip_code', 'location.country', 'location.state', 'location.display_address']].copy()
# Modify the $$$ price to numerical form
adfnew['price_dollar_signs'] = adf['price'].str.len()
bprof = ProfileReport(adfnew)
bprof.to_file(output_file='C:/Alan/DSC680/Project1Data/EDA/EDA_Yelp_PandasProfileReport_output.html')

print("Yelp Review File Complete Duration: --- %s seconds ---" % (time.time() - start_time))


