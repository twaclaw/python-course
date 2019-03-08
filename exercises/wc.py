""" Implement a word counter (wc)

The programm is supposed to be executed like this:

python wc.py file 

The output should be the number of lines of the file
"""

import sys

if len(sys.argv) != 2:
    print("usage {} filename".format(sys.argv[0]))
    sys.exit()

filename = sys.argv[1]
fd = open(filename, 'r')

# Implement your code here

for line in fd:
    # Implement your code here
    print(line)

fd.close()
