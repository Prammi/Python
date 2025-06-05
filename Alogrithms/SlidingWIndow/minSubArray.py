# # Minimum Size Subarray Sum
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint

def minSizeSubArray(input,target):
    op=[]
    left=0
    tempSum=0
    fl=-99999
    fr=99999
    left=0
    right=1
    tempSum=input[0]
    while left<right:
        tempSum=tempSum+input[right]
        if tempSum<target:
            right=right+1
        else:
            tempSum=tempSum-input[left]
            left=left+1
            if tempSum==target and right-left<fr-fl:
                fl=left
                fr=right
            if tempSum<=target:
                right=right+1
    return [fl,fr]


input=[2,3,1,2,4,3]
target=7
x=minSizeSubArray(input,target)
print(x)
