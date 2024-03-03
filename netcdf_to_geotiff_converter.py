#!/usr/bin/env python
import xarray as xr
import rioxarray as rio
from osgeo import gdal
import argparse
import os
import re
from osgeo import gdal
gdal.UseExceptions()

def nc_to_geotiff(filename,crs):
        ncfile = xr.open_dataset(filename)
        #Extract the variable
        variable = ncfile[list(ncfile.data_vars.keys())[0]]

        #Define lat/long 
        variable = variable.rio.set_spatial_dims('lon', 'lat')
        
        # if changing crs do it if not leave it in default
        if crs == "epsg:4326":
                warpoptions = gdal.WarpOptions(
                        srcSRS="epsg:4326",
                        dstSRS=crs
                )

                variable.rio.to_raster(os.path.splitext(filename)[0]+'.tmp.tif')
                ds = gdal.Warp(os.path.splitext(filename)[0]+'.tif',
                                os.path.splitext(filename)[0]+'.tmp.tif',
                                options=warpoptions )
                os.unlink(os.path.splitext(filename)[0]+'.tmp.tif')
        else:
                variable.rio.to_raster(os.path.splitext(filename)[0]+'.tif')

if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Process GeoTIFF file')
        parser.add_argument('-n','--netcdf4_dir', type=str, required=True,
                                help='Directory with bunch of netcdf4 files inside')
        
        parser.add_argument('-c','--crs', type=str, required=False, default="epsg:4326",
                                help='crs of the output geotiff(s)')
        
        args = parser.parse_args()


        for filename in os.listdir(args.netcdf4_dir):
                if re.search('(.*).nc$', filename):
                        nc_to_geotiff(os.path.join(args.netcdf4_dir,filename),args.crs)
