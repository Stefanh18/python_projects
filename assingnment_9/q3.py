with open("words.txt", "r", encoding = "utf-8") as file_content:
    longest = ''
    for line in file_content:
        if len(line) > len(longest):
            longest = line.strip()
print("Longest word is", "'" + longest + "'", "of length", len(longest))



