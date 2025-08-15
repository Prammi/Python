
input=[1,1,1,6]
tempInput=[-1]*len(input)
#monotonic code
stack =[]
for i in range(len(input)):
    while(len(stack)>0 and input[i]>input[stack[-1]]):
        popItem=stack.pop()
        tempInput[popItem]=input[i]  
    stack.append(i)  
    
print(tempInput)
    
