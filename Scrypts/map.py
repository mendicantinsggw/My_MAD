import pandas as pd
import folium
m = folium.Map(location=[52.86146928009639, 18.63998114971221], zoom_start=7, tiles=None)
state_geo = r"Scrypts/mapa.json"
state_data = pd.read_csv("Methods\TOPSIS\Matura2020_ranking_Topsis.csv" )
folium.Choropleth(
    geo_data=state_geo,
    name="choropleth",
    data=state_data,
    columns=["group", "Nowak"],
    key_on="properties.NAME_1",
    fill_color="YlGn",
    fill_opacity=1,
    line_opacity=0.1,
    legend_name="Unemployment Rate (%)",
).add_to(m)
folium.LayerControl().add_to(m)
m.save('my_map.html')