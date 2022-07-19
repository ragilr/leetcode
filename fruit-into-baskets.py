class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d=dict()
        i=0
        j=0
        m=float('-inf')
        print(fruits)
        while j<len(fruits):
            d[fruits[j]]=j
            if len(d)>2:
                # print('here')
                s=float('inf')
                for k,v in d.items():
                    if v<s:
                        s=v
                        dk=k
                i=s+1
                del d[dk]
            j+=1
            m=max(m,j-i)
        return m
        