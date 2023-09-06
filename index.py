#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd
import folium
import branca.colormap as cm


# In[2]:


#fpath = "/media/x/data/shape_collection/bkg.bund/vg250_01-01.utm32s.shape.ebenen/vg250_ebenen_0101/VG250_GEM.shp"
#fpath = "/media/x/data/kostra/GIS_KOSTRA-DWD-2010R_D0120/StatRR_KOSTRA-DWD-2010R_D0120.shp"
fpath = "/media/x/data/paul/basins_all_info.gpkg"


# In[3]:


data = gpd.read_file(fpath)
data = data.to_crs(epsg=4326)


# In[4]:


# reduce size
data = data[["sub_id", "highest_peak", "geometry"]]


# In[ ]:


x_map=data.centroid.x.mean()
y_map=data.centroid.y.mean()
print(x_map,y_map)


# In[16]:


mymap = folium.Map(location=[y_map, x_map], zoom_start=6,tiles=None)
folium.TileLayer('CartoDB positron',name="Light Map",control=False).add_to(mymap)

data2 = data.loc[data.index[:1000]]

myscale = (data['highest_peak'].quantile((0,0.1,0.75,0.9,0.98,1))).tolist()
mymap.choropleth(
 geo_data=data2,
 name='Choropleth',
 data=data2,
 columns=["sub_id", 'highest_peak'],
 key_on="feature.properties.sub_id",
 fill_color='YlGnBu',
 threshold_scale=myscale,
 fill_opacity=0.8,
 line_opacity=0.2,
)
mymap


# In[19]:


#mymap.save("index.html")


# In[23]:


#data[["highest_peak","geometry"]].to_file('data.geojson', driver='GeoJSON', float_format="%.1f")


# In[ ]:




