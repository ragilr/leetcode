class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i = 0
        j = 0
        l = len(s)
        d = dict()
        res=0
        while j<l and i<l:
            d[s[j]] = d.get(s[j],0)+1
            while(d.get('a',-1)>0 and d.get('b',-1)>0 and d.get('c',-1)>0):
                d[s[i]]=d[s[i]]-1
                res+=l-j
                i+=1
            j+=1
        return res
            