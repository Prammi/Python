import numpy as np

input=[
    [1,20],
    [2,30],
    [3,40],
    [4,70],
    [5,90],
]
knapSack_Capacity=6
number_of_items=len(input)

ks_matrix=np.zeros((knapSack_Capacity +1)*(number_of_items+1)).reshape([number_of_items+1,knapSack_Capacity +1])
for current_item in range(1,len(ks_matrix)):
    weight=input[current_item-1][0]
    profit=input[current_item-1][1]
    for ks_weight in range(1, len(ks_matrix[current_item]+1)):
        previous_item=ks_matrix[current_item-1]
        if(ks_weight<weight):            
            ks_matrix[current_item][ks_weight]=previous_item[ks_weight]
        else:
            ks_matrix[current_item][ks_weight]=max(previous_item[ks_weight],profit+previous_item[ks_weight-weight])


print(ks_matrix)