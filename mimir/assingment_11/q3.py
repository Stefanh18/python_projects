def get_list():
    a_list = input("Enter elements of list separated by commas: ").strip().split(',')
    return a_list

def even_sum(list_1):
    int_list = [int(x) for x in list_1]
    user_input = [x for x in int_list if x % 2 == 0]
    sum_of_input = sum(user_input)
    return sum_of_input



# Main program starts here - DO NOT change it
a_list = get_list()
print(even_sum(a_list))
