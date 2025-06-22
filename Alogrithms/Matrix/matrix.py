class Matrix:
    def __init__(self):
        'pass'
        
    def printAllNumbers(self,arr):  
        visited=[[-1]*4 for i in range(4)]      
        def pNumber(r,c):
            visited[r][c]=0
            print(f"the value at row {r} col {c} is {arr[r][c]}")

            #go top
            if r>0:
                if visited[r-1][c] is not 0:
                    pNumber(r-1,c)
            
            #go left
            if c>0:
                if visited[r][c-1] is not 0:
                    pNumber(r,c-1)
                
            
            #go right
            if c<len(arr[0])-1:
                if visited[r][c+1] is not 0:
                    pNumber(r,c+1)
            
            #go down
            if r<len(arr)-1:
                if visited[r+1][c] is not 0:
                    pNumber(r+1,c)
                
        pNumber(0,0)
     
    def floodFill(self,arr,r,c,color):
        
        def fillColor(r,c):
            arr[r][c]=color
            #go top
            if r>0:
                if arr[r-1][c] is 1:
                    fillColor(r-1,c)
            
            #go bottom
            if r<len(arr)-1:
                if arr[r+1][c] is 1:
                    fillColor(r+1,c)
            
            #go left
            if c>0:
                if arr[r][c-1] is 1:
                    fillColor(r,c-1)
            #go right
            if c<len(arr[0])-1:
                if arr[r][c+1] is 1:
                    fillColor(r,c+1)
        
        
        
        fillColor(r,c)    

mat=Matrix()
arr=[[0]*4 for i in range(4)]
mat.printAllNumbers(arr)
testInput=[[1,1,1],[1,1,0],[1,0,1]]

mat.floodFill(testInput,1,1,2)
print(testInput)