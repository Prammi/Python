def threeSumClosest(nums, target):
    
   diff=99999
   closeSum=0
   if len(nums)<3 or len(nums)>500:
       closeSum=-1
   elif(target<-10**4 or target> 10**4):
       closeSum=-1
   elif len(nums)==3:
       closeSum=sum(nums)
   else:
       for i in range(0,len(nums)-2):
           hook=nums[i]
           start=nums[i+1]
           for j in range(i+2,len(nums)):
               end=nums[j]
               tempDiff= abs(target -(hook+start+end))
               if(tempDiff<diff):
                   diff=tempDiff
                   closeSum=hook+start+end
             

               j+=1 
   return closeSum

result=threeSumClosest([2,5,6,7],16)
#result=threeSumClosest([10,20,30,40,50,60,70,80,90],1)

print(result)