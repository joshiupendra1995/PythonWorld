file_obj = open("D:\squares.txt", "w")

for number in range(13):
    square = number * number
    file_obj.write(str(square) + "\n")

file_obj.close()

new_f_obj = open("D:\squares.txt", "r")
print(new_f_obj.read()[:14])
new_f_obj.close()

