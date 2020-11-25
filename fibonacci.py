num = int(input("Enter the number"))

fib0 = 0
fib1 = 1
fib2 = 0
for i in range(1,num+1):
    fib2 = fib0 + fib1 # fib2=3
    fib0 = fib1  # fib0=2
    fib1 = fib2  # fib1=3
    print(fib2)  # 1 2 3


