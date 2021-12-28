import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, DateFormatter
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
import datetime as dt
import pandas as pd
import numpy as np
from .vaccine import doses

# Fixing random state for reproducibility
np.random.seed(19680801)
ONE_MILLION = 1e6

plt.rcdefaults()
fig,ax = plt.subplots()
# Format doses
xs = np.array([dose['date'] for dose in reversed(doses)])
for dose in reversed(doses):
    dose['total_doses'] = float(dose['total_doses'].replace(",",""))
ys = np.array([dose['total_doses'] for dose in reversed(doses)])
values = {'date':xs,
          'total_doses':ys}
df = pd.DataFrame(values)
pd.plotting.register_matplotlib_converters()

# Format the graph
ax.set_xlim(pd.Timestamp(df['date'][0]), pd.Timestamp(df['date'][df.index[-1]]))
ax.xaxis.set_major_formatter(DateFormatter('%d/%m'))
# ax.xaxis.set_major_locator(DayLocator(interval=25))

# Hide axis
right_side = ax.spines["right"]
right_side.set_visible(False)
top_side = ax.spines["top"]
top_side.set_visible(False)


ax.bar(xs, ys,color = "#06692e",linewidth=0.3)
ax.set_title('total Covid-19 vaccination doses')
plt.gcf().autofmt_xdate()

# total_total_dose_canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
# total_total_dose_canvas.set_size_request(600, 400)


#Annotate the last element
local_max = str(round(ys.max()/ONE_MILLION,1)) + 'M'
plt.annotate(local_max, xy=(1, ys.max()), xytext=(8, 0),
                 xycoords=('axes fraction', 'data'), textcoords='offset points')

total_dose_canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
total_dose_canvas.set_size_request(700, 500)
