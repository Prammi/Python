arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sum_till_here=0
max_sum=0
for i in range(len(arr)):

    sum_till_here=max(sum_till_here+arr[i],arr[i])
    max_sum=max(sum_till_here,max_sum)
    
print(max_sum)


#logic is to check the impact of current element on sum_till_her
#if its adding/increasing  sum_till_here  with current elemnt then update it 
# compare it with final result and udpate it