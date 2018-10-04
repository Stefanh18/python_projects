#sort_list() function goes here
def sort_list(a_list):
    a_list.sort()

def main():
    #loop to accept integers until a non-digit is entered goes here
    list1 = []
    integer = "1"
    while integer.isdigit():
        integer = input("")
        list1.append(integer)
    list1.pop()
    
    a_list = [int(x) for x in list1]
        
        
    

    ######Do not modify this part######
    print(a_list)
    print(sort_list(a_list))
    print(a_list)
    ######Do not modify this part######
    
main()