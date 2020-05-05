"""
Make some arrays in numpy and try 5 methods of your choice on them
Have the code save some output to your output directory ([my_code]_output/) as a pickle file, and have it read that file back in.  Have the code make the output directory if needed.
Use argparse to add command-line arguments to your code, allowing the user to make some choice about what happens.
Push your code to github, and then pull it to your account on fjord (in /data1), and try running it there.
"""

#imports
import sys, os
import numpy as np
import pickle
import argparse

def boolean_string(s):
    # this function helps with getting Boolean input
    if s not in ['False', 'True']:
        raise ValueError('Not a valid boolean string')
    return s == 'True' # note use of ==

# create the parser object
parser = argparse.ArgumentParser()

# NOTE: argparse will throw an error if:
#     - a flag is given with no value
#     - the value does not match the type
# and if a flag is not given it will be filled with the default.
parser.add_argument('-a', '--a_string', default='hi', type=str)
parser.add_argument('-b', '--integer_b', default=10, type=int)
parser.add_argument('-c', '--float_c', default=1.5, type=float)
parser.add_argument('-v', '--verbose', default=True, type=boolean_string)
# Note that you assign a short name and a long name to each argument.
# You can use either when you call the program, but you have to use the
# long name when getting the values back from "args".

# get the arguments
args = parser.parse_args()


a = np.array([1,2,3,4,5,6])
size = a.size
amax = np.max(a)
amin = np.min(a)
b = np.reshape(a,[2,3])
f = np.transpose(b)

out_dir = '../../output/effective_computing/'

# save it as a pickle file
out_fn = out_dir + 'pickled_array.p'
pickle.dump(b, open(out_fn, 'wb')) # 'wb' is for write binary

# read the array back in
d = pickle.load(open(out_fn, 'rb')) # 'rb is for read binary

# multiply every element in d by the number you passed

print(args.float_c*d)