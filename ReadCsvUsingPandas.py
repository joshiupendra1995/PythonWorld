import pandas as pd

EXPECTED_HEADER = ['id', 'name', 'salary']
header = list(pd.read_csv("data.csv").columns)
if EXPECTED_HEADER == header:
    print("lists are equal")
else:
    print("not equal")
