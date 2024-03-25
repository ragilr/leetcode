class Solution:
    def countSubstrings(self, s: str) -> int:
        ret = 0
        for i in range(len(s)):
            l=r=i
            while l>-1 and r<len(s) and s[l]==s[r]:
                ret+=1
                l,r=l-1,r+1
            l,r=i,i+1
            while l>-1 and r<len(s) and s[l]==s[r]:
                ret+=1
                l,r=l-1,r+1
        return ret            