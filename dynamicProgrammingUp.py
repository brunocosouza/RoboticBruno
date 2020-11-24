<<<<<<< HEAD
# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.
import numpy as np
forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
                
    policy = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
                
    policy2D = [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
    flag = True
    
    while flag:
        flag = False
        #Calcula todos os valores de cada celula
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for orientation in range(4):
                    if x == goal[0] and y == goal[1]:
                        if value[orientation][x][y] > 0:
                            change = True
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                    elif grid[x][y] == 0:
                        for i in range(3):
                            o2 = (orientation + action[i]) % 4
                            x2 = x + forward[o2][0]
                            y2 = y + forward[o2][1]
                            
                            if x2 >= 0 and x2  ...:
                                v2 = value[o2][x2][y2] + cost[i]
                                if v2 < value[orientation][x][y]:
                                    value[orientation][x][y] = v2
                                    policy[orinetation][x][y] = action_name[i]
                                    change = True
                            
                            

    return policy2D

optimum_policy2D(grid,init,goal,cost)
=======
# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.
import numpy as np
forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 20] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------

def optimum_policy2D(grid,init,goal,cost):
    value = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
                
    policy = [[[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))],
                [[999 for row in range(len(grid[0]))] for col in range(len(grid))]]
                
    policy2D = [[999 for row in range(len(grid[0]))] for col in range(len(grid))]
    flag = True
    
    while flag:
        flag = False
        #Calcula todos os valores de cada celula
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for orientation in range(4):
                    if x == goal[0] and y == goal[1]:
                        if value[orientation][x][y] > 0:
                            change = True
                            value[orientation][x][y] = 0
                            policy[orientation][x][y] = '*'
                    elif grid[x][y] == 0:
                        for i in range(3):
                            o2 = (orientation + action[i]) % 4
                            x2 = x + forward[o2][0]
                            y2 = y + forward[o2][1]
                            
                            if x2 >= 0 and x2  ...:
                                v2 = value[o2][x2][y2] + cost[i]
                                if v2 < value[orientation][x][y]:
                                    value[orientation][x][y] = v2
                                    policy[orinetation][x][y] = action_name[i]
                                    change = True
                            
                            

    return policy2D

optimum_policy2D(grid,init,goal,cost)
>>>>>>> d61a01d5ac8986ab997795e019df004d0302c58b
