first = int(input("Initial value: "))
steps = int(input("Steps: "))
sum_of_series = 0
count2 = first
while count2 <= 100:   
    print(count2, end= ' ')
    sum_of_series += count2 
    count2 += steps   
print(" ")
print("Sum of series: ", sum_of_series)
