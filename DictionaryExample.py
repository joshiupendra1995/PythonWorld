input_string = 'aabbccddeeffg'
dict = {}
for n in input_string:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1

print(dict)