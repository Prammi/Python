def bubbleSort(_input):    
    for i in range(0,len(_input)-1):
        for j in range(0,len(_input)-1-i):
            if _input[j]>_input[j+1]:
                temp=_input[j]
                _input[j]=_input[j+1]
                _input[j+1]=temp
                print("i value " + str(i) + " j value " + str(j) + " " + " ".join(str(_input)))
                
    return _input
        
       

sortedArray=bubbleSort([6,5,4,3,2,1])
print(sortedArray)