# # 4. Find the Longest Substring of a String Containing ‘K’ Distinct Characters
# Input: s = 'abcbdbdbbdcdabd'
# k = 2
# Output: bdbdbbd


def longestSubstring(input,k):
    starter=""
    d={}
    starterIndex=0
    for i in range(0,len(input)-1):
        if input[i] not in starter:
            d[input[i]]=1
        else:
            d[input[i]]=d[input[i]]+1
        starter=starter+input[i]
        if len(d) ==2:
            maxLength=input[0:i+1]  
            starterIndex=i+1
            break
         
            
    for i in range(starterIndex,len(input)):        
        if input[i] in starter:
            starter=starter+input[i]
            if(len(starter)>len(maxLength)):
                maxLength=starter
        else:
            starter=starter[-(k-1):] +input[i]
    return maxLength


if __name__=="__main__":
    input="abcbdbdbbdcdabd"
    k=2
    result=longestSubstring(input,k)
    print(result)