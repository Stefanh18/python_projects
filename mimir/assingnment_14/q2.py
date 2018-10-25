import string 

def get_word_list(x):
    list_1 = []
    for line in x:
        line = line.lower()
        words = line.split()
        for word in words:
            word = word.strip(string.punctuation)
            list_1.append(word) 
    return list_1
    
def word_list_to_counts(list_1):
    dic = {}
    for word in list_1:
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1
    return dic

def dict_to_tuple(a_dict):
    list_1=[]
    for key,val in a_dict.items():
        a_tuple=(key,val)
        list_1.append(a_tuple)
    return list_1

def main():
    filename = input("Name of file: ")
    # Get a file pointer
    fpointer = open(filename)
    # Get a list of words from the file
    word_list = get_word_list(fpointer) 
    # Transform the list to a dictionary of word-count pairs
    word_count_dict = word_list_to_counts(word_list) 
    # Finally, makes a list of tuples from the dictionary
    word_count_tuples = dict_to_tuple(word_count_dict)
    print(sorted(word_count_tuples))
    
main()