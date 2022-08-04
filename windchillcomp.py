from mysci.readdata import read_data
from mysci.printing import print_comparison
from mysci.computation import estimate_windchill

#Column names and column indices
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7, 'windchill': 12}

#Data types for each column (if non-string)
types = {'tempout': float, 'windspeed':float, 'windchill':float}

# Read the data file
data = read_data(columns, types=types)

# Estimate wind chill
windchill = [estimate_windchill(t, v) for t, v in zip(data['tempout'], data['windspeed'])]

# Output comparison of data
print_comparison('WINDCHILL', data['date'], data['time'], data['windchill'], windchill)

