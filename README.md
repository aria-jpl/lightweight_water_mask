## lightweight_water_mask package

This package uses global shapefiles to provide lightweight, fast land/water reporting for geojson inputs.

### Installation
```bash
python setup.py install
```

To test, in a python shell:
```python
>>> import lightweight_water_mask
>>> lightweight_water_mask.test()
```
Should return:
```
------------------------------------------------------
Evaluating area:   land_only_polygon
Covers any water?  False
Covers any land?   True
Covers only land?  True
Covers only water? False
Land area:         5.56 km^2
Water area:        0.00 km^2
Land coverage:     1.0
Water coverage:    0.0
------------------------------------------------------
Evaluating area:   caspian
Covers any water?  True
Covers any land?   True
Covers only land?  False
Covers only water? False
Land area:         160,119.04 km^2
Water area:        379,902.85 km^2
Land coverage:     0.296504721025
Water coverage:    0.703495278975
------------------------------------------------------
Evaluating area:   iceland
Covers any water?  True
Covers any land?   True
Covers only land?  False
Covers only water? False
Land area:         102,765.67 km^2
Water area:        111,487.34 km^2
Land coverage:     0.479646327138
Water coverage:    0.520353672862
------------------------------------------------------
Evaluating area:   new_zealand
Covers any water?  True
Covers any land?   True
Covers only land?  False
Covers only water? False
Land area:         267,330.89 km^2
Water area:        6,214,898.76 km^2
Land coverage:     0.041240576778
Water coverage:    0.958759423222
------------------------------------------------------
Evaluating area:   land_and_water_polygon
Covers any water?  True
Covers any land?   True
Covers only land?  False
Covers only water? False
Land area:         25,496.46 km^2
Water area:        23,308.48 km^2
Land coverage:     0.522415581185
Water coverage:    0.477584418815
------------------------------------------------------
Evaluating area:   hawaii
Covers any water?  True
Covers any land?   True
Covers only land?  False
Covers only water? False
Land area:         16,679.60 km^2
Water area:        1,136,885.80 km^2
Land coverage:     0.0144591719663
Water coverage:    0.985540828034
------------------------------------------------------
Evaluating area:   water_only_polygon
Covers any water?  True
Covers any land?   False
Covers only land?  False
Covers only water? True
Land area:         0.00 km^2
Water area:        858.72 km^2
Land coverage:     0.0
Water coverage:    1.0
```

### Run mask

The import can run four functions which take a geojson as an input.
* covers_land(geojson): returns True/False if the geojson covers **any** land.
* covers_water(geojson): returns True/False if the geojson covers **any** water.
* covers_only_water(geojson): returns True/False if the geojson covers **only** water.
* covers_only_land(geojson): returns True/False if the geojson covers **only** land.
* get_land_area(geojson): returns the land area in km^2 that is enclosed by the geojson.
* get_water_area(geojson): returns the water area in km^2 that is enclosed by the geojson.
* get_water_percentage(geojson): returns the percentage (between 0.0 and 1.0) of the geojson that is covered by water.
* get_land_percentage(geojson): returns the percentage (between 0.0 and 1.0) of the geojson that is covered by land.
* get_land_polygons(geojson): returns the land polygons covering the geojson, as either a geojson Polygon, MultiPolygon, or None
* get_water_polygons(geojson): returns the water polygons covering the geojson, as either a geojson Polygon, MultiPolygon, or None
examples:

```python
>>> import lightweight_water_mask
>>> test_geojson = {"type": "Polygon", "coordinates":[[[-120.3117620944977,32.9773526159236],[-120.35270333290102,32.75546576141111],[-120.1521009206772,32.67390732403642],[-119.98687148094179,32.86846786484173],[-120.13354003429414,33.02966016839023],[-120.3117620944977,32.9773526159236]]]}
>>> lightweight_water_mask.covers_land(test_geojson)
False
>>> lightweight_water_mask.covers_only_land(test_geojson)
False
>>> lightweight_water_mask.covers_water(test_geojson)
True
>>> lightweight_water_mask.covers_only_water(test_geojson)
True
>>> lightweight_water_mask.get_land_area(test_geojson)
0
>>> lightweight_water_mask.get_water_area(test_geojson)
858.7225910555086

```

