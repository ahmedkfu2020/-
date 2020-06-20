from matplotlib.pyplot import bar

labels = []
L = []
for i in range(16):
    labels = labels + [i+1]
    L  = L + [1]
    
for i in range(20):
    print((i+1),"th iteration:")
    # flip the sign of the marked element
    L[11] = -1 * L[11]
    
    # print after query phase
    print(L[11])
    
     # summation of all values
    sum = 0
    for i in range(len(L)):
        sum += L[i]

    # mean of all values
    mean = sum / len(L)

    # reflection over mean
    for i in range(len(L)):
        value = L[i]
        new_value = mean - (L[i]-mean)
        L[i] = new_value
        
    # print after inversion phase
    print(L[11])
    print()
