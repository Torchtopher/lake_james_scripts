import rasterio
from rasterio.warp import transform
from rasterio.plot import show
from sonarlight import Sonar
from matplotlib import pyplot
import numpy as np

sl2 = Sonar('HCA.sl2')
route = sl2.df.query("survey == 'primary'")
lon = route["longitude"].values
lat = route["latitude"].values

with rasterio.open("sattelite_imgs/HCA.tif") as src:
    xs, ys = transform('EPSG:4326', src.crs, lon, lat)

    fig, ax = pyplot.subplots(figsize=(12, 8))
    show(src, ax=ax)

    scatter = ax.scatter(xs, ys, s=3, c=route["water_depth"], label='Survey Route')
    pyplot.colorbar(scatter, ax=ax, label='Water Depth (m)')
    pyplot.show()

sl2 = Sonar('BBA.sl2')
route = sl2.df.query("survey == 'primary'")
lon = route["longitude"].values
lat = route["latitude"].values

with rasterio.open("sattelite_imgs/BBA.tif") as src:
    xs, ys = transform('EPSG:4326', src.crs, lon, lat)

    fig, ax = pyplot.subplots(figsize=(12, 8))
    show(src, ax=ax)

    scatter = ax.scatter(xs, ys, s=3, c=route["water_depth"], label='Survey Route')
    pyplot.colorbar(scatter, ax=ax, label='Water Depth (m)')
    pyplot.show()
