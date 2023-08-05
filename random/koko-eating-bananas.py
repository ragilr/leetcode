import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:       
        def can_eat_all(k):
            c=0
            for b in piles:
                c += math.ceil(b/k)
            return c<=h

        if len(piles)==1:
            return math.ceil(piles[0]/h)
        l = 1
        r = max(piles)
        m = (l+h)//2
        i = 0
        c = 0
        result = r
        while(l<r):
            print("Before",l,r,c,result)
            m = (l+r)//2
            if can_eat_all(m):
                r = m
            else:
                l = m+1
            print("After",l,r,c,result)
        return r
        