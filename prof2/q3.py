size = int(input("Enter the size of the list: "))
str1 = input("Enter numbers seperated by comma of the length {}: ".format(size))
list2 = str1.split(",")
final_list = []

for x in list2:
    final_list.append(x)
if len(final_list) == size:
    target = input("Enter the target: ")
    if target in final_list:
        str_final = str(final_list)
        final = str_final.count(target)
    print("The target occurs {} times".format(final))
else:
    print("Invalid input")