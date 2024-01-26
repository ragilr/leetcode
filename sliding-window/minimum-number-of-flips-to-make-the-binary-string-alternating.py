class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s=s+s
        zeroStart = ''
        oneStart = ''
        for i in range(len(s)):
            if i & 1:
                zeroStart+='1'
                oneStart+='0'
            else:
                zeroStart+='0'
                oneStart+='1'
        m = float('inf')
        l = 0
        zeroDiff = oneDiff = 0
        for r in range(len(s)):
            if zeroStart[r]!=s[r]:
                zeroDiff+=1
            if oneStart[r]!=s[r]:
                oneDiff+=1
            if r-l+1>n:
                if zeroStart[l]!=s[l]:
                    zeroDiff-=1
                if oneStart[l]!=s[l]:
                    oneDiff-=1
                l+=1
            if r-l+1==n:
                m=min(m,zeroDiff,oneDiff)            
        return m