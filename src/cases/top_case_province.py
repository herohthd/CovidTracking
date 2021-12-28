import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
import numpy as np
import pandas as pd
from .case import top_case_provinces,least_case_provinces
# Fixing random state for reproducibility
np.random.seed(19680801)

plt.rcdefaults()
fig,ax = plt.subplots()

top_case_provinces = {
    "provinces":
                [top_case_provinces[0]['province_name'],
                top_case_provinces[1]['province_name'],
                top_case_provinces[2]['province_name'],
                top_case_provinces[3]['province_name'],
                top_case_provinces[4]['province_name'],
                top_case_provinces[5]['province_name'],
                top_case_provinces[6]['province_name'],
                top_case_provinces[7]['province_name'],
                top_case_provinces[8]['province_name'],
                top_case_provinces[9]['province_name'],
                ],
    "case":
                [top_case_provinces[0]['case'],
                top_case_provinces[1]['case'],
                top_case_provinces[2]['case'],
                top_case_provinces[3]['case'],
                top_case_provinces[4]['case'],
                top_case_provinces[5]['case'],
                top_case_provinces[6]['case'],
                top_case_provinces[7]['case'],
                top_case_provinces[8]['case'],
                top_case_provinces[9]['case'],
             ]
}
least_case_provinces = {
    "provinces":
                [least_case_provinces[0]['province_name'],
                least_case_provinces[1]['province_name'],
                least_case_provinces[2]['province_name'],
                least_case_provinces[3]['province_name'],
                least_case_provinces[4]['province_name'],
                least_case_provinces[5]['province_name'],
                least_case_provinces[6]['province_name'],
                least_case_provinces[7]['province_name'],
                least_case_provinces[8]['province_name'],
                least_case_provinces[9]['province_name'],
                ],
    "case":
                [least_case_provinces[0]['case'],
                least_case_provinces[1]['case'],
                least_case_provinces[2]['case'],
                least_case_provinces[3]['case'],
                least_case_provinces[4]['case'],
                least_case_provinces[5]['case'],
                least_case_provinces[6]['case'],
                least_case_provinces[7]['case'],
                least_case_provinces[8]['case'],
                least_case_provinces[9]['case'],
             ]
}
df = pd.DataFrame.from_dict(top_case_provinces)
ax.barh(df.provinces,df.case)
ax.invert_yaxis()
ax.set_xlabel('Number')
for Y,X in enumerate(df.case):
    ax.annotate(X,xy=(X,Y))
ax.set_title('Top infected provinces(Per 100k population)')
top_case_canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
top_case_canvas.set_size_request(700, 500)
