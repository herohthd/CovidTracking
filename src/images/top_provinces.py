import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
import numpy as np
import pandas as pd
from .vaccine import top_vaccinated_provinces,least_vaccinated_provinces
# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig,ax = plt.subplots()

top_vaccinated_provinces = {
    "provinces":
                [top_vaccinated_provinces[0]['province_name'],
                top_vaccinated_provinces[1]['province_name'],
                top_vaccinated_provinces[2]['province_name'],
                top_vaccinated_provinces[3]['province_name'],
                top_vaccinated_provinces[4]['province_name'],
                top_vaccinated_provinces[5]['province_name'],
                top_vaccinated_provinces[6]['province_name'],
                top_vaccinated_provinces[7]['province_name'],
                top_vaccinated_provinces[8]['province_name'],
                top_vaccinated_provinces[9]['province_name'],
                ],
    "two_dose_percentage":
                [top_vaccinated_provinces[0]['province_two_dose_percentage'],
                top_vaccinated_provinces[1]['province_two_dose_percentage'],
                top_vaccinated_provinces[2]['province_two_dose_percentage'],
                top_vaccinated_provinces[3]['province_two_dose_percentage'],
                top_vaccinated_provinces[4]['province_two_dose_percentage'],
                top_vaccinated_provinces[5]['province_two_dose_percentage'],
                top_vaccinated_provinces[6]['province_two_dose_percentage'],
                top_vaccinated_provinces[7]['province_two_dose_percentage'],
                top_vaccinated_provinces[8]['province_two_dose_percentage'],
                top_vaccinated_provinces[9]['province_two_dose_percentage'],
             ]
}
least_vaccinated_provinces = {
    "provinces":
                [least_vaccinated_provinces[0]['province_name'],
                least_vaccinated_provinces[1]['province_name'],
                least_vaccinated_provinces[2]['province_name'],
                least_vaccinated_provinces[3]['province_name'],
                least_vaccinated_provinces[4]['province_name'],
                least_vaccinated_provinces[5]['province_name'],
                least_vaccinated_provinces[6]['province_name'],
                least_vaccinated_provinces[7]['province_name'],
                least_vaccinated_provinces[8]['province_name'],
                least_vaccinated_provinces[9]['province_name'],
                ],
    "two_dose_percentage":
                [least_vaccinated_provinces[0]['province_two_dose_percentage'],
                least_vaccinated_provinces[1]['province_two_dose_percentage'],
                least_vaccinated_provinces[2]['province_two_dose_percentage'],
                least_vaccinated_provinces[3]['province_two_dose_percentage'],
                least_vaccinated_provinces[4]['province_two_dose_percentage'],
                least_vaccinated_provinces[5]['province_two_dose_percentage'],
                least_vaccinated_provinces[6]['province_two_dose_percentage'],
                least_vaccinated_provinces[7]['province_two_dose_percentage'],
                least_vaccinated_provinces[8]['province_two_dose_percentage'],
                least_vaccinated_provinces[9]['province_two_dose_percentage'],
             ]
}
df = pd.DataFrame.from_dict(top_vaccinated_provinces)
ax.barh(df.provinces,df.two_dose_percentage)
ax.invert_yaxis()
ax.set_xlabel('Percentage')
for Y,X in enumerate(df.two_dose_percentage):
    ax.annotate(X,xy=(X,Y))
ax.set_title('Top fully vaccinated provinces(Only >18)')
canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
canvas.set_size_request(600, 400)

