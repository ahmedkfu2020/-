# define iterations as a list
iterations = [20,30,50]
y = randrange(10)/10
x = randrange(10)/10

# define initial probability pairs as a double list
initial_probabilities =[    
    [1/2,1/2],
    [0,1],
    [x/(x+y),y/(x+y)]
]

for initial_probability_pair in initial_probabilities: 
    print("probability of head is",initial_probability_pair[0])
    print("probability of tail is",initial_probability_pair[1])
    print()

    for iteration in iterations:

        # initial probabilites
        [prob_head,prob_tail] = initial_probability_pair
        
        print("the number of iterations is",iteration)
        
        for i in range(iteration):
             # the new probability of head is calculated by using the first row 
            new_prob_head = prob_head * (1-y) + prob_tail * (1-x)

            # the new probability of tail is calculated by using the second row 
            new_prob_tail = prob_head * y + prob_tail * x

            # update the probabilities
            prob_head = new_prob_head
            prob_tail = new_prob_tail

        # print prob_head and prob_tail
        print("the probability of getting head after",iteration,"coin tosses is",round(prob_head,6))
        print("the probability of getting tail after",iteration,"coin tosses is",round(prob_tail,6))
        print()
    print()
