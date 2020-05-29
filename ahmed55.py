def linear_evolve(operator,state):
    newstate=[]
    for i in range(len(operator)): # for each row
        # we calculate the corresponding entry of the new state
        newstate.append(0) # we set this value to 0 for the initialization
        for j in range(len(state)): # for each element in state
            newstate[i] = newstate[i] + operator[i][j] * state[j] # summation of pairwise multiplications
    return newstate # return the new probabilistic state
# test the function

# operator for the test
B = [
    [0.4,0.6,0],
    [0.2,0.1,0.7],
    [0.4,0.3,0.3]
]

# state for test
v = [0.1,0.3,0.6]

newstate = linear_evolve(B,v)
print(newstate)

for step in [5,10,20,40]:
    new_state = [0.1,0.3,0.6] # initial state
    for i in range(step):
        new_state = linear_evolve(B,new_state)
    print(new_state)
    
# change the initial state

for step in [5,10,20,40]:
    new_state = [1,0,0] # initial state
    for i in range(step):
        new_state = linear_evolve(B,new_state)
    print(new_state)
