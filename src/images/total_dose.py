import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from vaccine import doses
from matplotlib.ticker import EngFormatter



xs = np.array([datetime.strptime(dose['date'], "%b %d, %Y").strftime('%-d/%-m') for dose in doses])
ys = np.array([dose['total_doses'] for dose in doses])
print(xs,ys)

plt.plot(xs, ys)
plt.show()
