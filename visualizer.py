from osgeo import gdal, osr
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import xarray as xr
from IPython import embed
import numpy
from affine import Affine

gdal.UseExceptions()


fname = './img.tif'
da = xr.open_rasterio(fname)
transform = Affine.from_gdal(*da.attrs['transform'])

ds = gdal.Open(fname)
data = ds.ReadAsArray()
gt = ds.GetGeoTransform()
proj = ds.GetProjection()

inproj = osr.SpatialReference()
inproj.ImportFromWkt(proj)

extent = (gt[0], gt[0] + ds.RasterXSize * gt[1],
          gt[3] + ds.RasterYSize * gt[5], gt[3])
print(inproj)

'''
# Define the projection
crs=ccrs.PlateCarree()
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111, projection=crs)
ax.imshow(da.variable.data[0])
ax.coastlines()
#ax.set_extent(list(extent))
plt.show()


'''

projcs = inproj.GetAuthorityCode('PROJCS')
projection = ccrs.epsg(projcs)
print(projection)


subplot_kw = dict(projection=projection)
fig, ax = plt.subplots(figsize=(12, 9), subplot_kw=subplot_kw)
ax.coastlines(resolution='50m', color='black', linewidth=1)
#ax.drawmapboundary(fill_color='aqua')
#ax.fillcontinents(color='coral',lake_color='aqua')
#ax.set_extent([-180, 180, -20, 20])
ax.add_feature(cfeature.LAND)
#ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')
#ax.add_feature(cfeature.LAKES, alpha=0.5)
#ax.add_feature(cfeature.RIVERS)
states_provinces = cfeature.NaturalEarthFeature(
    category='cultural',
    name='admin_1_states_provinces_lines',
    scale='50m',
    facecolor='none')
ax.add_feature(states_provinces, edgecolor='gray')


#ax.imshow(data[:3, :, :].transpose((1, 2, 0)), extent=extent,origin='upper',)
image = data[:3, :, :].transpose((1, 2, 0))
image = image.astype(float)
image /= 255.
image = numpy.ma.masked_where(image == 0.0, image)
ax.imshow(image, extent=extent,origin='upper',)
plt.show()
#'''