top_num = int(input("Input a number between 0 and 999: "))

for x in range(0, top_num):
    if x < 10:
        print(x)
    if x > 9 and x < 100:
        if (x // 10) ** 2 + (x % 10) ** 2 == x:
            print(x)
    if x > 99 and x < 1000:
        if (x // 100) ** 3 + ((x % 100) // 10) ** 3 + (x % 10) ** 3 == x:
            print(x)

