from random import randrange

# let's pick a random number between {0,1,...,99}
# it is expected to be less than 60 with probability 0.6
#     and greater than or equal to 60 with probability 0.4

for experiment in [100,1000,10000,100000]:
    heads = tails = 0
    for i in range(experiment):
        if randrange(100) <60: heads = heads + 1 # with probability 0.6
        else: tails = tails + 1 # with probability 0.4
    print("experiment:",experiment)        
    print("the ratio of #heads/#tails is",(heads/tails),"heads =",heads,"tails = ",tails)
    print() # empty line
