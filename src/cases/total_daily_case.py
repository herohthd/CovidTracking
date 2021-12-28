import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, DateFormatter
from matplotlib.figure import Figure
from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
import datetime as dt
import pandas as pd
import numpy as np
from .case import case_by_day
# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig,ax = plt.subplots()

# Format cases
xs = np.array([case['date'] for case in reversed(case_by_day)])
ys = np.array([case['cases'] for case in reversed(case_by_day)])
values = {'date':xs,
          'daily_doses':ys}
df = pd.DataFrame(values)
pd.plotting.register_matplotlib_converters()

# Format the graph
# ax = plt.gca()
ax.set_xlim(pd.Timestamp(df['date'][0]), pd.Timestamp(df['date'][df.index[-1]]))
ax.xaxis.set_major_formatter(DateFormatter('%d/%m'))
# ax.xaxis.set_major_locator(DayLocator(interval=25))

# Hide axis
right_side = ax.spines["right"]
right_side.set_visible(False)
top_side = ax.spines["top"]
top_side.set_visible(False)


ax.bar(xs, ys,color = "#f46669",linewidth=0.3)
ax.set_title('Daily Covid-19 vaccination cases')
plt.gcf().autofmt_xdate()

total_daily_case_canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
total_daily_case_canvas.set_size_request(600, 400)

