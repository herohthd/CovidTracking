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

fig1,ax1 = plt.subplots()

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

df1 = pd.DataFrame.from_dict(least_vaccinated_provinces)
ax1.barh(df1.provinces,df1.two_dose_percentage)
ax1.set_xlabel('Percentage')
for Y,X in enumerate(df1.two_dose_percentage):
    ax1.annotate(X,xy=(X,Y))
ax1.set_title('Least vaccinated provinces (Only 18+)')
canvas1 = FigureCanvas(fig1)  # a Gtk.DrawingArea
canvas1.set_size_request(600, 400)


