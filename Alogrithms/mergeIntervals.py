class Intervals:
    def __init__(self):
         pass
     

    def mergeIntervals(self,input):
            input.sort(key= lambda x:x[0])
            result=[]
            result.append(input[0])
            for start,end in input[1:]:
                if start<result[-1][1]:
                    result[-1][1]=max(end,result[-1][1])
                else:
                    result.append([start,end])
            
            
            return result
    
    def addandMerge(self,arr,newInput):
            arr.append(newInput)
            arr.sort(key= lambda x:x[0])
            result=[]
            result.append(arr[0])
            for start,end in arr[1:]:
                if start<result[-1][1]:
                    result[-1][1]=max(end,result[-1][1])
                else:
                    result.append([start,end])
            
            
            return result
        
    
intervals=[[1,3],[2,6],[8,10],[15,18]]
newInterval=[17,19]   
int=Intervals()
result=int.mergeIntervals(intervals)
print(result)
result=int.addandMerge(intervals,newInterval)
print(result)
