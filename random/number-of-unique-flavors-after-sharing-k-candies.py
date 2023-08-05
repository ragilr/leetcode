class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        if k == 0:
            return len(set(candies))
    
        d =dict()
        for i in range(k,len(candies)):
            d[candies[i]]=d.get(candies[i],0)+1
        m = 0
        p=candies[0]
        for i in range(len(candies)-k+1):
            # print(d,candies[i:i+k],m)
            m = max(m,len(d))
            if i+k<len(candies):
                d[p]=d.get(p,0)+1
                d[candies[i+k]]-=1
                if d[candies[i+k]]==0:
                    del d[candies[i+k]]
                p=candies[i+1]
        return m