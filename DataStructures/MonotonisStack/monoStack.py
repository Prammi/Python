def nextgreater(arr):
    result=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[stack[-1]]<arr[i]:
            curr=stack.pop()
            result[curr]=arr[i]
        stack.append(i)
            
    return result
    


def nextSmaller(arr):
    result=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[i]<arr[stack[-1]]:
            curr=stack.pop()
            result[curr]=arr[i]
        stack.append(i)
    
    return result

def prevSmaller(arr):
    result=[-1]*len(arr)
    stack=[]
    for i in range(len(arr)):
        while stack and arr[i]>arr[stack[-1]]:
            idx=stack.pop()
            result[i]=arr[idx]
        stack.append(i)
    return result


def previous_smaller_element(arr):
    stack = []
    result = [-1] * len(arr)  # Initialize result array with -1

    for i in range(len(arr)):  # Iterate from left to right
        while stack and stack[-1] >= arr[i]:  # Maintain a decreasing stack
            stack.pop()

        if stack:  # If stack is not empty, top is the previous smaller element
            result[i] = stack[-1]

        stack.append(arr[i])  # Push current element onto stack

    return result


arr = [4, 8, 5, 2, 25]
result = nextgreater(arr)
result2 = nextSmaller(arr)
result3 = prevSmaller(arr)
result4=previous_smaller_element(arr)

print(result3)
print(result4)

# array_ = [1]
# print(array_[0])
# print(array_[-1])
