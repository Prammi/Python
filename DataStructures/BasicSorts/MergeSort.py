def mergeHelper(input1,input2):
    temp=[]
    i=0
    j=0
    while(len(temp)<len(input1)+len(input2)):
        
        if j == len(input2) or input1[i]<input2[j]:
            temp.append(input1[i])
            i+=1
        elif i==len(input1)or input1[i]>input2[j]:
            temp.append(input2[j])
            j+=1
            
    return temp 
       
def mergeSort(myList):
    if len(myList)==1:
        return myList
    midpoint=int(len(myList)/2)
    left=mergeSort(myList[0:midpoint]  )
    right=mergeSort(myList[midpoint:]  )   
    return mergeHelper(left,right)  
         
        
    
          
    
    
mergedArrray= mergeSort([8,7,6,5,4,3,2,1])
print(mergedArrray)