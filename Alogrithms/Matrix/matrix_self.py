def matrixTraversal(input):
    r=0
    c=0
    def recMatrixTraversal(r,c):
        print(f"row {r} and columns {c} value {input[r][c]}")
        input[r][c]=1
        if r-1 >=0 and input[r-1][c] !=1:
            recMatrixTraversal(r-1,c)
        elif c+1<len(input[0]) and input[r][c+1] !=1:
            recMatrixTraversal(r,c+1)
        elif r+1<len(input) and input[r+1][c] !=1:
            recMatrixTraversal(r+1,c)
        elif c-1>=0 and input[r][c-1] !=1:
            recMatrixTraversal(r,c-1)
    recMatrixTraversal(0,0)
    
    
    
input=[[0]*3 for i in range(3)]
print(matrixTraversal(input))