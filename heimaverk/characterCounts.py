# Exercise no. 44 in chapter 4 in the textbook.
# You should output the result in a table, formatted in the following manner:
# The first line contains the word "Upper case", right justified, 15 spaces wide, followed by the count of upper case characters, right justified, 5 spaces wide.
# The second line contains the word "Lower case", right justified, 15 spaces wide, followed by the count of lower case characters, right justified, 5 spaces wide.
# The third line contains the word "Digits", right justified, 15 spaces wide, followed by the count of digits, right justified, 5 spaces wide.
# The fourth line contains the word "Punctuation", right justified, 15 spaces wide, followed by the count of punctuation characters, right justified, 5 spaces wide.
# The input prompt should be: "Enter a sentence. "

sentence = input("Enter a sentence: ")
uppercase = 0
lowercase = 0
digit = 0
punctuation = 0

for index, letter in enumerate(sentence):
    if letter.isupper() == True:
        uppercase += 1
    elif letter.islower() == True:
        lowercase += 1
    elif letter.isdigit() == True:
        digit += 1
    elif letter.isspace() == True:
        continue
    else:
        punctuation += 1
        
print("{:>15}{:>5}".format("Upper case", uppercase))
print("{:>15}{:>5}".format("Lower case", lowercase))
print("{:>15}{:>5}".format("Digits", digit))
print("{:>15}{:>5}".format("Punctuation", punctuation))