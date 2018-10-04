#game_of_eights() function goes here
def game_of_eights(x):
    for index in range(len(x) - 1):
        if x[index] == 8 and x[index + 1] == 8:
            return True
    return False

def main():
    a_list = input("Enter elements of list separated by commas: ").split(',')
    try:
        a_list = [int(n) for n in a_list]
        print(game_of_eights(a_list))
    except:
        print("Error. Please enter only integers. ")
    # remainder of main() goes here

main()