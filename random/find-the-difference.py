class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        f = [0]*26
        for c in s:
            f[ord(c)-ord('a')]+=1
        for c in t:
            f[ord(c)-ord('a')]-=1
        c = ''
        for i in range(26):
            if f[i]!=0:
                c = chr(ord('a')+i)
                break
        return c
        