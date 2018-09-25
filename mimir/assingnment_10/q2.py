
# The main program starts here - DO NOT change it
def to_list(the_string):
    new_string = the_string.replace(",", " ")
    output = new_string.split()
    return output

the_string = input("Enter the string: ")
the_list = to_list(the_string)
print(the_list)