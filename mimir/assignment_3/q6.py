counter = 10
while 10 <= counter and 31 >= counter:
    counter2 = counter**2 % 100
    if counter2 == counter:
        print(counter)
    counter += 1