import folium
dir(folium)
my_map = folium.Map(location=[34.160583, -118.114990])
file_path = '/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Map.html'
my_map.save(file_path)

#Adding a Marker to the Map
my_map_3 = folium.Map(location=[38.58, -99.09],zoom_start=6, titles="Stamen Terrain")
my_map_3.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker",icon=folium.Icon(color="green")))
file_path = '/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Map3.html'
my_map_3.save(file_path)

# Practicing for-loops by adding multiple markers
my_map_4 = folium.Map(location=[38.58, -99.09],zoom_start=6, titles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")
for coordinates in [[38.2, -99.1],[39.2, -95.5]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker",icon=folium.Icon(color="pink")))
my_map_4.add_child(fg)
file_path = '/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Map4.html'
my_map_4.save(file_path)

# Practicing File processing by adding markers from files
import pandas

data = pandas.read_csv("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])

my_map_5 = folium.Map(location=[38.58, -99.09],zoom_start=6, titles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi I am a Marker",icon=folium.Icon(color="blue")))

my_map_5.add_child(fg)
file_path = '/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Map5.html'
my_map_5.save(file_path)

# How to add text to the map popup window
import pandas

data = pandas.read_csv("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

my_map_6 = folium.Map(location=[38.58, -99.09],zoom_start=6, titles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m",icon=folium.Icon(color="blue")))

my_map_6.add_child(fg)
file_path = '/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Map6.html'
my_map_6.save(file_path)

# Create a color generation function for markers
import pandas

data = pandas.read_csv("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 100 <= elevation < 3000:
        return 'orange'
    else:
        return 'yellow'

my_map_7 = folium.Map(location=[38.58, -99.09],zoom_start=6, titles="Mapbox Bright")
fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+" m",icon=folium.Icon(color=color_producer(el))))

my_map_7.add_child(fg)
file_path = '/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Map7.html'
my_map_7.save(file_path)

# Exploring the Population JSON data
import pandas

data = pandas.read_csv("/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 100 <= elevation < 3000:
        return 'orange'
    else:
        return 'yellow'

my_map_8 = folium.Map(location=[38.58, -99.09],zoom_start=6, titles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Vocanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",fill_color=color_producer(el), color ='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open('/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/world.json', 'r', encoding='utf-8-sig').read()), 
style_function=lambda x:{'fillColor':'blue' if x ['properties']['POP2005'] < 1000000 else 'purple' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'yellow'}))

my_map_8.add_child(fgv)
my_map_8.add_child(fgp)
my_map_8.add_child(folium.LayerControl())
file_path = '/Users/nguyenthuyvy/Desktop/Basic Knowledge/PYTHON/Python Projects_Oreilly/10 Python Projects/Python_Real_Projects/5. App 1- Web mapping with Python/Map8.html'
my_map_8.save(file_path)







