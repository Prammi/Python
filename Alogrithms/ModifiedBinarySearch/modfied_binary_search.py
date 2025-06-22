class Modified_Binary_Search:
    def __init__(self):
        pass
    
    def checkPivot(self,i,max):
        if i<0:
            i=max+i
        elif i>max:
            i=i-len(arr)
        return i
    
    def findMinElementIndex(self,arr,elem):
        deviation= -100
        for i in range(len(arr)-1):            
            if arr[i] > arr[i+1]:
                deviation=i+1
                break            
        
        left=deviation
        right=deviation-1
        

        while True:
            if(arr[left]==elem):
                return left
            elif(arr[right]==elem):
                return right
            else:       
                if left < right:
                    pivot=(left+right)//2
                elif right>left:
                    pivot=right -((left+right)//2)
                else:
                    break
                if arr[pivot]==elem:
                    return pivot
                if(arr[pivot]>elem):
                    right=self.checkPivot(pivot-1,len(arr))
                elif(arr[pivot]<elem):
                    left=self.checkPivot(pivot+1,len(arr))      

        
        return -1


arr=[4,5,6,7,0,1,2]
mod_bst=Modified_Binary_Search()
result =mod_bst.findMinElementIndex(arr,0)
print(result)