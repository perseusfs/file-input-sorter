with open("input_file.txt", "r") as file:
    input_list = file.readlines()
    input_list = [x.strip() for x in input_list]
print(*input_list)
number_list = input_list
length = len(number_list)
for i in range(length):
    for j in range(i+1, length):
        if float(number_list[i]) > float(number_list[j]):
            number_list[i], number_list[j] = number_list[j], number_list[i]

print(*number_list)

f = open("output_file.txt", "w")
for line in number_list:
    f.write(line)
    f.write("\n")
f.close()