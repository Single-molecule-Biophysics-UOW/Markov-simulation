# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 02:07:19 2022

@author: Stefan H. Mueller

Plot the generated simulation data
"""

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import os

"""
we assume that the simulation results are in a separate folder or are the
only .csv files in the active folder.
"""
files = [x for x in os.listdir() if '.csv' in x]


#%% select files
change_kN = pd.read_csv(files[0])
change_kx = pd.read_csv(files[1])

#%% create and show the plot
fig1, ax = plt.subplots(2,sharex=True)
print(0.1/change_kN['kx'])
ax[0].set_xscale('log')
ax[0].plot(change_kN['kx']/0.1,change_kN['0.1_napp'])
ax[0].plot(change_kN['kx']/0.3,change_kN['0.3_napp'])
ax[0].plot(change_kN['kx']/0.5,change_kN['0.5_napp'])
ax[0].plot(change_kN['kx']/0.7,change_kN['0.7_napp'])

ax[0].set_xlabel('$k_x/k_N$')
ax[0].set_ylabel('$N_{app}$')


ax[1].plot(change_kN['kx']/0.1,change_kN['0.1_kapp'])
ax[1].plot(change_kN['kx']/0.3,change_kN['0.3_kapp'])
ax[1].plot(change_kN['kx']/0.5,change_kN['0.5_kapp'])
ax[1].plot(change_kN['kx']/0.7,change_kN['0.7_kapp'])

ax[1].set_xlabel('$k_x/k_N$')
ax[1].set_ylabel('$k_{app} (k_N)$')

plt.show()

#%% create and show the plot
fig2, ax = plt.subplots(2,sharex=True)
print(0.1/change_kN['kx'])
ax[0].set_xscale('log')
ax[0].plot(change_kx['kN']/0.1,change_kx['0.1_napp'])
ax[0].plot(change_kx['kN']/0.3,change_kx['0.3_napp'])
ax[0].plot(change_kx['kN']/0.5,change_kx['0.5_napp'])
ax[0].plot(change_kx['kN']/0.7,change_kx['0.7_napp'])

ax[0].set_xlabel('$k_x/k_N$')
ax[0].set_ylabel('$N_{app}$')


ax[1].plot(change_kx['kN']/0.1,change_kx['0.1_kapp'])
ax[1].plot(change_kx['kN']/0.3,change_kx['0.3_kapp'])
ax[1].plot(change_kx['kN']/0.5,change_kx['0.5_kapp'])
ax[1].plot(change_kx['kN']/0.7,change_kx['0.7_kapp'])

ax[1].set_xlabel('$k_x/k_N$')
ax[1].set_ylabel('$k_{app} (k_N)$')

plt.show()


#%% save the figure as vector graphic and png
fig2.savefig('change_kx.svg')
fig2.savefig('change_kx.png')

# fig1.savefig('change_kN.svg')
# fig1.savefig('change_kN.png')

