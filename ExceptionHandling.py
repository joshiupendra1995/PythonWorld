a = ("a", "b", "c", "d", "e", "f", "g", "h")

# splits from left to right by 2 steps
x = slice(0, len(a), 2)
print(a[x])

# splits from right to left by 2 steps
x = slice(len(a), 0, -2)

print(a[x])
