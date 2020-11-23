from _collections import OrderedDict

# print("Before:\n")
# od = OrderedDict()
# od['a'] = 1
# od['b'] = 2
# od['c'] = 3
# od['d'] = 4
# for key, value in od.items():
#     print(key, value)
#
# print("\nAfter:\n")
# od['c'] = 5
# for key, value in od.items():
#     print(key, value)

input_string = 'aabbccddef'
ordered_dict = OrderedDict()

for input in input_string:
    keys = ordered_dict.keys()
    if input not in keys:
        ordered_dict[input] = 1
    else:
        ordered_dict[input] += 1
out_string = ""
for key, value in ordered_dict.items():
    out_string = out_string + str(key) + str(value)

print(out_string)
