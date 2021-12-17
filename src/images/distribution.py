import json
import plotly.express as px
import plotly.io as pio
import pandas as pd
from vaccine import provinces

pio.renderers.default = "firefox"

province_id_map = {}

file = open("diaphantinh.geojson","r")
vietnam_province = json.load(file)

for feature in vietnam_province['features']:
    feature['id'] = feature['properties']['gid']
    province_id_map[feature['properties']['ten_tinh']] = feature['id']


df = pd.DataFrame.from_dict(provinces)
df['province_distribution_percentage'] = df['province_distribution_percentage'].apply(lambda x : float(x.split("%")[0].replace(",",".")) )
df['id'] = df['province_name'].apply(lambda x: province_id_map[x])

fig = px.choropleth(df, locations = "id",geojson=vietnam_province,
                    color="province_distribution_percentage",hover_name="province_name",
                    hover_data=['province_population','province_actual_distribution'])
fig.update_geos(fitbounds="locations",visible=False)
pio.write_image(fig, 'distribution.png',scale =1)
fig.show()
