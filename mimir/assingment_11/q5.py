def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def get_integer(prompt):
    val = int(input(prompt))
    return val

def transform(list1, list2, index1, index2):
    
    temp_list = []
    for x in range(index1,index2):
        temp_list.append(list1[x])

    for x in temp_list:
        list1.remove(x)
    temp_list.reverse()

    list2 += temp_list
    
# Main program starts here - DO NOT change it
list1 = get_list()
list2 = get_list()
index1 = get_integer("Enter from value: ")
index2 = get_integer("Enter to value: ")
transform(list1, list2, index1, index2)
print(list1)
print(list2)


