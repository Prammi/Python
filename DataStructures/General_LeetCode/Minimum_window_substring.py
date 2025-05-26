from collections import Counter,defaultdict

class Solution():
       
    def minWindow(self,s,t):
        t_dict=Counter(t) ##rather than this u can find your own dictionary 
        
        t_len=len(t)
        m=len(s)
        n=len(t)
        if(m<1 or m>10**5 or n>m ):
            return ""
        else:
            output_str=""
            final_str=""
            for char in s:
                if(t_len==0):
                    final_str=""
                    t_len=len(t)
                    t_dict=Counter(t)

                if char in t_dict:
                    if(t_dict[char]!=0):
                        final_str=final_str+char
                        t_dict[char]-=1
                        t_len=t_len-1
                    
                else:
                    if(final_str!=""):
                        final_str=final_str+char
                    
                
                if(t_len==0):
                    if(output_str ==""):
                        output_str=final_str
                    else:
                        if(len(final_str)<len(output_str)):
                            output_str=final_str
                            
            return output_str
        
c=Solution()
print(c.minWindow("ADOBECODEBANC","ABC"))
            