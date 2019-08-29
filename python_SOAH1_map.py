# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:12:24 2019

@author: Cassie Stymiest, adapted from James Manning and Huanxin Xu
"""
# This imports the plot tool from the "matplotlib" toolbox and calls it "plt":
from matplotlib import pyplot as plt
# We also import the “pandas” data-manipulation toolbox and call it “pd”:
import pandas as pd 
# Next we read the data file which has a header line describing each column. It specifies column zero as the “index.”  We store this data in the variable df: 
df = pd.read_csv('https://www.nefsc.noaa.gov/drifter/drift_193320801.csv', index_col=[1])  # check col in csv file as some nefsc files it is col 0
# Now we locate all rows with index = 193320801,  find the “x” value (longitude) and the “y” value (latitude) and plot the track.
df.loc[193320801].plot(x='LON',y='LAT',legend=False)
plt.savefig('map.png')
# Finally, we ask Python to show a plot of these data:
plt.show()
