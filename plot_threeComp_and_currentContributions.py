# Preliminaries and Modules
import numpy as np
from scipy.integrate import odeint
from integrate_and_getCurrents_threeComp import *
from currents_visualization_threeComp import *






#specify the path to initial conditions and paramters files

pathtocis= './parameters-and-initial-conditions/initial-conditions.txt'

#pathtoparameters ='./parameters-and-initial-conditions/AB_PD1.txt'
#pathtoparameters ='./parameters-and-initial-conditions/AB_PD2.txt'
#pathtoparameters_PD ='./parameters-and-initial-conditions/AB_PD3.txt'


#pathtoparameters_LP ='./parameters-and-initial-conditions/LP2.txt'
#pathtoparameters ='./parameters-and-initial-conditions/LP5.txt'

#pathtoparameters ='./parameters-and-initial-conditions/PY3.txt'
#pathtoparameters ='./parameters-and-initial-conditions/PY4.txt'


#pathtoparameters ='./parameters-and-initial-conditions/AB3_LP4_PY1.txt'     #e
#pathtoparameters ='./parameters-and-initial-conditions/AB1_LP4_PY6.txt'
#pathtoparameters ='./parameters-and-initial-conditions/AB4_LP2_PY1.txt'    #j 
#pathtoparameters ='./parameters-and-initial-conditions/AB1_LP3_PY6.txt' 
#pathtoparameters ='./parameters-and-initial-conditions/AB1_LP3_PY1.txt'   #a
#pathtoparameters ='./parameters-and-initial-conditions/AB2_LP3_PY1.txt'  #a2
pathtoparameters ='./parameters-and-initial-conditions/AB5_LP4_PY5.txt'   #b



#load initialconditions and parameters

y0=genfromtxt(pathtocis)
parameters = genfromtxt(pathtoparameters)


#define temperature (set to 10 C) 
temp=10

#define integration interval and temporal resolution 
t0 = 0
tf = 3000 # 10 second duration (10000 msec)
dt = 0.1 #0.1
t = np.arange(t0, tf, dt)

#integration is performed using odeint, a built-in python package to integrate Ordinary Differential Equations

fullsolution =  odeint(variables, y0, t , args=(parameters,temp))


#plot the membrane potential of ABPD3
#%%
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3)
fig.tight_layout()
#fig.suptitle()
axs[0].plot(t,fullsolution[:,0] )
axs[1].plot(t, fullsolution[:,13])
axs[2].plot(t, fullsolution[:,26])
#axs[2].plot(t, fullsolution[:,39]*20-80)
#axs[2].plot(t, fullsolution[:,40]*20-80)
#axs[2].plot(t, fullsolution[:,43]*20-80)
#fig.savefig('Fig5_b.pdf')

xlabel('time [msec]') 
ylabel('V [mV]')
#%%
#define voltage and currents for currentscape plotting 

voltage = fullsolution[:,(0,13,26)]

currents = variables(fullsolution,0,parameters,temp,onlyDerivate=False)

# #plot currentscape (full temporal range)
# fig_AB = plotCurrentscape(voltage[:,0], currents[0:10])
# fig_LP = plotCurrentscape(voltage[:,1], currents[10:20])
# fig_PY = plotCurrentscape(voltage[:,2], currents[20:30])
# #fig.savefig('Fig5_b.pdf')
#%%
# #show the figures
#fig.savefig('j_copy.pdf')

#Current contribution calculations 

import pandas as pd
currents_AB = abs(np.vstack(currents[0:10]))
fullCurr_AB = sum(currents_AB[:,3990:18092])
intCurr_AB = sum(currents_AB[0:8,3990:18092]) / fullCurr_AB
synCurr_AB = sum(currents_AB[8,3990:18092]) / fullCurr_AB
glutCurr_AB = 1   #AB/PD neuron only receives glutamatergic input
iNa_AB =  sum(currents_AB[0,3990:18092]) / (sum(currents_AB[0:8,3990:18092]) )
iCaT_AB = sum(currents_AB[1,3990:18092]) / (sum(currents_AB[0:8,3990:18092]) )
iCaS_AB = sum(currents_AB[2,3990:18092]) / (sum(currents_AB[0:8,3990:18092]) )
iA_AB = sum(currents_AB[3,3990:18092]) / (sum(currents_AB[0:8,3990:18092]) )
iKCa_AB = sum(currents_AB[4,3990:18092]) / (sum(currents_AB[0:8,3990:18092]) )
iKd_AB = sum(currents_AB[5,3990:18092]) / (sum(currents_AB[0:8,3990:18092]) )
iH_AB = sum(currents_AB[6,3990:18092]) / (sum(currents_AB[0:8,3990:18092]) )
iL_AB = sum(currents_AB[7,3990:18092]) / (sum(currents_AB[0:8,3990:18092]) )



currents_LP = abs(np.vstack(currents[10:20]))
fullCurr_LP = sum(currents_LP[:,3990:18092])
intCurr_LP = sum(currents_LP[0:8,3990:18092]) / fullCurr_LP
synCurr_LP = sum(currents_LP[8:10,3990:18092]) / fullCurr_LP
glutCurr_LP = sum(currents_LP[8,3990:18092]) / sum(currents_LP[8:10,3990:18092])
cholCurr_LP = sum(currents_LP[9,3990:18092]) / sum(currents_LP[8:10,3990:18092])
iNa_LP =  sum(currents_LP[0,3990:18092]) / (sum(currents_LP[0:8,3990:18092]) )
iCaT_LP = sum(currents_LP[1,3990:18092]) / (sum(currents_LP[0:8,3990:18092]) )
iCaS_LP = sum(currents_LP[2,3990:18092]) / (sum(currents_LP[0:8,3990:18092]) )
iA_LP = sum(currents_LP[3,3990:18092]) / (sum(currents_LP[0:8,3990:18092]) )
iKCa_LP = sum(currents_LP[4,3990:18092]) / (sum(currents_LP[0:8,3990:18092]) )
iKd_LP = sum(currents_LP[5,3990:18092]) / (sum(currents_LP[0:8,3990:18092]) )
iH_LP = sum(currents_LP[6,3990:18092]) / (sum(currents_LP[0:8,3990:18092]) )
iL_LP = sum(currents_LP[7,3990:18092]) / (sum(currents_LP[0:8,3990:18092]) )



currents_PY = abs(np.vstack(currents[20:30]))
fullCurr_PY = sum(currents_PY[:,3990:18092])
intCurr_PY = sum(currents_PY[0:8,3990:18092]) / fullCurr_PY
synCurr_PY = sum(currents_PY[8:10,3990:18092]) / fullCurr_PY
glutCurr_PY = sum(currents_PY[8,3990:18092]) / sum(currents_PY[8:10,3990:18092])
cholCurr_PY = sum(currents_PY[9,3990:18092]) / sum(currents_PY[8:10,3990:18092])
iNa_PY =  sum(currents_PY[0,3990:18092]) / (sum(currents_PY[0:8,3990:18092]) )
iCaT_PY = sum(currents_PY[1,3990:18092]) / (sum(currents_PY[0:8,3990:18092]) )
iCaS_PY = sum(currents_PY[2,3990:18092]) / (sum(currents_PY[0:8,3990:18092]) )
iA_PY = sum(currents_PY[3,3990:18092]) / (sum(currents_PY[0:8,3990:18092]) )
iKCa_PY = sum(currents_PY[4,3990:18092]) / (sum(currents_PY[0:8,3990:18092]) )
iKd_PY = sum(currents_PY[5,3990:18092]) / (sum(currents_PY[0:8,3990:18092]) )
iH_PY = sum(currents_PY[6,3990:18092]) / (sum(currents_PY[0:8,3990:18092]) )
iL_PY = sum(currents_PY[7,3990:18092]) / (sum(currents_PY[0:8,3990:18092]) )


#Intrinsic v. Synaptic
data_currents = {'Intrinsic': [intCurr_AB, intCurr_LP, intCurr_PY],
        'Synaptic': [synCurr_AB,synCurr_LP,synCurr_PY]
        }

df_currents = pd.DataFrame(data_currents, columns = ['Intrinsic','Synaptic'], index=['AB', 'LP', 'PY'])

print (df_currents)
df_currents.plot.bar()


#glut/chol v. synaptic
data_synaptic = {'Glutamatergic': [glutCurr_AB, glutCurr_LP, glutCurr_PY],
        'Cholinergic': [0, cholCurr_LP, cholCurr_PY]
        }

df_synaptic = pd.DataFrame(data_synaptic, columns = ['Glutamatergic','Cholinergic'], index=['AB', 'LP', 'PY'])

print (df_synaptic)
df_synaptic.plot.bar(color=[(0.7372549019607844, 0.7411764705882353, 0.13333333333333333, 1.0),(0.09019607843137255, 0.7450980392156863, 0.8117647058823529, 1.0)])

#%%
#intrinsic currents
data_intrinsic = {'iNA': [iNa_AB, iNa_LP, iNa_PY],
                  'iCaT': [iCaT_AB, iCaT_LP, iCaT_PY],
                  'iCaS': [iCaS_AB, iCaS_LP, iCaS_PY],
                  'iA': [iA_AB, iA_LP, iA_PY],
                  'iKCa': [iKCa_AB, iKCa_LP, iKCa_PY],
                  'iKd': [iKd_AB, iKd_LP, iKd_PY],
                  'iH': [iH_AB, iH_LP, iH_PY],
                  'iL': [iL_AB, iL_LP, iL_PY]
        }

df_intrinsic = pd.DataFrame(data_intrinsic, columns = ['iNa','iCaT','iCaS','iA','iKCa','iKD','iH','iL'], index=['AB', 'LP', 'PY'])

print (df_intrinsic)
intrinsic_a = df_intrinsic.plot.bar()
savefig('intrinsic_b.pdf')
show()

