class Sorting:
    def __init__(self):
        pass
    
    def bubbleSort(self,arr):
        for i in range(1,len(arr)):
            for j in range(1,len(arr)):
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
        return arr
    
    def insertionSort(self,arr):
        for i in range(1,len(arr)):
            for j in range(i,0,-1):
                if arr[j]<arr[j-1]:
                    arr[j],arr[j-1]=arr[j-1],arr[j]
        
        return arr
    
    def selectionSort(self,arr):
        for i in range(0,len(arr)):
            smallest=i
            for j in range(i, len(arr)):
                if(arr[j]<arr[smallest]):
                    smallest=j
            
            arr[i],arr[smallest]=arr[smallest],arr[i]  
        
        return arr  
    
    def mergeSort(self,arr):
         
        if len(arr)==1:
            return [arr[0]]
        _len=len(arr)
        mid=_len//2
        lInput=arr[:mid]
        rInput=arr[mid:]
        left=self.mergeSort(lInput)
        right=self.mergeSort(rInput)
        l=0 
        r=0
        temp=[]
        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                temp.append(left[l])
                l+=1
            else:
                temp.append(right[r])
                r+=1
        
        while l<len(left):
            temp.append(left[l])
            l+=1
        
        while r<len(right):
            temp.append(right[r])
            r+=1  
        
        return temp
        
        
        
        
        
        
                    

sorting=Sorting()
arr=[-8,-9,5,6,3,4]
arr2=[9,8,7,6,5,100,-2]

bb_result=sorting.bubbleSort(arr.copy())
is_result=sorting.insertionSort(arr.copy())
ss_result=sorting.selectionSort(arr.copy())
merge_sort=sorting.mergeSort(arr2.copy())
print(merge_sort)