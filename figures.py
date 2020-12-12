"""
Code to plot average nearest neighbor distance between fish in a school as a function of group size - one line per water temperature. 
"""

# imports
import sys, os
import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import cm



in_dir1 = '../../output/temp_collective/roi/annd.p'

annd_values = pickle.load(open(in_dir1, 'rb')) # 'rb is for read binary

in_dir2 = '../../output/temp_collective/roi/annd_std.p'

out_dir = '../../output/temp_collective/roi_figures/annd.png'

std_annd_values = pickle.load(open(in_dir2, 'rb')) # 'rb is for read binary

temperature = [29,25,21,17,13,9]
group = [1,2,4,8,16]
x = 5
#Plotting
lw=1.25
fs=14
colors = plt.cm.viridis_r(np.linspace(0,1,6))
plt.close('all') # always start by cleaning up
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(211)
for i in range(6):
    ax.plot(group[0:x], annd_values[i,0:x], label = str(temperature[i])+ r'$^{\circ}$C', linewidth = lw, color = colors[i])
    ax.fill_between(group[0:x], annd_values[i,0:x] - std_annd_values[i,0:x],  annd_values[i,0:x] + std_annd_values[i,0:x], alpha = 0.3, color = colors[i])

plt.xlabel('Group Size', size = 0.9*fs)
plt.ylabel('ANND (Body Length)', size = 0.9*fs)
ax.tick_params(labelsize=.8*fs)
ax.set_title('a)', loc='left', fontsize = fs)
plt.legend(fontsize=fs, loc='upper right', title = 'Water Temperature')

x=6
colors = plt.cm.viridis(np.linspace(0,1,5))
ax = fig.add_subplot(212)
for i in range(1,5):
    ax.plot(temperature[0:x], annd_values[0:x,i], label = str(group[i]), linewidth = lw, color = colors[i])
    ax.fill_between(temperature[0:x], annd_values[0:x,i] - std_annd_values[0:x,i],  annd_values[0:x,i] + std_annd_values[0:x,i], alpha = 0.3, color = colors[i])

plt.xlabel('Temperature '+r'($^{\circ}$C)', size = 0.9*fs)
plt.locator_params(axis='x', nbins=5)
plt.ylabel('ANND (Body Length)', size = 0.9*fs)
ax.tick_params(labelsize=.8*fs)
ax.set_title('b)', loc='left', fontsize = fs)
plt.legend(fontsize=fs, loc='upper right', title = 'Group Size')



fig.suptitle('Average Nearest Neighbor Distance (ANND)', size = 1.5*fs)

fig.savefig(out_dir)

plt.show()