input=[
    [0,2,8,0,0,0],
    [2,0,5,6,0,0],
    [8,5,0,3,2,0],
    [0,6,3,0,1,9],
    [0,0,2,1,0,3],
    [0,0,0,9,3,0],
    ]

finalResult={}
nodes=["A","B","C","D","E","F"]
visited=[]


def get_Nodes(index):
    tempResult=[]
    tempInput=input[index]
    for i in range(len(tempInput)):
        if tempInput[i]!=0 and i!=index and (nodes[i] not in visited):
            tempResult.append([nodes[i],tempInput[i],i])
            
    return tempResult    

def formTheFinalResult():
    for n in range(len(nodes)):
        finalResult[nodes[n]]=[9999,9999]

def findShortestPath(input):
    formTheFinalResult()
    print(finalResult)
    currMinLength=0
    for r in range(len(input)):
        minLength=[]
        _nodes=get_Nodes(r)
        for _n in _nodes:
            if(input[r][_n[1]]+currMinLength<finalResult[_n[0]][0]):
                finalResult[_n[0]]=[input[r][_n[1]]+currMinLength,_n[r]]
                minLength.append(input[r][_n[1]]+currMinLength)
            else:
                minLength.append(finalResult[_n[0]][0])
        visited.append(_nodes[r])
        currMinLength=min(minLength)
        
       
        

findShortestPath(input)