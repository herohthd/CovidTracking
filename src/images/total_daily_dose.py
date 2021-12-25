import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, DateFormatter
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_gtk3cairo import FigureCanvasGTK3Cairo as FigureCanvas
import datetime as dt
import pandas as pd
import numpy as np
from vaccine import doses


# Format doses
xs = np.array([dose['date'] for dose in reversed(doses)])
for dose in reversed(doses):
    dose['daily_doses'] = float(dose['daily_doses'].replace(",",""))
ys = np.array([dose['daily_doses'] for dose in reversed(doses)])


# Assign doses to pandas data frame
values = {'date':xs,
          'daily_doses':ys}
df = pd.DataFrame(values)
df['date'] = pd.to_datetime(df['date'], format='%b %d, %Y', dayfirst=True)
pd.plotting.register_matplotlib_converters()

# Format the graph
ax = plt.gca()
ax.set_xlim(pd.Timestamp(xs[0]), pd.Timestamp(xs[-1]))
ax.xaxis.set_major_formatter(DateFormatter('%d/%m'))
ax.xaxis.set_major_locator(DayLocator(interval=25))

# Hide axis
right_side = ax.spines["right"]
right_side.set_visible(False)
top_side = ax.spines["top"]
top_side.set_visible(False)


plt.bar(df['date'], df['daily_doses'],color = "#06692e",linewidth=0.3)
plt.title('Daily Covid-19 vaccination doses')
plt.gcf().autofmt_xdate()

plt.savefig("total_daily_dose.png", bbox_inches='tight')
plt.show()
