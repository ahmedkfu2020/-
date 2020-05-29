#
# OUR SOLUTION
#

# initial case
# We assume that the probability of having head is 1 at the beginning,
#    because Asja will start with one euro.
prob_head = 1
prob_tail = 0


#
# first coin-flip
#

# the new probability of head is calculated by using the first row 
new_prob_head = prob_head * 0.6 + prob_tail * 0.3

# the new probability of tail is calculated by using the second row 
new_prob_tail = prob_head * 0.4 + prob_tail * 0.7

# update the probabilities
prob_head = new_prob_head
prob_tail = new_prob_tail

#
# second coin-flip
#
# we do the same calculations

new_prob_head = prob_head * 0.6 + prob_tail * 0.3
new_prob_tail = prob_head * 0.4 + prob_tail * 0.7

prob_head = new_prob_head
prob_tail = new_prob_tail

#
# third coin-flip
#
# we do the same calculations

new_prob_head = prob_head * 0.6 + prob_tail * 0.3
new_prob_tail = prob_head * 0.4 + prob_tail * 0.7

prob_head = new_prob_head
prob_tail = new_prob_tail

# print prob_head and prob_tail
print("the probability of getting head after 3 coin tosses is",round(prob_head,6))
print("the probability of getting tail after 3 coin tosses is",round(prob_tail,6))
