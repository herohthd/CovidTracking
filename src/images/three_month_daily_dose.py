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


plt.rcdefaults()
fig,ax = plt.subplots()
# Format doses
xs = np.array([dose['date'] for dose in reversed(doses)])
ys = np.array([dose['daily_doses'] for dose in reversed(doses)])

values = {'date':xs[-90::],
          'daily_doses':ys[-90::]}
df = pd.DataFrame(values)
pd.plotting.register_matplotlib_converters()

# Format the graph
ax.set_xlim(pd.Timestamp(df['date'][0]), pd.Timestamp(df['date'][89]))
ax.xaxis.set_major_formatter(DateFormatter('%d/%m'))
# ax.xaxis.set_major_locator(DayLocator(interval=25))

# Hide axis
right_side = ax.spines["right"]
right_side.set_visible(False)
top_side = ax.spines["top"]
top_side.set_visible(False)


ax.bar(xs[-90::], ys[-90::],color = "#06692e",linewidth=0.3)
ax.set_title('Daily Covid-19 vaccination doses')
plt.gcf().autofmt_xdate()

three_month_dose_canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
three_month_dose_canvas.set_size_request(600, 400)
