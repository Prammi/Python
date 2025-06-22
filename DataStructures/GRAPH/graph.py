from collections import deque
class Graph:
    def __init__(self):
        pass

    def depthFirstTraversal(self,ip):        
        print("printing depth first approach")              
        visited=[]
        stack=[]
        stack.append('a')
        while len(stack)>0:
            temp_Node=stack.pop()
            if temp_Node not in visited:
                visited.append(temp_Node)
                print(temp_Node)
                stack.extend(ip[temp_Node])
        return None
    
    def breathFirstTraversal(self,ip):
        print("printing breadth first approach")
        visited=[]
        queue=deque()
        queue.append('a')
        while len(queue)>0:
            temp_node=queue.popleft()
            if temp_node not in visited:
                visited.append(temp_node)
                print(temp_node)
                queue.extend(ip[temp_node])
    
    def findPath(self,source,destination,ip):
        print(f"finding path between {source} and {destination}") 
        result=[]
        def recursive(node,path,result):
            path=path+ ' '+node
            if node==destination:
                result.append(path)
            else:
                path=path+'->'
                for i in ip[node]:
                    if len(i)>0:
                        recursive(i,path,result)
        
        recursive(source,"",result)
        return result
    
    
    def findLargestComponent(self,ip):
        result=0
        visited=[] 
        stack=[]
        result=0
        for node in ip:
            count=0
            path=""
            if node not in visited:
                stack.append(node)
                while len(stack)>0:
                    tempNode=stack.pop()
                    if tempNode not in visited: 
                        path=path+str(tempNode)+"-->"                   
                        count+=1
                        visited.append(tempNode)
                        stack.extend(ip[tempNode])
                    
            if len(path)>0:
                print(path)
            result=max(count,result)
        return result
    
    def buildGraph(self,ip):
         ip_nodes={}
        
         for i in ip:
            node=i[0]
            neighbours=i[1]
            if node not in ip_nodes:
                ip_nodes[node]=[]
            if neighbours not in ip_nodes:
                ip_nodes[neighbours]=[]
                
            ip_nodes[node].append(neighbours)
            ip_nodes[neighbours].append(node)
            
         return ip_nodes
        
        
    def findShortestPath(self,ip,source, destination):
        # prep the nodes 

        ip_nodes=self.buildGraph(ip)
        # find the shortest path 
        def recursiveDPS(node,path,result,visited): 
            path.append(node)           
            if node==destination:
                print("-->".join(map(str, result)))
                result[0]=min(len(path),result[0]) 
            else:
                if node not in visited:
                    visited.append(node)                
                    for neighbour in ip_nodes[node]:
                        recursiveDPS(neighbour,path.copy(),result,visited)
                    
        
        path=[]
        result=[999]
        visited=[]
        recursiveDPS(source,path,result,visited)
        
        print(f"the shortest path between {source} and {destination} is {result[0]}" )
            
    def  findShortestPathBFS(self,ip,source, destination):
        # prep the nodes 
        ip_nodes=self.buildGraph(ip) 
        visited=[]
        path=[]
        result=[9999]
        # traverse BFS
        queue=deque()
        queue.append(source)  
        
        def recursiveCall(node,path,result,visited):
            path.append(node)
            while len(queue)>0:
                if node ==destination:
                    print("-->".join(map(str, result)))
                    result[0]=min(len(path),result[0])
                    break
                else:
                    tempNode=queue.popleft()
                    if tempNode not in visited:
                        visited.append(node)
                        queue.extend(ip_nodes[node])
                        recursiveCall(node,path.copy(),result,visited)
                    
                    
                
            
        recursiveCall(source,path,result,visited)
        print(f"the shortest path between {source} and {destination} is {result[0]}" )
    
    
    def bfs_shortest_path(self,graph, start, goal):
        ip_nodes=self.buildGraph(graph)
        visited = set()
        queue = deque([[start]])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == goal:
                return path

            if node not in visited:
                visited.add(node)
                for neighbor in ip_nodes.get(node, []):
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)      
    
    def dfsIsLandCount(self,r,c,gridMap,visited,landCount,index):
        visited[r][c]="1"
        if r-1>=0:
            if visited[r-1][c] !="1" and gridMap[r-1][c] !="0" :
                landCount[index]+=1
                self.dfsIsLandCount(r-1,c,gridMap,visited,landCount,index)
                
        #go bottom
        if r+1<=len(gridMap)-1:
            if visited[r+1][c] !="1" and gridMap[r+1][c] !="0" :
                landCount[index]+=1
                self.dfsIsLandCount(r+1,c,gridMap,visited,landCount,index)
        
        
        #go left
        if c-1>=0:
            if visited[r][c-1] !="1" and gridMap[r][c-1] !="0" :
                landCount[index]+=1
                self.dfsIsLandCount(r,c-1,gridMap,visited,landCount,index)
                
        #go right
        if c+1<=len(gridMap[0])-1:
            if visited[r][c+1] !="1" and gridMap [r][c+1] !="0" :
                landCount[index]+=1
                self.dfsIsLandCount(r,c+1,gridMap,visited,landCount,index)
                      
    def countIsLands(self,gridMap):
        visited=[[0]*len(gridMap[0]) for i in range(len(gridMap))]
        count=0
        isLandCount=[]
        for r in range(len(gridMap)):
            for c in range(len(gridMap[0])):
                if gridMap[r][c]=="1" and visited[r][c] !="1":
                    isLandCount.append(1)
                    count+=1
                    self.dfsIsLandCount(r,c,gridMap,visited,isLandCount,len(isLandCount)-1)
                    
        print(isLandCount)

g=Graph()
isLandWaterGrid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
g.countIsLands(isLandWaterGrid)

            
ip={
'a':['c','b'],
'b':['a','d'],
'c':['a','e'],
'd':['b','f'],
'f':['d'],
'e':['c']
}

g.depthFirstTraversal(ip)
g.breathFirstTraversal(ip)


ip2={
    'f':['g','i'],
    'g':['h'],
    'h':[],
    'i':['g','k'],
    'j':['i'],
    'k':[]
}
print(g.findPath('f','h',ip2))


ip3 = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}
paths = g.findPath('A', 'D', ip3)
print(paths)

ip4={
    0:[1,5,8],
    1:[0],
    5:[0,8],
    8:[0,5],    
    4:[2,3],
    2:[3,4],
    3:[2,3],
    9:[10],
    10:[11],
    11:[12],
    12:[13],
    13:[14],
    14:[15],
    15:[14]
}
paths=g.findLargestComponent(ip4)
print(paths)


ip5=[['w','x'],['x','y'],['z','y'],['z','v'],['w','v']]
g.findShortestPath(ip5,'v','w')
g.bfs_shortest_path(ip5,'v','w')




# path=['1','2','3']
# result=[]
# result.append(" -> ".join(path))
# print(result)


# alternative for gettting the count rotating through matrix def dfsIslandSize(self, r, c, grid, visited):
#     if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
#         return 0
#     if visited[r][c] or grid[r][c] == 0:
#         return 0

#     visited[r][c] = True
#     size = 1

#     # explore all 4 directions
#     size += self.dfsIslandSize(r-1, c, grid, visited)
#     size += self.dfsIslandSize(r+1, c, grid, visited)
#     size += self.dfsIslandSize(r, c-1, grid, visited)
#     size += self.dfsIslandSize(r, c+1, grid, visited)

#     return size
