# Given a string of any length named s.
# Extract and then print the first and last characters of the string (with one space between them).
# For example, given s = 'abcdef'
# the output will be
# a f

s = input("Input a string: ")

first_last = s[0] + " " + s[-1]

print(first_last)