size = int(input("Enter the size of the list: "))
asdv = True
while asdv:
    final_list = []
    list1 = input("Enter numbers seperated by comma of the length {}: ".format(size))
    list2 = list1.split(",")
    for x in list2:
        final_list.append(x)
    if len(final_list) == size:
        higest_number = 0
        for x in final_list:
            if x > higest_number:
                x = higest_number
        print(higest_number) 
        asdv = False
    else:
        print("Invalid input")

