def paranthesis(n):
    def recurParanthesis(s,left,right):
        if(len(s)==2*n):
            print(s)
        else:
            if(left<n):
                recurParanthesis(s+"(",left+1,right)
            if(right<left):
                recurParanthesis(s+")",left,right+1)               
    
    recurParanthesis("",0,0)
paranthesis(3)   