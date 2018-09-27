def get_emails():
    list_of_email = []
    email = "x"
    while email.lower() != "q":
        email = input("Email address: ")
        list_of_email.append(email)
        if email == "q":
            list_of_email.pop()
    return list_of_email

def get_names_and_domains(email_list):
    new_list = [tuple(x.split("@")) for x in email_list]
    return new_list



# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)