def merge_lists(list1, list2):
    finale_list = []
    for x in list1 + list2:
        if not x in finale_list:
            finale_list.append(x)
    finale_list.sort()
    return finale_list
# Main program starts here - DO NOT change it
list1 = input("Enter elements of list separated by commas: ").split(',')
list2 = input("Enter elements of list separated by commas: ").split(',')
print(merge_lists(list1, list2))
