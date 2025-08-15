### PERMUTATIONS AND COMBINATIONS EXAMPLE 

input=[1,2,3]

def combinations(temp,index):
    if(index==len(input)):
        print(temp[:])
    else:        
        temp.append(input[index])
        combinations(temp,index+1)
        temp.pop()
        combinations(temp,index+1)    


def permutations(temp):
    if(len(temp)==len(input)):
        print(temp[:])
    else:            
        for x in range(len(input)):
            if input[x] not in temp:
                temp.append(input[x])
                permutations(temp)
                temp.pop()
            
    
        
combinations([],0)
permutations([])

    