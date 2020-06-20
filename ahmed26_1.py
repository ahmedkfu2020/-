from matplotlib.pyplot import bar

labels = []
L = []
for i in range(8):
    labels = labels + [i+1]
    L  = L + [1]

# visualize the values of elements in the list 
bar(labels,L)


# 
# 1st step - query
#

# flip the sign of the marked element
L[3] = -1 * L[3]

# visualize the values of elements in the list 
bar(labels,L)


#
# 1st step - inversion
#

# summation of all values
sum = 0
for i in range(len(L)):
    sum += L[i]

# mean of all values
mean = sum / len(L)

# reflection over the mean
for i in range(len(L)):
    value = L[i]
    new_value = mean - (L[i]-mean)
    L[i] = new_value

# visualize the values of elements in the list 
bar(labels,L)

# 
# 2nd step - query
#

# flip the sign of the marked element
L[3] = -1 * L[3]

# visualize the values of elements in the list 
bar(labels,L)

#
# 2nd step - inversion
#

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

# visualize the values of elements in the list 
bar(labels,L)

for i in range(3):
    # flip the sign of the marked element
    L[3] = -1 * L[3]
    
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
        
# visualize the values of elements in the list 
bar(labels,L)        
