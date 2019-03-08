""" Convert csv table to dictionary

Convert the table located in data/energy_countries.csv into a dictionary. 
This table is a modified version of the data available at:

https://data.worldbank.org/indicator/eg.fec.rnew.zs

The format is:
Country name | Country code | 1990 | .... |2015|

Each value is the %-value of the total energy consumption that is produced with renewables.

Use the country code as a key:
Each entrance should have the attributes country_name and then one entrance for each year

'RWA': [80.0875582175947,81.8261168913197,81.5562628296224,81.3324076143306,78.5389768561632,88.3582377902898,89.1548284004775,91.1241958132464,90.8049706032367,90.7614884552462,86.6785245581281,86.8757627735523,87.1082026675283,87.2876198960335,87.5421366193574,89.2446121757129,90.5858527254493,90.3098879135669,90.6305031272287,90.5419268269666,90.6555290837025,89.6448125883995,88.7852909566571,88.474248475437,88.1813037678132,86.6553742907747]

Don't forget to cast the values to floats

If the string is empty add the value None
"""


DATABASE = 'data/energy_countries.csv'

fd = open(DATABASE, 'r')

countries = {}

for line in fd:
    # implement your code here

    # remove the end of line
    new_line = line[:-1]

    # split the line in fields
    fields = new_line.split(',')

    print(fields)

# Don't forget to close the file
fd.close()
