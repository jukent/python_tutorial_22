≈#Column names and column indices
columns = {'date': 0, 'time': 1, 'tempout': 2}

#Data types for each column (if non-string)
types = {'tempout': float}


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
