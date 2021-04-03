"""
Author: Alan Danque
Date:   20210323
Purpose:Issues with the conversion of the decision tree dot to png file
"""
import pydot
from pathlib import Path
import pandas as pd
import time
start_time = time.time()
pd.options.mode.chained_assignment = None  # default='warn'  # https://stackoverflow.com/questions/20625582/how-to-deal-with-settingwithcopywarning-in-pandas

results_dir = Path('C:/Alan/DSC680/Project1Data/').joinpath('results')
results_dir.mkdir(parents=True, exist_ok=True)

tree_dot_file = results_dir.joinpath('tree.dot')
tree_png_file = results_dir.joinpath('tree.png')
dotfile = open(tree_dot_file, 'r')
treepngfile = open(tree_png_file, 'w')

#from subprocess import check_call
#check_call(['dot','-Tpng',dotfile,'-o',treepngfile])

(graph,) = pydot.graph_from_dot_file(tree_dot_file)
graph.write_png(tree_png_file)

print("PyDot Conversion Complete: --- %s seconds  ---" % (time.time() - start_time))
"""
PyDot Conversion Complete: --- 3804.3111951351166 seconds  ---
"""
