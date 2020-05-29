def biased_coin(N,B):
    from random import randrange
    random_number = randrange(N)
    if random_number < B:
        return "Head"
    else:
        return "Tail"
