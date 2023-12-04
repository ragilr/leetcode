class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l = len(s)
        res = set()
        for i in range(l-k+1):
            res.add(s[i:i+k])
        return len(res)==(1<<k)