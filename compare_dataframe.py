import pandas as pd

df = pd.read_csv('nba_all.csv')
list1 = df.values.tolist()
list2 = df.values.tolist()

count = 0
for f, b in zip(list1, list2):
    if f[1] == b[1]:
        count = count + 1

print(count)
