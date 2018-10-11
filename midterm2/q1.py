# Function definitions start here
def open_file(filename):
    try:
        with open(filename, "r") as file_content:
            longest_word = ''
            for lines in file_content:
                line = lines.strip()
                if len(line) > len(longest_word):
                    longest_word = line.strip()
        return longest_word
    except:
        return False

def get_longest_word(file_stream):
    longest_word = file_stream
    return longest_word
            
# The main program starts here
filename = input("Enter name of file: ")
file_stream = open_file(filename)
if file_stream:
	longest_word = get_longest_word(file_stream)
	print("Longest word is '{:s}' of length {:d}".format(longest_word, len(longest_word)))
	file_stream.close
else:
	print('File',filename,'not found!')