# all portions are stored in a list 
all_portions = [7,5,4,2,6,1];

# let's calculate the total portion
total_portion = 0
for i in range(6):
    total_portion = total_portion + all_portions[i]

print("total portion is",total_portion)

# find the weight of one portion
one_portion = 1/total_portion
print("the weight of one portion is",one_portion)

print() # print an empty line
# now we can calculate the probabilities of rolling 1,2,3,4,5, and 6
for i in range(6):
    print("the probability of rolling",(i+1),"is",(one_portion*all_portions[i]))
