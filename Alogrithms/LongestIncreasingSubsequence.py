def LongestIncreasingSubSeq(ip):
    left=0
    result=[0,0]
    temp=[0,0]
    for  right in range(1,len(ip)):
        temp[0]=left
        temp[1]=right
        if ip[right]<ip[right-1]:
            left=right
            temp[0]=left
            temp[1]=right
        else:
            temp[0]=left
            temp[1]=right
            if(result[1]-result[0]<temp[1]-temp[0]):
                result[0],result[1]=temp[0],temp[1]
            
    return result

ip=[3,1,3,2,3,6]
result=LongestIncreasingSubSeq(ip)
print(ip[result[0]:result[1]+1])
        
        