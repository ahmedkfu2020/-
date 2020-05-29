# we randomly create a probabilistic state
#
# we should be careful about two things:
#     1. a probability value must be between 0 and 1
#     2. the total probability must be 1
#


# we use a list of size 4
# initial values are zeros
my_state = [0,0,0,0]
normalization_factor = 0 # this will be the summation of four values

# we pick for random values between 0 and 100
from random import randrange
while normalization_factor==0: # the normalization factor cannot be zero
    for i in range(4):
        my_state[i] = randrange(101) # pick a random value between 0 and (101-1)
        normalization_factor += my_state[i]
                
print("the random values before the normalization",my_state)

# normalize each value
for i in range(4): my_state[i] = my_state[i]/normalization_factor
    
print("the random values after the normalization",my_state)  

#  find their summation
sum = 0
for i in range(4): sum += my_state[i]

print("the summation is",sum)
