def menu_selection():
    print('Menu:')
    choice = input('add(a), remove(r), find(f): ')
    return choice

def execute_selection(choice, a_dict):   
    if choice == 'a':
        key = input('Key: ')
        value = input('Value: ')
        if key in a_dict:
            print('Error. Key already exists.')
        else:
            a_dict[key]=value
    elif choice == 'r':
        key = input('key to remove: ')
        if key not in a_dict:
            print('No such key exists in the dictionary.')
        else:
            del a_dict[key]
    elif choice == 'f':
        key = input('Key to locate: ')
        if key not in a_dict:
            print('Key not found.')
        else:
            value = a_dict[key]
            print ("Value: ", value)

def dict_to_tuples(a_dict):
    dictlist = []
    for key,value in a_dict.items():
        a_tuple = (key, value)
        dictlist.append(a_tuple)
    return dictlist
        
# Do not change this main function
def main():
    more = True
    a_dict = {}
    
    while more:      
        choice = menu_selection()
        execute_selection(choice, a_dict)
        again = input("More (y/n)? ")
        more = again.lower() == 'y'
    
    dictlist = dict_to_tuples(a_dict)
    print(sorted(dictlist))

main()