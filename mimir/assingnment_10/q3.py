# Your functions should appear here

def triple_list(a_list):
    outcome = a_list * 3
    return outcome
def populate_list(a_list):
    new = True
    while new == True:
        user_input = input("Enter value to be added to list: ")
        if user_input.lower() == "exit":
            new = False
        else:
            a_list.append(user_input)
    return user_input

# Main program starts here - DO NOT change it.
initial_list = []
populate_list(initial_list)
new_list = triple_list(initial_list)

for items in new_list:
    print(items)
