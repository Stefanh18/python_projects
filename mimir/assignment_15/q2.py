def make_sets_out_of_list(input_1, input_2):
    my_set = set(input_1.split(","))
    my_set_1 = set(input_2.split(","))
    my_set = {int(x) for x in my_set}
    my_set_1 = {int(x) for x in my_set_1}
    return my_set, my_set_1
    
def display_options():
    print("1. Intersection")
    print("2. Union")
    print("3. Difference")
    print("4. Quit")

def options(set_1, set_2):
    user_choice = int(input("Set operation: "))
    if user_choice == 1:
        returning_set = set_1 & set_2
    elif user_choice == 2:
        returning_set = set_1.union(set_2)
    elif user_choice == 3:
        returning_set = set_1 - set_2
    elif user_choice == 4:
        returning_set = False
    return returning_set

def main():
    input_1 = input("Input a list of integers separated with a comma: ")
    input_2 = input("Input a list of integers separated with a comma: ")
    set_1, set_2 = make_sets_out_of_list(input_1, input_2)
    print(set_1)
    print(set_2)
    while True:
        display_options()
        set_to_display = options(set_1, set_2)
        if set_to_display == False:
            break
        print(set_to_display)

main()