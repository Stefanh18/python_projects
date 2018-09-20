top_num = int(input("Upper number for the range: ")) # Do not change this line

summa = 0
for x in range(1, top_num + 1):
    summa = 0
    for i in range(1,x):
        if x % i == 0:
            summa = summa + i
            i = i + 1
    if summa == x:
        print(x)