import json
import folium
import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)
import pandas as pd

guDF = pd.read_csv('1uu.txt', sep='\t', encoding='UTF-8', index_col="gu")
print(guDF.head(10))

geo_str = json.load(open('skorea_municipalities_geo_simple.json', encoding='utf-8'))
m = folium.Map(location=[37.5502, 126.982], zoom_start=11) #, tiles='Stamen Toner')


map_osm = folium.Choropleth(  #map.choropleth(
                geo_data=geo_str,
               data = guDF['visit'],
               columns = [guDF.index, guDF['visit']],
               fill_color = 'PuRd', #PuRd, YlGnBu
               key_on = 'feature.id').add_to(m)   #feature.properties.SIG_KOR_NM
map_osm.save('osm.html')

#m.get_root().render()


