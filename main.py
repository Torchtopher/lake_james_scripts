from sonarlight import Sonar

#Read data from a '.sl2' or '.sl3' file
sl2 = Sonar('HCA.sl2')

#See summary of data and available channels
print(sl2)

import matplotlib.pyplot as plt

#Plot route and water depth (meters)
route = sl2.df.query("survey == 'primary'")

import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt

# Extract lon/lat/depth arrays
lon = route["longitude"].values
lat = route["latitude"].values
depth = route["water_depth"].values

# Define grid resolution (degrees, adjust for your lake size)
grid_res = 0.00001  # ≈ 11 m per pixel at mid-latitudes
lon_grid, lat_grid = np.meshgrid(
    np.arange(lon.min(), lon.max(), grid_res),
    np.arange(lat.min(), lat.max(), grid_res)
)

# Interpolate depth onto grid
depth_grid = griddata((lon, lat), depth, (lon_grid, lat_grid), method="cubic")

# Plot bathymetry map
plt.figure(figsize=(8,6))
im = plt.imshow(
    depth_grid,
    extent=(lon.min(), lon.max(), lat.min(), lat.max()),
    origin="lower",
    cmap="viridis"
)
plt.colorbar(im, label="Depth (m)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Interpolated lake depth map")
plt.show()


print(route.columns)
plt.scatter(route["longitude"], route["latitude"], c=route["water_depth"], s = 3)
plt.colorbar()
plt.show()

#Plot primary channel
prim = sl2.image("primary")
plt.imshow(prim.transpose())
plt.show()

plt.scatter(route["longitude"], route["latitude"], c=route["water_depth"], s=5)
plt.gca().invert_yaxis()  # optional, depends on map orientation
plt.colorbar(label="Depth (m)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Survey track colored by depth")
plt.show()
