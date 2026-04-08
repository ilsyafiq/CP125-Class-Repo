import pandas as pd


def high_performers(filename):
    df = pd.read_csv(filename)
    names_set = set(df.loc[(df.Math>85) & (df.Science>85) & (df.English>85) & (df.Physics>85) & (df.Chemistry>85), 'Name'])
    result = {
        'count':len(names_set),
        'names': names_set
    }
    return result
high_performers('labs/lab09/data/students.csv')
