input=[9,8,7,6,5,4,3,2,1]
input2=[-9,8,7,6,5,4,3,2,1]

def siftup(val):
    input.append(val)
    i=len(input)-1
    parent=(i-1)//2
    while i>0 and   input[parent]<input[i]:
        input[i],input[parent]=input[parent],input[i]
        i=parent
        parent=(i-1)//2
        
def siftDown():
    i=0
    left = 2*i +1
    right = 2*i +2
    smallest=-1
    while((left<=len(input2) and input2[left]<input2[i]) or( right<=len(input2) and input2[right]>input2[i])):
        if(input2[left]>input2[right] and right>=len(input2)):
            smallest=left
        else:
            smallest=right
        if(input2[smallest]>input2[i]):
            input2[smallest],input2[i]=input2[i],input2[smallest]
        i=smallest
        left=2*i +1
        right= 2*i +2
    


print(input)
siftup(10)
print(input)


print(input2)
siftDown()
print(input2)

# print(str((3-1)//2))
# print(str((3-1)/2))


