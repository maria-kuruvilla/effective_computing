"""
Code to test input and (filtered) output of a text file.
"""
i=0
# imports
import sys, os
sys.path.append(os.path.abspath('shared'))
import my_module as mymod
import matplotlib.pyplot as plt

myplace = 'maria' # *** YOU NEED TO EDIT THIS ***

# input directory
in_dir = '../' + myplace + '_data/'

# make sure the output directory exists
out_dir = '../' + myplace + '_output/'
mymod.make_dir(out_dir)

# define the input filename
in_fn = in_dir + '2017-01-0118.ctd'
# this is some Canadian CTD data, formatted in a strict but
# difficult-to-use way

# define the output filename
out_fn = out_dir + 'out_test.txt'

# open the output file for writing
outfile = open(out_fn, 'w')
depthlist =[]
templist =[]
with open(in_fn, 'r', errors='ignore') as f:
	for line in f:
		if i < 571:
			i = i+1
		if i >= 571:
			#import pdb; pdb.set_trace() #usefull for debuging, stops code at location and then you can step through and check variables 
			LS = line.split() # .split() makes a list out of the separate items in line
			depthlist.append(-float(LS[1]))
			templist.append(float(LS[2]))
			#depth = float(depthlist)
			#temp = float(templist)
			#print(line)
			i = i+1

fig, ax = plt.subplots()
ax.scatter(templist, depthlist)
a = out_dir+'/out_test_1.png'
fig.savefig(a)

# close the output file
outfile.close()