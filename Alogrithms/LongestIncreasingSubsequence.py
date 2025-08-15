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

def LongestCommonString(ip1,ip2):
    #create matrix
    finalResult=set()
    matrix=[[0]*(len(ip1)+1) for _ in range(len(ip2)+1)]
    
    # update the matrix 
    
    for i in range(len(ip2)):
        for j in range(len(ip1)):
            if ip2[i] ==ip1[j]:
                matrix[i+1][j+1]=max(1+matrix[i][j],matrix[i][j+1])
            else:
                matrix[i+1][j+1]=max(matrix[i+1][j],matrix[i][j+1])
               
                
    return matrix


def findNonCommonStrings(w1,w2):
    w1_array=list(w1)
    w2_array=list(w2)
    w3_array=w1_array[:]
    w3_array.extend(w2_array)
    setofWords=set(w3_array)
    print(setofWords)
    
    _dict= {word:0 for word in setofWords}
    print(_dict.items())
    
    for i in range(len(w1_array)):
        for j in range(len(w2_array)):
            if w1_array[i]==w2_array[j]:
                _dict[w1_array[i]]=1
                break
                
    #final result
    tempresult=0
    for value in _dict.values():
        if value==0:
            tempresult+=1
            
    return tempresult


def LongestIncreasingSeqNumber(ip):
    result=[1]
    prevMax=ip[0]
    
    def recursion(index,result,prevMax):
        if index<len(ip):
            if(ip[index]>prevMax):
                prevMax=ip[index]
                result[0]+=1
            index+=1
            return recursion(index,result,prevMax)
        else:
            return (index,result,prevMax)
    (a,b,c)=recursion(1,result,prevMax)
    return b

# word1="sea"
# word2="eat"
# #worst way of doing as its n2 and simple as 2 for loops
# result=findNonCommonStrings(word1,word2)
# print(result)

ip=[3,1,3,2,3,6]
result=LongestIncreasingSeqNumber(ip)
print(f"highest increasing seq {result}")
        
        
ip1="abcd"
ip2="acb"
result=LongestCommonString(ip1,ip2)
print(result) 


