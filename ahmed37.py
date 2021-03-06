# define iterations as a list
iterations = [20,30,50]

for iteration in iterations:
    
    # initial probabilites
    prob_head = 1
    prob_tail = 0
    a = randrange(10)/10
    b= randrange(10)/10
    print("a = ", a , "b = ", b)
    print("the number of iterations is",iteration)
    
    for i in range(iteration):
         # the new probability of head is calculated by using the first row 
        new_prob_head = prob_head * a + prob_tail * b

        # the new probability of tail is calculated by using the second row 
        new_prob_tail = prob_head * (1-a) + prob_tail * (1-b)

        # update the probabilities
        prob_head = new_prob_head
        prob_tail = new_prob_tail
    
    # print prob_head and prob_tail
    print("the probability of getting head after",iteration,"coin tosses is",prob_head)
    print("the probability of getting tail after",iteration,"coin tosses is",prob_tail)
    print()
