# for random number generation
from random import randrange

# we will use evolve function
def evolve(Op,state):
    newstate=[]
    for i in range(len(Op)): # for each row
        newstate.append(0)
        for j in range(len(state)): # for each element in state
            newstate[i] = newstate[i] + Op[i][j] * state[j] # summation of pairwise multiplications
    return newstate # return the new probabilistic state

# the initial state
state = [0.5, 0, 0.5, 0]

# probabilistic operator for symbol a
A = [
    [0.5,  0, 0, 0],
    [0.25, 1, 0, 0],
    [0,    0, 1, 0],
    [0.25, 0, 0, 1]
]

# probabilistic operator for symbol b
B = [
    [1, 0, 0,    0],
    [0, 1, 0.25, 0],
    [0, 0, 0.5,  0],
    [0, 0, 0.25, 1]
]

#
# your solution is here
#

length = 40
total = 50
# total = 1000 # we will also test our code for 1000 strings

# we will check 5 cases
# let's use a list 
cases = [0,0,0,0,0]

for i in range(total): # total number of strings
    Na = 0
    Nb = 0
    string = ""
    state = [0.5, 0, 0.5, 0]
    for j in range(length): # generate random string
        if randrange(2) == 0: 
            Na = Na + 1 # new symbol is a
            string = string + "a"
            state = evolve(A,state) # update the probabilistic state by A
        else:
            Nb = Nb + 1 # new symbol is b
            string = string + "b"
            state = evolve(B,state) # update the probabilistic state by B
    # now we have the final state
    p0 = state[0] + state[1] # the probabilities of being in 00 and 01
    p1 = state[2] + state[3] # the probabilities of being in 10 and 11
    print() # print an empty line
    print("(Na-Nb) is",Na-Nb,"and","(p0-p1) is",p0-p1)
    # let's check possible different cases
    
    # start with the case in which both are nonzero
    # then their multiplication is nonzero
    # let's check the sign of their multiplication
    if (Na-Nb) * (p0-p1) < 0: 
        print("they have opposite sign")
        cases[0] = cases[0] + 1
    elif (Na-Nb) * (p0-p1) > 0: 
        print("they have the same sign")
        cases[1] = cases[1] + 1
        
    #  one of them should be zero
    elif (Na-Nb) == 0:
        if (p0-p1) == 0: 
            print("both are zero")
            cases[2] = cases[2] + 1
        else: 
            print("(Na-Nb) is zero, but (p0-p1) is nonzero")
            cases[3] = cases[3] + 1
    elif (p0-p1) == 0: 
        print("(Na-Nb) is nonzero, while (p0-p1) is zero")
        cases[4] = cases[4] + 1
        
# check the case(s) that are observed and the case(s) that are not observed
print() # print an empty line
print(cases)        
