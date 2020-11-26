import os
import re

directory = 'D:/input'
matchExp = 'uj'
for i in os.listdir(directory):
    file = open(os.path.join(directory, i))
    line = file.readline()
    if re.search(matchExp, line):
        print(line)
