# 3 Sum - Triplet Sum in Array
# Last Updated : 02 Jan, 2025
# Given an array arr[] of size n and an integer sum, the task is to check if there is a triplet in the array which sums up to the given target sum.

# Examples: 

# Input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
# Output: true 
# Explanation: The triplet [1, 4, 8] sums up to 13

# Input: arr[] = [1, 2, 4, 3, 6, 7], target = 10 
# Output: true 
# Explanation: The triplets [1, 3, 6] and [1, 2, 7] both sum to 10. 

# Input: arr[] = [40, 20, 10, 3, 6, 7], sum = 24 
# Output: false
# Explanation: No triplet in the array sums to 24.

def findTripletSum(arr,target):
    for i in range(len(arr)-2):
        start=i+1
        end=len(arr)-1
        while start!=end:            
            end-=1
            if(arr[i]+arr[start]+arr[end]==target):
                return True
    return False
        

if __name__=="__main__":
    input =  [40, 20, 10, 3, 6, 7]
    target = 24
    result=findTripletSum(input,target) # type: ignore
    print(result)