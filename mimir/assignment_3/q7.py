hole = 1

while hole < 19:
    
    hole = str(hole)
    par_str = "Par of hole " + hole + ": "
    par = input(par_str)

    score_str = "score of hole " + hole + ": "
    score= input(score_str)
    
    print("Par of hole ",hole,par,": " , score )
    hole = int(hole)
    hole += 1
    
    score=int(score)
    par= int(par)

    if score <  par - 3:
        print("invalid score")
    elif score + 3 == par:
        print("albatross")
    elif score + 2 == par:
        print("eagle")
    elif score + 1 == par:
        print("birdie")
    elif score == par + 1:
        print("bogey")
    elif score == par + 2:
        print("double bogey")
    elif score == par + 3:
        print("triple bogey")
    elif score > par + 3:
        print("bad hole")

