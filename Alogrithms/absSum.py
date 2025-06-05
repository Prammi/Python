# Count pairs with absolute difference equal to k

def getAbsSum(input,sum):
    c=0
    l=0
    r=len(input)-1
    while l < len(input)-1:
        if(r==l):
            l=l+1
            r=len(input)-1
        if abs(input[l]-input[r])==sum:
            c=c+1
        r=r-1    
        
    return c

        
    
if __name__ == "__main__":
    
    input=[1, 4, 1, 4, 5]
    c=getAbsSum(input,3)
    print(c)
    
    input=[8, 16, 12, 16, 4, 0]
    c=getAbsSum(input,4)
    print(c)