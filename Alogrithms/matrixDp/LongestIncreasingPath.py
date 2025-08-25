matrix = [[3,4,5],[3,2,6],[2,2,1]]
greaterResult=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
lesserResult=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]

greaterResult[1][1]= 1
lesserResult[1][1]= 1
finalResult=0

# print(resultMatrix)

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        #Either go Top
        if r-1>=0:
            if(matrix[r][c] <matrix[r-1][c]):
                greaterResult[r+1][c+1]=1+max(greaterResult[r][c+1],greaterResult[r+1][c])
               
            else:
                lesserResult[r+1][c+1]=1+max(lesserResult[r][c+1],lesserResult[r+1][c])
            
               
        #Either go go left
        if c-1>=0:
            if(matrix[r][c] <matrix[r][c-1]):
                greaterResult[r+1][c+1]=1+max(greaterResult[r][c+1],greaterResult[r+1][c])
            else:
                lesserResult[r+1][c+1]=1+max(lesserResult[r][c+1],lesserResult[r+1][c])
                
        
        
        finalResult=max(finalResult,lesserResult[r+1][c+1],greaterResult[r+1][c+1])
                

print(finalResult)

            
            