# GeoSpatial Data Processing Tools

This repository contains tools for processing geospatial data, specifically for reading GeoTIFF files and converting NetCDF files to GeoTIFF format.

## Files

- `geotiff_reader.py`: A script to read GeoTIFF files and extract data based on latitude and longitude coordinates.
- `netcdf_to_geotiff_converter.py`: A script to convert NetCDF files to GeoTIFF format with the option to specify the coordinate reference system (CRS).
- `requirements.txt`: A list of Python packages required to run the scripts.

## Usage

### geotiff_reader.py
To use the GeoTIFF reader, navigate to the directory containing the `geotiff_reader.py` script and run the following command:

```sh
usage: geotiff_reader.py [-h] [-f GEOTIFF_FILE] [-d GEOTIFF_DIR] -p POINTS_FILE [-b RASTER_BAND] [-a] [--csv_output CSV_OUTPUT]

Process GeoTIFF file

options:
  -h, --help            show this help message and exit
  -f GEOTIFF_FILE, --geotiff_file GEOTIFF_FILE
                        GeoTIFF file location
  -d GEOTIFF_DIR, --geotiff_dir GEOTIFF_DIR
                        Directory with bunch of GeoTIFF files inside
  -p POINTS_FILE, --points_file POINTS_FILE
                        File with points columns (longitude,latitude)
  -b RASTER_BAND, --raster_band RASTER_BAND
                        Raster band in tiff file you would like to read data from
  -a, --all_bands       Read values from all raster bands
  --csv_output CSV_OUTPUT

```

Replace `<path_to_csv_with_points>` with the path to the CSV file containing the points (longitude, latitude). Optionally, you can specify a single GeoTIFF file using `--geotiff_file` or a directory containing multiple GeoTIFF files using `--geotiff_dir`. Use `--raster_band` to specify a particular band to read from the GeoTIFF file(s), or use `--all_bands` to read from all available bands. The results will be written to the file specified by `--csv_output`, which defaults to `output.csv` if not provided.

To use the GeoTIFF reader, you need to provide a GeoTIFF file or a directory containing GeoTIFF files, and a CSV file with points (longitude, latitude). The script will output a CSV file with the extracted data.

To use the GeoTIFF reader, you need to provide a GeoTIFF file or a directory containing GeoTIFF files, and a CSV file with points (longitude, latitude). The script will output a CSV file with the extracted data.

### netcdf_to_geotiff_converter.py

To convert NetCDF files to GeoTIFF, provide a directory containing NetCDF files. You can also specify the CRS for the output GeoTIFF files.

To convert NetCDF files to GeoTIFF format, navigate to the directory containing the `netcdf_to_geotiff_converter.py` script and run the following command:

```sh
usage: netcdf_to_geotiff_converter.py [-h] -n NETCDF4_DIR [-c CRS]

Process GeoTIFF file

options:
  -h, --help            show this help message and exit
  -n NETCDF4_DIR, --netcdf4_dir NETCDF4_DIR
                        Directory with bunch of netcdf4 files inside
  -c CRS, --crs CRS     crs of the output geotiff(s)
```

Replace `<path_to_netcdf_files_directory>` with the path to the directory containing your NetCDF files. Optionally, you can specify the coordinate reference system (CRS) for the output GeoTIFF files by replacing `<coordinate_reference_system>` with the desired CRS code (e.g., "epsg:4326").

If you do not specify a CRS, the script will default to "epsg:4326".

## Installation

To install the required Python packages, run:

```sh
pip install -r requirements.txt
```

Ensure you have the necessary system libraries for GDAL installed on your system.


If you get error from tools that states
```
Traceback (most recent call last):
  File "/home/steki/GITHUB/geo-tools/./geotiff_reader.py", line 3, in <module>
    from osgeo import gdal, ogr, gdal_array
  File "/home/steki/GITHUB/geo-tools/idiote/lib64/python3.11/site-packages/osgeo/gdal_array.py", line 10, in <module>
    from . import _gdal_array
ImportError: cannot import name '_gdal_array' from 'osgeo' (/home/steki/GITHUB/geo-tools/idiote/lib64/python3.11/site-packages/osgeo/__init__.py)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/steki/GITHUB/geo-tools/./geotiff_reader.py", line 6, in <module>
    raise ImportError("The GDAL fun part........ \n\n run:\n\tpip3 install --no-cache-dir --force-reinstall 'GDAL[numpy]==3.8.3'\n") from e
ImportError: The GDAL fun part........ 

 run:
        pip3 install --no-cache-dir --force-reinstall 'GDAL[numpy]==3.8.3'
```

run suggested 
```sh
pip3 install --no-cache-dir --force-reinstall 'GDAL[numpy]==3.8.3'
``` 
but change version (3.8.3) to your system installed libgdal version
