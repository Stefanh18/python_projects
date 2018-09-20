my_str = ""
serhljodar = "aeiouyAEIOUY"
end1= "yay"
end2 = "ay"

while my_str != ".":
    my_str = input("Enter a word: ")
    for index, letter in enumerate(my_str):
        serhljodar1 = my_str.find(letter)
        if len(my_str) == 3 and my_str[index] in serhljodar:
            first_part = my_str[ 0 : (serhljodar1)]
            second_part = my_str[1:]
            new_str = second_part + first_part + end2
        elif letter in serhljodar and index != 0:
            first_part = my_str[ 0 : (serhljodar1)]
            second_part = my_str[serhljodar1 : ]
            new_str = second_part + first_part + end2    
        elif my_str[0] in serhljodar:
            new_str = my_str + end1   
        elif index == (len(my_str) - 1) and my_str[-1] not in serhljodar:
            new_str = my_str + end2
        else:
            new_str = my_str
            continue
        if my_str == ".":
            quit
        else:
            print(new_str)
            break
