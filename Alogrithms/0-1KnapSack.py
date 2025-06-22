def knapSack(weights,profits,capacity):
    _dp=buildTheMatrix(len(weights),capacity)
    for w in range(1,len(weights)+1):
        for c in range(capacity+1):
            if c < weights[w-1]:
                _dp[w][c]=_dp[w-1][c]
            else:
                _dp[w][c]=max(_dp[w-1][c] ,( profits[w-1]+_dp[w-1][c-weights[w-1]] ))
    return _dp

def buildTheMatrix(r,c):
    _matrix= [[0]*(c+1) for i in range((r+1))]
    return _matrix
    


weights=[1,2,3,4,5]
profits=[10,8,6,4,2]
capacity=8
result=knapSack(weights,profits,capacity)
list(map(print, result))