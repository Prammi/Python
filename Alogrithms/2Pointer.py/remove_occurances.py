# Remove All Occurrences of an Element in an Array
# Last Updated : 09 Nov, 2024
# Given an integer array arr[] and an integer ele the task is to the remove all occurrences of ele from arr[] in-place and return the number of elements which are not equal to ele. If there are k number of elements which are not equal to ele then the input array arr[] should be modified such that the first k elements should contain the elements which are not equal to ele and then the remaining elements.

# Note: The order of first k elements may be changed.

def removeOccur(input,ele):
    start=0
    end=0
    while end<len(input):
        if(end==ele):
            input[start],input[end]=input[end],input[start]
            start+=1
            end=start
        else:
            end+=1
            
input=[3,2,2,3]
removeOccur(input,3)
print(input)
            

    
    