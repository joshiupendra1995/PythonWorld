List1 = [1, 3, 4, 5]
List2 = [3, 4, 5]
print(List1)
List1.append(8)
List1.append(9)
List1.append(10)
List1.append(11)
List1.remove(11)

print(List1)
Tuple1 = tuple(List1)

for n in Tuple1:
    print(n)
# n=int(input("enter number"))
# for i in range(1,n+1):
#   for j in range(1,i+1):
#       print(j , end=" ")
#
#   print("\r")
