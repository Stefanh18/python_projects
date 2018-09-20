my_int = int(input('Give me an int >= 0: '))
deili = my_int
bstr = ''
while my_int > 0:
    quotient = my_int // 2
    afgangur = my_int % 2
    bstr = bstr + str(afgangur)
    my_int = quotient
else:
    if bstr == '':
        bstr = '0'

print("The binary of", deili, "is", bstr[::-1])
