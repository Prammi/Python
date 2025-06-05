class Solution(object):
    def longestPalindrome(self, s):
        longest=0
        left=0
        right=len(s)-1
        while left<=right and right>0 and left<len(s)-1:
            if s[left]==s[right]:
                left+=1                
                right-=1
                if(left==right):
                    longest+=1
                else:
                    longest+=2                
            else:
                right-=1
            
                
            
        
        


_cl=Solution()
_cl.longestPalindrome('abbc')