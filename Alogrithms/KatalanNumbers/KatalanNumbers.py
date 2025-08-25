input =5

catalan=[0]*(input+1)
catalan[0]=1
catalan[1]=1


for i in range(2,input+1):
    for j in range(i):
        catalan[i]+= catalan[j]*catalan[i-j-1]
        
print(catalan)