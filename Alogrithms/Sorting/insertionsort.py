def insertionSort(input):
    for i in range(0,len(input)-1):
        min=i
        for j in range(i,len(input)):
            if input[j]<input[min]:
                min=j
        
        input[min],input[i]=input[i],input[min]    
        

input=[9,8,7,6,5,4,3,2,1,0]
insertionSort(input)
print(input)  
              
