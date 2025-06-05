# # Count Negative Elements Present in Every K-Length Subarray
# Input: arr = [-1, 2, -2, 3, 5, -7, -5], K = 3
# Output: 2, 1, 1, 1, 2



def countNegatives(input,k):
    count=0
    left=0
    
    for right in range(len(input)):
        if input[right]<0:
            count+=1
        if right>=k-1:
            print(count)
            if(input[left]<0):
                count=count-1
            left=left+1
            
countNegatives([-1, 2, -2, 3, 5, -7, -5],3)
            
            
            
            
            