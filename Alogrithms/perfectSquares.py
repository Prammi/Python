def perfectSquare(sum):
    ips=[]
    finalResult=[]
    #find perfect squares in the sum 
    for i in range(1,(sum)+1):
        if is_perfect_square(i):
            ips.append(i)
    
    
    

    def recursion(i,capacity,ips,tempResult):
        if capacity==0:
            finalResult.append(tempResult[:])  
            
        if i>=len(ips)or capacity<=0:
            return None
        #take 
        tempResult.append(ips[i]) 
        recursion(i,capacity-ips[i],ips,tempResult)
        tempResult.pop()
        #dont take
        recursion(i+1,capacity,ips,tempResult)   
               
        
    recursion(0,sum,ips,[])
    return finalResult
    
def is_perfect_square(n):
    i = 1
    while n > 0:
        n -= i
        i += 2
    return n == 0

def findPermutations(str):
    finalResult=[]
    def recursion(str,i,path):
        if i==len(str):
            finalResult.append(path[:])
            return None
        # if i>len(str)-1:
        #     return []  
        #dont take
        recursion(str,i+1,path)
        #take
        path.append(str[i])
        recursion(str,i+1,path)
        path.pop()
        
           
    
    recursion(str,0,[])
    return finalResult
    
    
ip=['a','b','c']
result=findPermutations(ip)
print(result)
sum=5
result=perfectSquare(sum)
print(result)
