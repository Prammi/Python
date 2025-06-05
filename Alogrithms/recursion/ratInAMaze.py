matrix=[[1,0,0,0,0],[1,1,0,0,0],[0,1,1,1,0],[0,0,0,1,0],[0,0,0,1,1]]
visited= set()
SPoint=(0,0)
hasPath=False


def findPath(i,j):
    global hasPath
    if i==4 and j==4:
        hasPath=True
    if matrix[i][j]==1 and (i,j) not in visited: 
        visited.add((i,j))        
    #go bottom
        if i<len(matrix)-1:
            findPath(i+1,j)
    #go top
        if i>0:
            findPath(i-1,j)
    #go left
        if j>0:
            findPath(i,j-1)
    #go right
        if j<len(matrix[0])-1:
            findPath(i,j+1)
    
findPath(0,0)
print("Visited cells:", visited)
print(hasPath)