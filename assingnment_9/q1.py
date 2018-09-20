new_str = ""
with open("test.txt", "r", encoding = "utf-8") as file_content:
    for line in file_content:
        line = line.strip()
        new_str += line.replace(" ", "")
print(new_str)



