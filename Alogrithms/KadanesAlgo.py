def kadane(ip):
    from math import inf
    temp=ip[0]
    result=ip[0]
    for i in range(1,len(ip)):
        temp=max(ip[i],ip[i]+temp)
        result=max(temp,result)
        
    return result
    

ip=[9,8,-9,3,-10,-20,50]
ip2=[-4,-3,-2,-1,0]

result=kadane(ip2)
print(result)

# logic is check temp+curr element with current element 
