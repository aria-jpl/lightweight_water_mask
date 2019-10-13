from setuptools import setup, find_packages
import glob

data_files = []
directories = glob.glob('lightweight_water_mask/data/')
for directory in directories:
    files = glob.glob(directory+'*')
    data_files.append((directory, files))

setup(
    name='lightweight_water_mask',
    version='0.2',
    description="Water mask utility, using OpenStreetMap water shapefiles",
    author="Justin Linick",
    author_email="Justin.P.Linick@jpl.nasa.gov",
    # packages=find_packages(),
    # py_modules=['geopandas', 'shapely', 'fiona', 'pyproj'],
    install_requires=['geopandas', 'shapely', 'fiona', 'pyproj'],
    data_files=data_files
)
