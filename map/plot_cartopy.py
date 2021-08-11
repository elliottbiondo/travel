import ssl
ssl._create_default_https_context = ssl._create_unverified_context


import matplotlib.pyplot as plt
import cartopy.crs as ccrs                   # import projections
import cartopy.feature as cf                 # import features

lat = []
lon = []

with open("places.json") as f:
    for line in f.readlines():
        if "Latitude" in line:
            lat.append(float(line.split()[2].replace('"', '').replace(',', '')))
        elif "Longitude" in line:
            lon.append(float(line.split()[2].replace('"', '').replace(',', '')))

with open("hack.txt") as f:
    for line in f.readlines():
        if "LL" in line:
            lat.append(float(line.split()[1].strip(",")))
            lon.append(float(line.split()[2]))

lon_min = -140
lon_max = 140
lat_min = 17
lat_max = 62

ax = plt.subplot(projection = ccrs.PlateCarree())
ax.add_feature(cf.NaturalEarthFeature('physical', 'land', '50m', edgecolor='none', facecolor='#e0e0e0'))
ax.add_feature(cf.NaturalEarthFeature('physical', 'lakes', '50m', edgecolor='none', facecolor='white'))
ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())

ax.scatter(lon, lat, transform=ccrs.PlateCarree(), s=1, color='black',  zorder=2, lw=0)

plt.savefig("map.png", bbox_inches="tight", dpi=1000, pad_inches=-0.01)
