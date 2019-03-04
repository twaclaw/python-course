""" Create a histogram of words starting by each alphabet letter

The output should look like this:

a  ***************************************** (4172)
b  **************************************(3841)

...

z  **(100)

Where each '*' represents 10 occurrences
"""

# This file just opens the file, prints all the lines, and closes the file

words = './data/dict.txt'

fd = open(words, 'r')

for line in fd:
    print(line)

fd.close()
