my_int = int(input('Give me an int >= 0: '))
empty=''
orig=my_int
while my_int > 0:
        quotient=my_int//2
        remainder=my_int%2
        empty=empty+str(remainder)
        my_int=quotient
else:
    if empty=='':
        empty='0'
    print('The binary of',orig,'is',empty[::-1])