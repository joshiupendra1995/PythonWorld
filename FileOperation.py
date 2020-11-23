file = open('hello.txt', 'r')
for f in file:
    if 'Make' in f:
        print(f)
