def get_input():
    name = input("Name: ")
    phone_number = input("Number: ")
    return name, phone_number

def add_contact_to_phone_book(phone_book, name, phone_number):
    phone_book[name] = phone_number

def change_dictionary_to_tuple_list(phone_book):
    tuple_list = []
    for name, number in phone_book.items():
        tuple_list.append((name, number))
    return tuple_list

def main():
    choice = "y"
    phone_book = {}
    while choice.lower() == "y":
        # Get input from user
        name, phone_number = get_input()

        # add contact to dictionary
        add_contact_to_phone_book(phone_book, name, phone_number)
        choice = input("More data (y/n)? ")
    phone_book_list = change_dictionary_to_tuple_list(phone_book)
    print(sorted(phone_book_list))

main()
