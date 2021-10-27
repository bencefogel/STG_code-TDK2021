import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
from colormap import *


currents = np.array(currents)
#%%
###DATA SHAPE 

dt_norm = 0.1 / 300

#AB
na1 = np.sum(np.abs(currents[0,:])) * dt_norm
cat1 = np.sum(np.abs(currents[1,:])) * dt_norm
cas1 = np.sum(np.abs(currents[2,:]))* dt_norm
a1 = np.sum(np.abs(currents[3,:]))* dt_norm
kca1 = np.sum(np.abs(currents[4,:]))* dt_norm
kd1 = np.sum(np.abs(currents[5,:]))* dt_norm
h1 = np.sum(np.abs(currents[6,:]))* dt_norm
l1 = np.sum(np.abs(currents[7,:]))* dt_norm

glut1 = np.sum(np.abs(currents[8,:]))* dt_norm
chol1 = np.sum(np.abs(currents[9,:]))* dt_norm

#LP
na2 = np.sum(np.abs(currents[10,:]))* dt_norm
cat2 = np.sum(np.abs(currents[11,:]))* dt_norm
cas2 = np.sum(np.abs(currents[12,:]))* dt_norm
a2 = np.sum(np.abs(currents[13,:]))* dt_norm
kca2 = np.sum(np.abs(currents[14,:]))* dt_norm
kd2 = np.sum(np.abs(currents[15,:]))* dt_norm
h2 = np.sum(np.abs(currents[16,:]))* dt_norm
l2 = np.sum(np.abs(currents[17,:]))* dt_norm

glut2 = np.sum(np.abs(currents[18,:]))* dt_norm
chol2 = np.sum(np.abs(currents[19,:]))* dt_norm

#PY

na3 = np.sum(np.abs(currents[20,:]))* dt_norm
cat3 = np.sum(np.abs(currents[21,:]))* dt_norm
cas3 = np.sum(np.abs(currents[22,:]))* dt_norm
a3 = np.sum(np.abs(currents[23,:]))* dt_norm
kca3 = np.sum(np.abs(currents[24,:]))* dt_norm
kd3 = np.sum(np.abs(currents[25,:]))* dt_norm
h3 = np.sum(np.abs(currents[26,:]))* dt_norm
l3 = np.sum(np.abs(currents[27,:]))* dt_norm

glut3 = np.sum(np.abs(currents[28,:]))* dt_norm
chol3 = np.sum(np.abs(currents[29,:]))* dt_norm

#%%
###PLOTTING
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

# y-axis in bold
rc('font', weight='bold')
 
# Values of each group

bars1 = np.array([na1, na2, na3])
bars2 =  np.array([cat1, cat2, cat3])
bars3 =  np.array([cas1, cas2, cas3])
bars4 =  np.array([a1, a2, a3])
bars5 =  np.array([kca1, kca2, kca3])
bars6 =  np.array([kd1, kd2, kd3])
bars7 =  np.array([h1, h2, h3])
bars8 =  np.array([l1, l2, l3])

bars9 =  np.array([glut1, glut2, glut3] )
bars10 =  np.array([chol1, chol2, chol3]) 

# Heights of bars1 + bars2
sbars3 = np.add(bars1, bars2).tolist()
sbars4 = np.add(sbars3, bars3).tolist()
sbars5 = np.add(sbars4, bars4).tolist()
sbars6 = np.add(sbars5, bars5).tolist()
sbars7 = np.add(sbars6, bars6).tolist()
sbars8 = np.add(sbars7, bars7).tolist()

 
# The position of the bars on the x-axis
r = [0,3,6]
r2 = [1,4,7]
 
# Names of group and bar width
names = ['ABPD', 'LP', 'PY']
barWidth = 1
 
cmap = matplotlib.cm.get_cmap('tab10')
fig = plt.figure()
# Create Na bars
plt.bar(r, bars1, color=cmap(0), edgecolor='white', width=barWidth)
# Create k bars, on top of the first ones
plt.bar(r, bars2, bottom=bars1, color=cmap(1), edgecolor='white', width=barWidth)
# Create leak bars (top)
plt.bar(r, bars3, bottom=sbars3, color=cmap(2), edgecolor='white', width=barWidth)

plt.bar(r, bars4, bottom=sbars4, color=cmap(3), edgecolor='white', width=barWidth)

plt.bar(r, bars5, bottom=sbars5, color=cmap(4), edgecolor='white', width=barWidth)

plt.bar(r, bars6, bottom=sbars6, color=cmap(5), edgecolor='white', width=barWidth)

plt.bar(r, bars7, bottom=sbars7, color=cmap(6), edgecolor='white', width=barWidth)

plt.bar(r, bars8, bottom=sbars8, color=cmap(7), edgecolor='white', width=barWidth)

#create second sets of bars
plt.bar(r2, bars9, color=cmap(8), width=barWidth)

plt.bar(r2, bars10, bottom=bars9, color=cmap(9), width=barWidth)

 
# Custom X axis
ticks = [0.5, 3.5, 6.5]
plt.xticks(ticks, names, fontweight='bold')
# plt.xlabel("Synaptic current contributions for model neurons in the STG")
# plt.ylabel("electric current (nA)") 


fig.savefig('STG_curr.pdf')
# Show graphic
plt.show()

















