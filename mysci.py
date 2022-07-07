#Column names and column indices
columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7, 'windchill': 12}

#Data types for each column (if non-string)
types = {'tempout': float, 'windspeed':float, 'windchill':float}


#Initialize my data variable
data = {}
for column in columns:
    data[column] = []

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
    for _ in range(3):
        datafile.readline()

    for line in datafile:
        datum = line.split()
        for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(datum[i])
            data[column].append(value)


def estimate_windchill(t, v):
    wci = t - 0.7 * v
    return wci


windchill = []
for temp, windspeed in zip(data['tempout'], data['windspeed']):
    windchill.append(estimate_windchill(temp, windspeed))

# DEBUG
for wc_data, wc_est in zip(data['windchill'], windchill):
    print(f'{wc_data:.5f}    {wc_est:.5f}    {wc_data - wc_est:.5f}')



