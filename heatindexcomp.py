from readdata import read_data

#Column names and column indices
columns = {'date': 0, 'time': 1, 'tempout': 2, 'humout': 5, 'heatindex': 13}

#Data types for each column (if non-string)
types = {'tempout': float, 'humout':float, 'heatindex':float}

# Read the data file
data = read_data(columns, types=types)

# Compute heat index
def compute_heatindex(t, hum):
    a = -42.379 
    b = 2.04901523
    c = 10.14333127
    d = -0.22475541
    e = -0.00683783
    f = -0.05481717
    g = 0.00122874
    h = 0.00085282
    i = -0.00000199

    rh = hum/100

    hi = (a + (b * t) + (c * rh) + (d * t * rh) + \
        (e * t**2) + (f * rh**2) + (g * t**2 * rh) + \
        (h * t * rh**2) + (i * t**2 * rh**2))

    return hi


heatindex = []
for temp, hum in zip(data['tempout'], data['humout']):
    heatindex.append(compute_heatindex(temp, hum))

# Output comparison of data
print('                      ORIGINAL    ESTIMATED')
print('   DATE      TIME    HEATINDEX    HEATINDEX    DIFFERENCE')
print('-------    ------    ---------    ---------    ----------')

zip_data = zip(data['date'], data['time'], data['heatindex'], heatindex)
for date, time, hi_data, hi_est in zip_data:
    hi_diff = hi_data - hi_est
    print(f'{date}    {time:>6}    {hi_data:9.6f}    {hi_est:9.6f}    {hi_diff:10.6f}')


