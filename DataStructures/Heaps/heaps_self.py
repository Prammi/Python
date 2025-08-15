

def addElemMinHeap(item):
    input.append(item)
    swift_up_min(len(input)-1)
    
      
def swift_up_min(i):
    while i > 0:
        parent = (i - 1) // 2
        if input[i] < input[parent]:
            input[i], input[parent] = input[parent], input[i]
            i = parent
        else:
            break

def swift_up_max(i):
    while i > 0:
        parent = (i - 1) // 2
        if input[i] > input[parent]:
            input[i], input[parent] = input[parent], input[i]
            i = parent
        else:
            break

def addElemMaxHeap(i):
    input.append(i)
    swift_up_max(len(input)-1)


                   
def printHeap():
    for i in range(len(input)):
        print(input[i]) 

input =[]
print("inputs for min heap")      
addElemMinHeap(10)
addElemMinHeap(20)
addElemMinHeap(15)
addElemMinHeap(3)
addElemMinHeap(5)
printHeap()                

print("inputs for max heap")   t=[]
addElemMaxHeap(10)
addElemMaxHeap(20)
addElemMaxHeap(15)
addElemMaxHeap(3)
addElemMaxHeap(5)
printHeap()    
    
    