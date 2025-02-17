# Automated_Power_Plants_Bavaria
Automated geospatial assessment and placement of power plants in Bavaria using Python. Integrates data from OpenStreetMap and governmental sources, processed with GeoPandas and Shapely. Generates a validated dataset for energy planning. Developed as part of a master's thesis at the Technical University of Munich.
## Overview
Bavaria is transitioning toward renewable energy with a special focus on geothermal energy. This project automates the creation of a geospatial dataset for power plants in Bavaria, ensuring reliable, scalable, and error-validated data. The final output aids in planning renewable energy infrastructure and was developed as part of the Geothermal Alliance Bavaria project.
## Features
* Automated data extraction, cleaning, and integration from multiple sources (OpenStreetMap, Energieatlas Bayern, Bundesnetzagentur, etc.).
* Validation and correction of geographical anomalies using geospatial techniques (e.g., buffer aggregation, spatial joins).
* Output as a unified geospatial dataset for analysis in GIS tools like QGIS and ArcGIS.
* Utilized Python libraries: GeoPandas, Pandas, Shapely, Nominatim.
## Technologies Used
* Programming Language: Python 3.9+
* Libraries: GeoPandas, Pandas, Shapely, Geopy, osmnx
* Data Sources: OpenStreetMap, Energieatlas Bayern, Bundesnetzagentur, Open Power System Data (OPSD)
## Repository Structure
```
├── data/                     # Placeholder for raw and processed data (add only open data links if applicable)
├── scripts/                  # Python scripts for data processing
│   ├── geocoding_xlsx.ipynb    # Handles data cleaning and integration
│   ├── merge_shapefiles.ipynb  # Validation and correction of outliers
│   └── osm_search.ipynb      # Optional: Code for visualizing results in QGIS
│   └── postcodes.ipynb      # Optional: Code for visualizing results in QGIS
│   └── utils.py      # Optional: Code for visualizing results in QGIS
├── README.md                 # Project description
└── requirements.txt          # List of Python dependencies
```
## Downloading Data via Overpass Turbo  
To obtain the Bavarian postal code boundaries, use the following Overpass Turbo query: 
```overpass
[out:json][timeout:90];
area[name="Bayern"];
relation(area)["boundary"="postal_code"];
out geom;
```
1. Go to [Overpass Turbo](https://overpass-turbo.eu/).
2. Copy and paste the query into the editor.
3. Run the query and export the result as GeoJSON.
4. Save it as:
```
data/bayern_postcodes_overpass_turbo.geojson
```
