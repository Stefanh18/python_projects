# palindrome function definition goes here
def palidrome(sentence):
    result = ""
    for letter in sentence:
        if letter.isalpha():
            result += letter
    return result.lower()

in_str = input("Enter a string: ")
x = palidrome(in_str)
y = palidrome(in_str)[::-1]
if x == y:
    print('"' + in_str + '"',"is a palindrome.")
else:
    print('"' + in_str + '"',"is not a palindrome.")
# call the function and print out the appropriate message