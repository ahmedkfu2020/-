def biased_coin(N,B):
    from random import randrange
    random_number = randrange(N)
    if random_number < B:
        return "Head"
    else:
        return "Tail"
        
from random import randrange
N = 101
B = randrange(100)

total_tosses = 500
the_number_of_heads = 0
for i in range(total_tosses):
    if biased_coin(N,B) == "Head":
        the_number_of_heads = the_number_of_heads + 1

my_guess =  the_number_of_heads/total_tosses        
real_bias = B/N
error = abs(my_guess-real_bias)/real_bias*100 

print("my guess is",my_guess)
print("real bias is",real_bias)
print("error (%) is",error)
