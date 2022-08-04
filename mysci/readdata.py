def read_data(columns, types={}, filename="data/wxobs20170821.txt"):
    """
    Read data from CU Boulder Weather Station data file

    Parameters:
        columns: A dictionary of column names mapping to column indices
        types: A dictionary of column names mapping to types to which to 
            convert each data column (otherwise they will be strings)
        filename: The string path pointing to the CU Boulder Weather Station data file
    """
    #Initialize my data variable
    data = {}
    for column in columns:
        data[column] = []

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

    return data
