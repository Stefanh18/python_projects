# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
# Create a function that takes 3 parameter, the numbers of small bricks, the number of big bricks and the goal length. 
# The function should return True if it is possible to make the goal long row by choosing from the given bricks. 
# This can be done without any loops so don´t use any loops.


def check_bricks(small_bricks, big_bricks, goal):
    if (small_bricks * 1) + (big_bricks * 5) == goal:
        return True
    elif small_bricks > goal:
        return True
    elif small_bricks + (big_bricks * 5) <= goal and goal % 5 == 0:
        return True
    elif (big_bricks * 5) <= goal and goal % 5 == 0:
        return True 
    else:
        return False
