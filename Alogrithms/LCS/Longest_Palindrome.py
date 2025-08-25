import numpy as np
str="aaaaa"
input=list(str) # ['a','b','a','f']
rev_input=input[::-1]
matrix_len=len(input)+1
matrix=np.zeros(matrix_len**2,dtype=np.int16).reshape((matrix_len,matrix_len))

def get_longest_palindrome():
    for r in range(1,matrix_len):
        for c in range(1,matrix_len):
            if(rev_input[r-1]==input[c-1]):
                matrix[r][c]=matrix[r-1][c-1]+1
            else:
                matrix[r][c]=max(matrix[r][c-1],matrix[r-1][c])
    
    get_last_row=matrix[matrix_len-1]
    palindrome_string=""
    for i in range(matrix_len-1,0,-1):
        if(get_last_row[i] !=get_last_row[i-1]):
            palindrome_string=palindrome_string+input[i-1]
            
    print(palindrome_string)
            
    
get_longest_palindrome()