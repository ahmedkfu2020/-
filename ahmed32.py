#
# We copy and paste the previous codes
#

# initial case
# We assume that the probability of having head is 1 at the beginning,
#    becasue Asja will start with one euro.
prob_head = 1
prob_tail = 0

number_of_iterations = 10

for i in range(number_of_iterations):
    # the new probability of head is calculated by using the first row 
    new_prob_head = prob_head * 0.6 + prob_tail * 0.3

    # the new probability of tail is calculated by using the second row 
    new_prob_tail = prob_head * 0.4 + prob_tail * 0.7

    # update the probabilities
    prob_head = new_prob_head
    prob_tail = new_prob_tail
    
# print prob_head and prob_tail
print("the probability of getting head after",number_of_iterations,"coin tosses is",prob_head)
print("the probability of getting tail after",number_of_iterations,"coin tosses is",prob_tail)
