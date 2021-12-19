class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mega = {}
        res = []
        for w in strs:
            f = {}
            for c in w:
                f[c]=f.get(c,0)+1
            h = tuple(sorted(f.items()))
            if h in mega:
                i=mega[h]
                res[i].append(w)
            else:
                res.append([w])
                mega[h]=len(res)-1
        return res
        