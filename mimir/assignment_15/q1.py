def common_letters_using_list(first_name, last_name):
    common_letter = []
    for chars in last_name:
        if chars in first_name and chars not in common_letter:
            common_letter.append(chars)
    return common_letter

def common_letters_using_sets(first_name, last_name):
    common_letter = set(first_name) & set(last_name)
    return list(common_letter)

def main():
    first_name, last_name = input("Enter name: ").lower().split()  
    common_letter_list = sorted(common_letters_using_list(first_name, last_name))
    common_letter_list_2 = sorted(common_letters_using_sets(first_name, last_name))
    print(common_letter_list)
    print(common_letter_list_2)

main()