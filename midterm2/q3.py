def make_sublists(a_list): 
    n = len(a_list)
    for i in range(0,n + 1):
        new_list += a_list[:i]
    return new_list

a_list = input("Enter integers separated with commas: ")
listi = make_sublists(a_list)

print(listi)
# Main program starts here

# This should be the last statement in your main program/function 
#print(sorted(sub_lists))
