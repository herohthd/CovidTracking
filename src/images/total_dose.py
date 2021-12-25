import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, DateFormatter
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_gtk3agg import (
#     FigureCanvasGTK3Agg as FigureCanvas)
import datetime as dt
import pandas as pd
import numpy as np
from pandas.plotting import register_matplotlib_converters
from vaccine import doses

ONE_MILLION = 1e6

# Format doses
xs = np.array([dose['date'] for dose in reversed(doses)])
for dose in reversed(doses):
    dose['total_doses'] = float(dose['total_doses'].replace(",",""))
ys = np.array([dose['total_doses'] for dose in reversed(doses)])


# Assign doses to pandas data frame
values = {'date':xs,
          'total_doses':ys}
df = pd.DataFrame(values)
df['date'] = df['date'].apply(lambda x:
                                    dt.datetime.strptime(x,'%b %d, %Y'))
# df['date'] = pd.to_datetime(df['date'], format='%b %d, %Y', dayfirst=True)
# df = df.set_index("date")
pd.plotting.register_matplotlib_converters()
df[["total_doses"]].plot()
# Format the graph
ax = plt.gca()
# ax.axes.get_yaxis().set_visible(False)
ax.set_xlim(pd.Timestamp(xs[0]), pd.Timestamp(xs[-1]))
ax.xaxis.set_major_formatter(DateFormatter('%d/%m'))
ax.xaxis.set_major_locator(DayLocator(interval=40))

# Hide axis
right_side = ax.spines["right"]
right_side.set_visible(False)
top_side = ax.spines["top"]
top_side.set_visible(False)


plt.plot(df['date'], df['total_doses'],color = "#06692e",linewidth=1)
plt.title('People having received Covid-19 vaccines')
plt.gcf().autofmt_xdate()


#Annotate the last element
local_max = str(round(ys.max()/ONE_MILLION,1)) + 'M'
plt.annotate(local_max, xy=(1, ys.max()), xytext=(8, 0),
                 xycoords=('axes fraction', 'data'), textcoords='offset points')
plt.savefig("total_dose.png", bbox_inches='tight')
plt.show()

