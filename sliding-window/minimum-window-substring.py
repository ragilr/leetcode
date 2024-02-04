class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sc = Counter(s)
        tc = Counter(t)
        for k,v in tc.items():
            if k not in sc or sc[k]<v:
                return ''
        
        def doesSatisfy(curr):
            count = 0
            for k,v in tc.items():
                if k in curr and curr[k]>=v:
                    count+=1
                else:
                    break
            return count==len(tc)
        
        curr = {}
        l = 0
        r = 0
        m = float('inf')
        ret = ''
        for r,c in enumerate(s):
            curr[c] = curr.get(c,0)+1
            while doesSatisfy(curr):
                if r-l+1<m:
                    m=r-l+1
                    ret = s[l:r+1]
                curr[s[l]]=curr[s[l]]-1
                l+=1                                
        return ret        