""" Create a histogram of words starting by each alphabet letter

The output should look like this:

a  ***************************************** (4172)
b  **************************************(3841)

...

z  **(100)

Where each '*' represents 10 occurrences
"""

words = './data/dict.txt'

fd = open(words, 'r')

words = {}

for line in fd:
    first_letter = line[0]
    # continue the implementation

for w in words:
    if w >= 'a' and w <= 'z':
        freq = words[w]
        # continue the implementation

fd.close()
