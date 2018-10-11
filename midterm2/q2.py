def is_prime(n):
    '''Returns True if the given positive number is prime and False otherwise'''
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    else:
        return True
      
def sort_list(listi):
    sorted_listi = sorted(listi)
    return sorted_listi

def get_list():
    user_list = input("Enter integers separated with commas: ")
    user_list = user_list.split(",")
    user_list = [int(i) for i in user_list]
    return user_list

def min_max_ave(user_input):
    mini = min(user_input)
    maxi = max(user_input)
    aver = sum(user_input)/len(user_input)
    return mini, maxi, aver

# The main program starts here
try:
    prime_list = []
    user_input = get_list()
    print("Input list:", user_input)
    sorted_list = sort_list(user_input)
    print("Sorted list: ", sorted_list)
    for i in user_input:
        prime = is_prime(i)
        if prime == True and i not in prime_list:
            prime_list.append(i)
    print("Prime list:", sorted(prime_list))
    mini, maxi, aver = min_max_ave(user_input)
    print("Min: {}, Max: {}, Average: {:.2f}".format(mini, maxi, aver))
except:
    print("Incorrect input!")
