class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c = 0
        for i in range(0,len(s)-2):
            if s[i]!=s[i+1] and s[i+1]!=s[i+2] and s[i+2]!=s[i]:
                c+=1
        return c