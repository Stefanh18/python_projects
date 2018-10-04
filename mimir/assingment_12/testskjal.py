#sort_list() function goes here
def sort_list():
    a_list = []
    integer = input("Enter a integer: ")
    while integer.isdigit():
        a_list.append(integer)
    print(a_list)


sort_list()