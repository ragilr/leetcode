class Solution:
    def arrangeCoins(self, n: int) -> int:
        c=1
        while n>0:
            n=n-c
            c=c+1
        if n==0:
            return c-1
        return c-2            