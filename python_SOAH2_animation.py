# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 21:17:30 2019
Create map of miniboat or drifter data - see educationalpassages.org and studentdrifters.org for project information

@author: Cassie Stymiest
Derived from code by James Manning, Huanxin Xu, NOAA NEFSC

"""
from matplotlib import pyplot as plt  # imports a plotting toolbox
from matplotlib import animation  # imports an animation toolbox
import pandas as pd  # imports a very useful toolbox that does many things like read csv files
df=pd.read_csv('https://www.nefsc.noaa.gov/drifter/drift_193320801.csv',index_col=[1]) #defines the data file, check col in csv file as some nefsc files it is col 0
def animate(i):       
    plt.plot(df.loc[193320801]['LON'].iloc[20*i:20*(i+1)+1], df.loc[193320801]['LAT'].iloc[20*i:20*(i+1)+1],'-',markersize=9,color='b')
ani=animation.FuncAnimation(plt.figure(figsize=(10,10)),animate,frames=int(len(df.loc[193320801])/20), blit=False)
axes = plt.gca()
axes.set_xlim([-74,0])
axes.set_ylim([30,60]) # sets boundaries for the axes so they won't move during animation
ani.save('soah_animation2.gif') # saves the animation as a gif file
plt.show()


