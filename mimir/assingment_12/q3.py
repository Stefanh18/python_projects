#build_wordlist() function goes here
def build_wordlist(infile):
    finale_str = ""
    for line in infile:
        finale_str += line
    finale_str = finale_str.replace("\n", " ")
    finale_list = finale_str.split(" ")
    return finale_list

#find_unique() function goes here
def find_unique(word_list):
    dori_list = []
    for x in word_list:
        if x not in dori_list:
            dori_list.append(x)
    return dori_list

def main():
    infile = open("test.txt", 'r')
    word_list = build_wordlist(infile)  
    infile.close()  
    new_wordlist = find_unique(word_list)
    new_wordlist.sort()
    print(new_wordlist)

main()