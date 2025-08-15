arr=[1,2,3,4,5,6,7,8,9]
input2=[1,2,3,4,5,6,7,8,9,0]


def Binary_Search(target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search right half
        else:
            high = mid - 1  # Search left half
    return -1  # Target not found

def Modified_Binary_Search():
    low=0
    high=len(input2)-1
    while(low<high):
        mid=(low+high)//2
        if(input2[mid]>input2[high]):
            low=mid +1 ###### always add 1 to low 
        else:
            high=mid #### set high to mid only not -1
            
    return low
print(Binary_Search(1))
print(Modified_Binary_Search())