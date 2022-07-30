class Solution:
    def firstUniqChar(self, s: str) -> int:
        d=dict()
        for i,c in enumerate(s):
            if c in d:
                d[c]=float('inf')
            else:
                d[c]=i
        m = float('inf')
        for k,v in d.items():
            m = min(m,v)
        if m == float('inf'):
            m=-1
        return m