def file_csv(filename,number_of_column):
    with open(filename, "r") as file_content:
        listi = []
        for i in file_content:
            new_list = i.split(",")
            listi.append(new_list[number_of_column])
    return listi

def calculation(listi):
    sjukd = listi.pop(0)
    for index,ind in enumerate(listi):  
        ind = ind.replace("%","")
        listi[index] = float(ind)      
    return listi, sjukd

def min_max(listi):
    mini = min(listi)
    find_indexmin = listi.index(mini)
    maxi = max(listi)
    find_indexmaxi = listi.index(maxi)
    return mini,maxi,find_indexmin,find_indexmaxi

def states(filename,value,indexmax,indexmin):
    defult = file_csv(filename,0)
    defult.pop(0)
    statemax = defult[indexmax]
    statemin = defult[indexmin]
    return statemax, statemin

def main(filename):
    file_csv(filename,0)
    print("{:<33}{:<21}{:>15}".format("Indicator", "Min", "Max"))
    print("-" * 87)
    colums = (1,5,7,11,13)
    for i in colums:
        column_list = file_csv(filename,i)
        modified,sjukd = calculation(column_list)
        mini,maxi,find_indexmin,find_indexmaxi = min_max(modified)
        statemax,statemin = states(filename,i,find_indexmaxi,find_indexmin)
        print("{:<33}{:<21}{:>6.1f}{:6}{:<15}{:>6.1f}".format(sjukd + ":", statemin, mini, " ", statemax, maxi))

filename = input("Enter filename containing csv data: ")
try:    
    main(filename)
except:  
    print("Cannot find file", filename) 
    print("{:<33}{:<21}{:>15}".format("Indicator", "Min", "Max"))
    print("-" * 87)


