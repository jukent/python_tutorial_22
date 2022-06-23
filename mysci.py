#Initialize my data variable
data = {'date':[],
    'time':[],
    'tempout':[]} #list[0] vs dict['key'] --> data['tempout']

# Read the data file
filename = "data/wxobs20170821.txt"

with open(filename, 'r') as datafile:
    for _ in range(3):
        datafile.readline()

    for line in datafile:
        datum = line.split()
        data['date'].append(datum[0])
        data['time'].append(datum[1])
        data['tempout'].append(float(datum[2]))


