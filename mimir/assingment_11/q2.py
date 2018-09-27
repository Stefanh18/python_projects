#list_to_tuple function goes here
def list_to_tuple(user_input):
    try:
        user_list = [int(i) for i in user_input]
        user_input = tuple(user_list)
    except:
        print("Error. Please enter only integers.")
        user_input = ()
    return user_input

# Main program starts here - DO NOT change it
a_list = input("Enter elements of list separated by commas: ").strip().split(',')
a_tuple = list_to_tuple(a_list)
print(a_tuple)