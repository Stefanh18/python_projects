import random
import string

def get_word_string(filename):
    try:
        with open(filename, "r") as file_content:
            list_1 = []
            for line in file_content:
                line_list = line.strip()
                list_1.append(line_list)
            string = " ".join(list_1)
    except:
        print("File {} not found".format(filename))
    return string
            
def scramble_string(word_string):
    word_list = word_string.split(" ")
    final_string = ""
    for word in word_list:
        new_word = list(word[1:-1])
        first_letter = word[0]
        last_letter = word[-1]
        if word[-1] in string.punctuation:
            last_letter = word[-2:]
            new_word = list(word[1:-2])
        random.shuffle(new_word)
        word_1 = "".join(new_word)
        end_word = first_letter + word_1 + last_letter
        if len(word) == 1:
            end_word = word
        elif len(word) == 2:
            end_word = word
        final_string += end_word + " "
    return final_string

# Main program starts here - DO NOT change it
random.seed(10)
filename = input("Enter name of file: ")
word_string = get_word_string(filename)
scrambled_string = scramble_string(word_string)
print(scrambled_string)