class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d=dict()
        ret = 0
        l = 0
        tot = 0
        for r in range(len(fruits)):
            d[fruits[r]] = d.get(fruits[r],0)+1
            tot+=1
            while len(d)>2:
                fru = fruits[l]
                d[fru]-=1
                tot-=1
                if d[fru]==0:
                    del d[fru]
                l+=1
            ret = max(ret,tot)  
        return ret