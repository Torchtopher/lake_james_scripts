from sonarlight import Sonar
import numpy as np
import pandas as pd
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read data from sonar file
sl2 = Sonar('HCA.sl2')

# Get primary survey data
route = sl2.df.query("survey == 'primary'")

# Extract lon/lat/depth arrays
lon = route["longitude"].values
lat = route["latitude"].values
depth = route["water_depth"].values

print(lon)
print(lat)
print(route.columns)

# Define grid resolution (degrees, adjust for your lake size)
# grid_res = 0.00001  # ≈ 11 m per pixel at mid-latitudes
grid_res = 1 # ≈ 11 m per pixel at mid-latitudes
lon_grid, lat_grid = np.meshgrid(
    np.arange(lon.min(), lon.max(), grid_res),
    np.arange(lat.min(), lat.max(), grid_res)
)

# Interpolate depth onto grid
depth_grid = griddata((lon, lat), depth, (lon_grid, lat_grid), method="cubic")

# Create 3D surface plot
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface - invert depth to show lake bottom topology
# (multiply by -1 so deeper areas appear lower)
surf = ax.plot_surface(lon_grid, lat_grid, -depth_grid,
                       cmap='terrain',
                       edgecolor='none',
                       antialiased=True,
                       alpha=0.9)

# Customize the plot
ax.set_xlabel('Longitude', fontsize=10)
ax.set_ylabel('Latitude', fontsize=10)
ax.set_zlabel('Depth (m)', fontsize=10)
ax.set_title('3D Bathymetric Model of Lake', fontsize=14, fontweight='bold')

# Add colorbar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5, label='Depth (m)')

# Adjust viewing angle for better perspective
ax.view_init(elev=30, azim=45)

# Improve layout
plt.tight_layout()
plt.show()

# Optional: Create a second plot with different viewing angle
fig2 = plt.figure(figsize=(14, 10))
ax2 = fig2.add_subplot(111, projection='3d')

surf2 = ax2.plot_surface(lon_grid, lat_grid, -depth_grid,
                         cmap='viridis',
                         edgecolor='none',
                         antialiased=True,
                         alpha=0.9)

ax2.set_xlabel('Longitude', fontsize=10)
ax2.set_ylabel('Latitude', fontsize=10)
ax2.set_zlabel('Depth (m)', fontsize=10)
ax2.set_title('3D Bathymetric Model - Alternate View', fontsize=14, fontweight='bold')

fig2.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5, label='Depth (m)')

# Different viewing angle
ax2.view_init(elev=60, azim=135)

plt.tight_layout()
plt.show()
