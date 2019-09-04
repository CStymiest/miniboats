# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 22:42:06 2019
Create map of miniboat or drifter data - see educationalpassages.org and studentdrifters.org for project information

@author: Cassie Stymiest
Adapted from https://makersportal.com/blog/2018/7/20/geographic-mapping-from-a-csv-file-using-python-and-basemap

"""
#!/usr/bin/python

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import csv

import os
import conda

# grabbing the csv data
lats, lons, names, sst = [],[],[],[]
temp_dat = []
with open('drift_193320801.csv') as csvfile:
    reader = csv.DictReader(csvfile,delimiter=',')
    for data in reader:
        # to select part of data set:         
        # if float(data['UTC'])>-5. or float(data['UTC'])<-8. or float(data['ELEV'])<0.0:
          #  continue
        names.append('K'+data['YEARDAY'])
        lats.append(float(data['lat']))
        lons.append(float(data['lon']))

conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib

# How much to zoom from coordinates (in degrees)
zoom_scale = 3

# Setup the bounding box for the zoom and bounds of the map
#bbox = [np.min(lats)-zoom_scale,np.max(lats)+zoom_scale,\
#        np.min(lons)-zoom_scale,np.max(lons)+zoom_scale]
#untested modification by JiM
bbox = [int(np.min(lats)-zoom_scale),int(np.max(lats)+zoom_scale),int(np.min(lons)-zoom_scale),int(np.max(lons)+zoom_scale)]

fig, ax = plt.subplots(figsize=(12,6))
plt.title("SOAH")
# Define the projection, scale, the corners of the map, and the resolution.
m = Basemap(projection='merc',llcrnrlat=bbox[0],urcrnrlat=bbox[1],\
            llcrnrlon=bbox[2],urcrnrlon=bbox[3],lat_ts=10,resolution='i')

# Draw coastlines and fill continents and water with color
m.drawcoastlines()
m.fillcontinents(color='grey',lake_color='dodgerblue')

# draw parallels, meridians, and color boundaries
m.drawparallels(np.arange(bbox[0],bbox[1],(bbox[1]-bbox[0])/5),labels=[1,0,0,0])
m.drawmeridians(np.arange(bbox[2],bbox[3],(bbox[3]-bbox[2])/5),labels=[0,0,0,1],rotation=45)
m.drawmapboundary(fill_color='lightblue')

# build and plot coordinates onto map
x,y = m(lons,lats)
m.plot(x,y,'w*',markersize=2)
plt.title("Spirit of Ashley Hall Miniboat Track")
plt.savefig('soah_mapbase.png', format='png', dpi=500)
plt.show()

