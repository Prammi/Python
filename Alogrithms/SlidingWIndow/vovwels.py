# 7. Length of the Longest Substring That Doesn’t Contain Any Vowels


def longestSubString(input):
 
    vowels=['a','e','i','o','u']
    left=0
    right=0

    maxStr=""
    maxdiff=-99999999
    for i in range(len(input)):
        if input[i] in vowels:
            
            right=right+1
            left=right
        else:
            right=right+1
            diff=right+1-left
            if(diff>maxdiff):
                maxdiff=diff
                maxStr=input[left:right]   
    return maxStr



input= "codeforintelligents"
op=longestSubString(input)
print(op)