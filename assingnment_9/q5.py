with open("words.txt", "r") as words_file:
    with open("sentences.txt", "w") as sentences_file:
        for line_str in words_file:
            if line_str == "\n":
                print(line_str,file=sentence_file,end="")
                print(line_str, end="")
            else:
                line_str = line_str.strip()
                print(line_str,file=sentence_file,end=" ")
                print(line_str,end=" ")