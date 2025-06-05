# Remove duplicates from Sorted Array
# Last Updated : 19 Nov, 2024
# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

# Note: The elements after the distinct ones can be in any order and hold any value, as they don't affect the result.

# Examples: 

# Input: arr[] = [2, 2, 2, 2, 2]
# Output: [2]
# Explanation: All the elements are 2, So only keep one instance of 2.

# Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# Output: [1, 2, 3, 4, 5]

# Input: arr[] = [1, 2, 3]
# Output: [1, 2, 3]
# Explanation : No change as all elements are distinct.

def removeDuplicated(arr):
    idx=1
    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            arr[idx]=arr[i+1]
            idx+=1
            
    return idx

if __name__ == "__main__":
    input=[1,1,2,2,3,3,3]
    idx=removeDuplicated(input)
    print(input[0:idx])
    print(input)
    