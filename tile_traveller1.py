# Notandi ert staðsettur á reit 1,1 á x og y ás.
# Notandi velur átt af þeim áttum sem hann á möguleika á því að fara í. Ef valið er átt sem er ekki til kemur invalid input
# reitirnir eru 3x3 og eftirfarandi er ekki hægt
# þegar x er 1 þá er ekki hægt að fara til vinstri
# þegar x er 3 þá er ekki hægt að fara til hægri
# þegar y er 1 er ekki hægt að fara niður 
# þegar y er 3 þá er ekki hægt að fara upp
# ef x = 1 og y er 1 þá er einungis hægt að fara upp
# ef x = 2 og y = 1  þá er einungis hægt að fara upp
# ef x=2 og y = 2 þá er hægt að fara til vinstir eða niður
# ef x= 3, og y = 2 þá er einungis hægt að fara niður og upp.  
# ef notandi nær gildinu x= 3 og y = 1 þá er hann búinn að vinna leikinn

begining = (1,1)
print('You can travel: (N)orth.')

while begining != (3,1):
    if begining == (1,1):
        direction = input('Direction: ')
        if direction == 'n' or direction == 'N':
            begining = (1,2)
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            begining = begining
    if begining == (1,2):
        if direction == 'n' or direction =='N':
            begining = (1,3) 
            print('You can travel: (E)ast or (S)outh.')
            direction = input('Direction: ')
        elif direction == 'E' or direction =='e':
            begining = (2,2)  
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')
        elif direction == 's' or direction =='S':
            begining = (1,1)
            print('You can travel: (N)orth.')
        else:
            print('Not a valid direction!')
            begining = begining
            direction = input('Direction: ')
    if begining == (1,3):
        if direction == 's' or direction == 'S':
            begining = (1,2)
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            direction = input('Direction: ')
        elif direction == 'e' or direction =='E':
            begining = (2,3) 
            print('You can travel: (E)ast or (W)est.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            begining = begining
            direction = input('Direction: ')
    if begining == (2,2):
        if direction == 's' or direction == 'S':
            begining = (2,1)
            print('You can travel: (N)orth.')
            direction = input('Direction: ')
        elif direction == 'w' or direction == 'W':
            begining = (1,2)  
            print('You can travel: (N)orth or (E)ast or (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            begining = begining
            direction = input('Direction: ')
    if begining == (2,1):   
        if direction == 'n' or direction =='N':
            begining = (2,2)  
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')    
        else:
            print('Not a valid direction!')
            begining = begining
            direction = input('Direction: ')
    if begining == (2,3):       
        if direction == 'e' or direction =='E':
            begining = (3,3)  
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')
        elif direction == 'w' or direction =='W':
            begining = (1,3)
            print('You can travel: (E)ast our (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            begining = begining
            direction = input('Direction: ')
    if begining == (3,3): 
        if direction == 'w' or direction =='W':
            begining = (2,3)   
            print('You can travel: (E)ast or (W)est.')
            direction = input('Direction: ')
        elif direction == 's' or direction == 'S':
            begining = (3,2) 
            print('You can travel: (N)orth or (S)outh.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            begining = begining
            direction = input('Direction: ')
    if begining == (3,2):  
        if direction == 's' or direction == 'S':
            begining = (3,1) 
        elif direction == 'n' or direction == 'N':
            begining = (3,3)  
            print('You can travel: (S)outh or (W)est.')
            direction = input('Direction: ')
        else:
            print('Not a valid direction!')
            begining = begining
            direction = input('Direction: ')
    if begining == (3,1):
        print('Victory!')