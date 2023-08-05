class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d=dict()
        c=0
        for i in order:
            d[i]=c
            c+=1
        ret = ''.join(sorted(s,key= lambda x:d.get(x,float('inf'))))
        return ret