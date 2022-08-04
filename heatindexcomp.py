from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import compute_heatindex

#Column names and column indices
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'heatindex': 13}

#Data types for each column (if non-string)
types = {'tempout': float, 'humout':float, 'heatindex':float}

# Read the data file
data = read_data(columns, types=types)

# Compute heat index
heatindex = [compute_heatindex(t , h) for t, h in zip(data['tempout'], data['humout'])]

# Output comparison of data
print_comparison('HEAT INDX', data['date'], data['time'], data['heatindex'], heatindex)

