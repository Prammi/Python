input=[3,9,2,1,4,5,6,10]
def findTop3(n):
    tempArray=input[:n]
    tempArray.sort()
    tempArray=tempArray[::-1]
    left =1
    right =2
    smallest=-1
    for i in range(3,len(input)):
        if (tempArray[left]<tempArray[right] and (input[i]>tempArray[left])):
            smallest=left
            tempArray[smallest]=input[i]
            print(tempArray[0:3])
            siftup(tempArray,smallest)
        elif (tempArray[left]>tempArray[right] and (input[i]>tempArray[right])):
            smallest=right
            tempArray[smallest]=input[i]
            print(tempArray[0:3])
            siftup(tempArray,smallest)
            
    return tempArray
       

def siftup(input,val):
    parent=(val-1)//2
    while val>0 and   input[parent]<input[val]:
        input[val],input[parent]=input[parent],input[val]
        val=parent
        parent=(val-1)//2
        

def findbottom3(n):
    tempArray=input[:n]
    tempArray.sort()
    left =1
    right =2
    smallest=-1
    for i in range(3,len(input)):
        if (tempArray[left]>tempArray[right] and (input[i]<tempArray[left])):
            smallest=left
            tempArray[smallest]=input[i]
            print(tempArray[0:3])
            siftup(tempArray,smallest)
        elif (tempArray[left]<tempArray[right] and (input[i]<tempArray[right])):
            smallest=right
            tempArray[smallest]=input[i]
            print(tempArray[0:3])
            siftup(tempArray,smallest)
            
    return tempArray
       



print(input)        
result=findTop3(3)
result.sort(reverse=True)
print(result)
result=findbottom3(3)
print(result) 