class Solution:
    def reverseWords(self, s: str) -> str:
        l=0
        ret=""
        for i in range(len(s)):
            if s[i]==' ':
                ret+=self.reverse(s[l:i])
                # ret+=" "
                if l ==0:
                    ret+=" "
                # print(ret,".")
                l=i
        ret+=self.reverse(s[l:])
        if(l>0):
            ret=ret[0:-1]
        return ret
    
    def reverse(self, s:str) -> str:
        j=len(s)-1
        ret=""
        while j>-1:
            ret = ret + s[j]
            j=j-1
        return ret
    
        
        