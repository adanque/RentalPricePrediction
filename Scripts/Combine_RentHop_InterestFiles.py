"""
Author: Alan Danque
Date:   20210323
Purpose:Combines the Low, Medium and High Interest Level Files after ZipCode processing
"""
import os, shutil
from pathlib import Path
import glob
import time
from datetime import date, datetime, timedelta
start_datetime = datetime.now()
start_time = time.time()
interval = .1

mypath = "C:\\alan\\DSC680\\Project1Data"
base_dir = Path(mypath)
# appdir = Path(os.path.dirname(base_dir)) # Only used for need to use parent folder
stag_dir = base_dir.joinpath('Staging')
stag_dir.mkdir(parents=True, exist_ok=True)

bfilename = 'MasterFinalAnalyticsDataSet.csv'
DataExportFile = stag_dir.joinpath(bfilename)
# Create output
stag_dir_p = str(stag_dir) +'\\MasterDataset_*.csv'
with open(DataExportFile, "ab") as outfile:
    for filename in glob.glob(stag_dir_p):
        print(filename)
        if filename == DataExportFile:
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)

print(" Complete: --- %s seconds has passed ---" % (time.time() - start_time))

