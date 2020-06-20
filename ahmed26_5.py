N = 16
marked_elements = [0,2,9]

L = []

for i in range(N):
    L = L + [1/(N**0.5)]

# print the elements of a given list with a given precision
def print_list(L,precision):
    output = ""
    for i in range(len(L)):
        output = output + str(round(L[i],precision))+"  "
    print(output)

print_list(L,3)

for i in range(10):
    print((i+1),"th iteration:")
    # flip the sign of the marked element
    for marked in marked_elements:
        L[marked] = -1 * L[marked]

    # print after query phase
    print_list(L,3)
    
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
        
    # calculate the length of the list
    length_of_list = 0    
    for j in range(len(L)):
        length_of_list += L[j]*L[j]
    
    print("length of list is",round(length_of_list,3))
    # print after inversion phase
    print_list(L,3)
    print()    
