num = int(input("enter the number"))
factorial = 1
if num < 0:
    print("Negative number doesnt have a factorial")
    exit(1)
if num == 0:
    print("Factorial of 0 is 1")
    exit(1)
for i in range(1, num + 1):
    factorial = factorial * i

print(factorial)
