def insertionSort(_input):       
    for i in range(0,len(_input)-1):
        j=i+1
        while(_input[j]<_input[j-1] and j>0):           
            temp=_input[j]
            _input[j]=_input[j-1]
            _input[j-1]=temp
            print("i value " + str(i) + " j value " + str(j) + " " + " ".join(str(_input)))        
            j-=1
    return _input
        
       
print("Insertion SORT")
print([6,5,4,3,2,1])
sortedArray=insertionSort([6,5,4,3,2,1])
#sortedArray=insertionSort([2,1,3,4,5,6])

print(sortedArray)