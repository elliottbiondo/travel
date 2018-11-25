import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
import io

lat = []
lon = []

with open("places.json") as f:
    for line in f.readlines():
        if "Latitude" in line:
            lat.append(float(line.split()[2].replace('"', '').replace(',', '')))
        elif "Longitude" in line:
            lon.append(float(line.split()[2].replace('"', '').replace(',', '')))

#lat_min = 23
lat_min = 0
lat_max = 60
lon_min = -150
lon_max = 150

# create map using BASEMAP
m = Basemap(llcrnrlon=lon_min,
            llcrnrlat=lat_min,
            urcrnrlon=lon_max,
            urcrnrlat=lat_max,
            lat_0=(lat_max - lat_min)/2,
            lon_0=(lon_max-lon_min)/2,
            projection='merc',
            resolution = 'h',
            area_thresh=10000.,
            )

land_color="gray"
water_color="white"
marker_color="red"

m.drawmapboundary(fill_color=water_color)
m.fillcontinents(color = land_color, lake_color=water_color)

# convert lat and lon to map projection coordinates
lons, lats = m(lon, lat)

# plot points as red dots
m.scatter(lons, lats, marker = 'o', s=2, color=marker_color, zorder=5)


plt.savefig("map.png", bbox_inches="tight")
