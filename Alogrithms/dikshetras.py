def greedy_dijkstra(graph,visited):
    def getNodes(node):
        temp=graph[node]
        neighbours=[]
        for i in range(len(temp)):
            if temp[i] !=0:
                neighbours.append(i)
        
        return neighbours
    

    def findMinNode(node):
        _length=999999
        tempNode=None
        for i in finalResult:
            [length,prevNode]=finalResult[i]
            if prevNode==node and length<_length:
                _length=length
                tempNode=i
        return tempNode
                

    def callRecursion(node,length):
        neighbours=getNodes(node)
        for neighbour in neighbours :
            if neighbour not in visited:
                if finalResult[neighbour][0]>length+graph[node][neighbour]:
                    finalResult[neighbour]=[length+graph[node][neighbour],node]
        nextNode=findMinNode(node)
        if(nextNode is not None):
            tempLength=finalResult[nextNode][0]
            visited.append(node)
            callRecursion(nextNode,tempLength)
        
    
    
    for i in range(len(graph)):
        finalResult[i]=[9999,9999]
        
    callRecursion(0,0)
    return finalResult

graph = [ 
         [0, 1, 2, 0, 0, 0], 
         [1, 0, 0, 5, 1, 0], 
         [2, 0, 0, 2, 3, 0], 
         [0, 5, 2, 0, 2, 2], 
         [0, 1, 3, 2, 0, 1], 
         [0, 0, 0, 2, 1, 0] ] 

visited=[]
length=0
finalResult={}
result=greedy_dijkstra(graph, visited)   
print(result)
result[0]=[0,0]
for i in range(len(finalResult)-1,0,-1):
    def getPrevNode(node,path,length):
        path=path+str(node)
        [_length,prevNode]=finalResult[node]
        if prevNode !=node:
            path=path+'==>'
            getPrevNode(prevNode,path,length)
        else:
            print(f"the path is {path} and the distance is {length}")
             
    [length,prevNode]=finalResult[i]
    getPrevNode(i,"",length)
    
