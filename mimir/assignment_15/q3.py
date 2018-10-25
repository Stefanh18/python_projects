import string

def reader(filename):
    with open(filename, 'r') as file_content:
        word_file = []
        for line in file_content:
            new_line = line.strip().split()
            word_file += new_line
    return word_file

def prep_file(w_file):
    """Takes in file, reads lines, splits and strips"""
    word_list = []
    for word in w_file:
        clean_word = word.strip().strip(string.punctuation).lower()
        word_list.append(clean_word)
    return word_list

def make_tuples_list(strip_file):
    tuple_list = []
    for index in range(1, len(strip_file)):
        tuple_list.append((strip_file[index-1], strip_file[index]))
    return tuple_list

def pair_to_count(tuple_list):
    """Strips out each word, make a dictionary, counts how often each word appears and """
    dict_count = {}
    for pair in tuple_list:
        if pair in dict_count:
            dict_count[pair] += 1
        else:
            dict_count[pair] = 1
    return dict_count 

def ten_biggest(pair_list):
    countable = [(val, key) for key, val in pair_list.items()]
    # sort_counted = sorted(countable, reverse=True)
    sort_counted = sorted(countable, reverse=True)
    big_sorted = []
    for i in range(10):
        big_sorted.append(sort_counted[i])
    return big_sorted
    
def reverse_tuple(listi):
    empty = []
    for i in listi:
        empty.append(i[::-1])
    return empty

def main():
    #input file name
    file_name = input("Enter name of file: ")
    # file_name = "lorem.txt"
    #import file
    word_file = reader(file_name)
    #prepare file. lower case, strip punctuations
    strip_file = prep_file(word_file)
    # print(strip_file)
    #tuple (word1, word2)
    tuple_list = make_tuples_list(strip_file)
    # print(tuple_list)
    #make dictionary out of word pairs
    pair_counts = pair_to_count(tuple_list)
    # print(pair_counts)
    #list(set(name of set))
    ten_big = ten_biggest(pair_counts)
    # print(ten_big)
    tuplur = reverse_tuple(ten_big)
    print(tuplur)

main()