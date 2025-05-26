def selectionSort(_input):   
    for i in range(0,len(_input)-1):
        min_index=i
        for j in range(i+1,len(_input)):
            if _input[i]>_input[j]:
                min_index=j
                print("i value ="+str(i) +" min_index is"+ str(min_index))
        if min_index is not i:   
            temp=_input[min_index] 
            _input[min_index]=_input[i]  
            _input[i]=temp
        print("i value " + str(i) + " j value " + str(j) + " " + " ".join(str(_input)))
                
    return _input
        
       
print("SELECTION SORT")
sortedArray=selectionSort([6,5,4,3,2,1,100,56, 19,11,22])
print(sortedArray)